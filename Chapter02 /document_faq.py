import streamlit as st
import time

from elasticsearch import Elasticsearch
from openai import OpenAI


def elastic_search(query):
    es_client = Elasticsearch('http://localhost:9200')
    index_name = "course-questions"
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    
    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    return result_docs

def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
        context = context + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
    )

    response = client.chat.completions.create(
        model='gemma:2b',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

# Define the function you want to execute (e.g., your RAG function)
def rag_function(query, show_logs):
    st.write(f"Executing rag_function with input: {query}")
    search_results = elastic_search(query)
    st.write(f"result from elastic search: \n {search_results[0].get('text', '')}")
    prompt = build_prompt(query, search_results)
    st.write('building prompt completed. running llm')
    answer = llm(prompt)
    return answer

def main():
    st.title('Simple Rag function using phi3')

    # Input box for user question
    user_input = st.text_input('Enter your question:')

    show_logs = st.checkbox("Show Logs")

    # Button to trigger the function execution
    if st.button('Ask'):
        # Display loading message while executing
        with st.spinner('Running RAG function...'):
            
            # Call your function
            result = rag_function(user_input, show_logs)
            # Display the result
            st.success(result)

if __name__ == "__main__":
    main()
