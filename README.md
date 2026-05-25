# mini-search-engine
# Mini Search Engine

A full-stack search engine that indexes text documents and returns ranked results using the TF-IDF algorithm. Built with a FastAPI backend and a live UI hosted on GitHub Pages.

**Live Demo:** https://vakas100.github.io/mini-search-engine/  
**Backend API:** Deployed on Render

---

## Features

- Full-text search across indexed documents
- TF-IDF ranking to return the most relevant results first
- REST API backend with FastAPI
- Custom dataset generated via `dataset_creator.py`
- Clean UI hosted on GitHub Pages

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Python |
| Algorithm | TF-IDF (Term Frequency-Inverse Document Frequency) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render (backend), GitHub Pages (frontend) |

---

## How It Works

1. Text documents are generated and preprocessed at startup using `dataset_creator.py`
2. When a query is submitted, TF-IDF scores are computed across all documents
3. Results are ranked by relevance score and returned via the API
4. The frontend fetches results and displays them in order of relevance

---

## Project Structure

```
mini-search-engine/
├── main.py                # TF-IDF indexing and search logic
├── api.py                 # FastAPI routes and endpoints
├── dataset_creator.py     # Script to generate text documents for indexing
├── index.html             # Frontend UI (hosted on GitHub Pages)
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version for Render deployment
└── .gitignore
```

---

## Run Locally

```
# Clone the repo
git clone https://github.com/vakas100/mini-search-engine
cd mini-search-engine

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn api:app --reload
```

Then open `index.html` in your browser or visit `http://127.0.0.1:8000/docs` to explore the API.

---

## Future Improvements

- Add support for searching PDF and Word documents
- Implement BM25 ranking algorithm for better relevance scoring
- Add pagination to search results
- Store documents in a database instead of memory
