# 📄 DocChat — Chat with your PDFs

🔗 **[Live demo](https://docchat---ask-your-pdf-n7ntsv4kkwnem5awr63ha8.streamlit.app/)** _(add once deployed)_

![demo](assets/demo.gif)

## What it does
Upload a PDF, ask questions about it, and get answers grounded in the actual document
(retrieval-augmented generation) instead of the model guessing.

## How it works
1. Extract text from the PDF
2. Split into overlapping chunks
3. Embed chunks with a sentence-transformer, index with FAISS
4. On a query: retrieve the top-k most relevant chunks, pass them + the question to an LLM
5. Return the answer along with which chunks it used

## Tech stack
Streamlit · sentence-transformers · FAISS · OpenAI API

## Run locally
```bash
git clone https://github.com/you/docchat
cd docchat
pip install -r requirements.txt
export GROQ_API_KEY=YOUR_API_KEY
streamlit run app.py
```

## What I learned
_(2-3 honest sentences once you've built it — e.g. chunk size trade-offs, retrieval
quality issues, prompt engineering to reduce hallucination)_

## Possible improvements
- Multi-document support
- Sentence-aware chunking instead of fixed word count
- Swap in a local LLM to remove API dependency
