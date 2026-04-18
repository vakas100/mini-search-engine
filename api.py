from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List
from main import load_files, preprocess, inverted_index, user_query, lookup, calculate_tfidf, get_result

app = FastAPI()

class SearchResult(BaseModel):
    rank: int
    filename: str
    score: float
    snippet: str


data = load_files()
processed_data = preprocess(data)
inverted_dict = inverted_index(processed_data)

@app.get('/',response_model=List[SearchResult])
def search(query: str):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    query_processed = user_query(query)
    result = lookup(query_processed, inverted_dict)

    if not result:
        return []

    rankings = calculate_tfidf(query_processed, result, processed_data)
    output = get_result(rankings,data)

    return output

if __name__ == "__main__":
    uvicorn.run('api:app', reload=True)