
`
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
`


`
docker exec -it ollama bash
ollama pull phi3
`