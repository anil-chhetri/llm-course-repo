## steps for environment preparation.

`
pip install tqdm notebook==7.1.2 elasticsearch pandas scikit-learn
`

## topics to understand text search 

**vector space**: a vector space contains a collection of objects called vector which are numerical represntations of words, sentences and even documents. It is an algebric model that represent object like text as vectors, this makes it easy to determin the similarity between words or the relevance between search query and document.  Cosine similarity is often used to determine similary between vectors.
When using vectors space models, the way that representation are made is by identifying the context around the word in the text, and this capture the relative meaning. Vector space allows you to represent words and documents as vectors. 


**term document matrix (TDM)**: TDM represent document vectors in matrix form in which row correspond to the term in document, column correspond to the document in the corpus and cell correspond to weights of the terms.
there are various approaches for determining the terms's weight. 
- Binary weights: the weights take the values 0 and 1 where 1 reflect the presence and - reflect the absence of the term in a particular document. 
- Term frequency: the weights represent the frequency of the term in a specific documents. *the underlying assumption is that the higher the term fequency in a document, the more important it is for that document.
- Inverse document frequency: the idea is to assign higher weights to unusual terms, ie. terms that are not common on corpus. IDF is computed at the corpus level, not individual documents. 
- Term frequency inverse document frequency (TF-IDF): It values those terms that are not so common in the corpus (relatively high IDF), but still have some reasonable level of frequency.It is the most frequently used metrics for computing term weights in a vector space model. 

> When we are considering a DataFrame with column text, 
> the whole data frame is represented as corpus, and the row represent the document.


**CountVectorize**: it is a simple and efficient text preprocessing technique that converts text documents into a numerical representation based on token frequency. it provides a document term matrix that represent the occurance of tokens in each document. It doesn't consider the importance of tokens; it simiply counts the occurance. 

**TfidfVectorizer**: it is similar to countvectorize as it also convert the text document into a matrix representation. however it consider weight for each token in each document, considering both term frequency and inverse document frequency aspects. 

**Cosine Similarity**: Cosine similarity measures the cosine of the angle between two multi-dimensional vectors. The smaller the angle, the higher the cosine similarity. For example, if a word appears 30 times in one document and 5 times in another document, measurement by Euclidean distance places them far apart. But cosine similarity would detect a smaller angle between them, thus establishing a similarity.