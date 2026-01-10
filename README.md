# RAG-study-buddy-proto

## How to Run

1. Fill in your `api_key` variable in `generate/answer.py`.

2. Run the vector database (Weaviate):

   ```bash
   docker run -d -p 8080:8080 semitechnologies/weaviate

   ```

3. Create a folder named `datalake` and place your PDF file inside it:

   ```bash
   mkdir datalake
   ```

4. Run the study buddy with a document and a question:

   ```bash
   python cli.py "document.pdf" "what is the main topic of this document?"
   ```
