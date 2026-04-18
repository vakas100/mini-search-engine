from fastapi import FastAPI
import uvicorn
from typing import List
from main import load_files
from main import preprocess
from main import inverted_index
from main import user_query
from main import lookup
from main import calculate_tfidf
from main import get_result

app = FastAPI()

@app.get('/')
def search(query: str):
    data = load_files()
    processed_data = preprocess(data)
    inverted_dict = inverted_index(processed_data)

    query_processed = user_query(query)
    result = lookup(query_processed, inverted_dict)
    rankings = calculate_tfidf(query_processed, result, processed_data)

    output = get_result(rankings,data)

    return output

if __name__ == "__main__":
    uvicorn.run('api:app', reload=True)