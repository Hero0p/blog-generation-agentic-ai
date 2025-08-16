import uvicorn
from fastapi import FastAPI , Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM    

import os
from dotenv import load_dotenv
load_dotenv

app = FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##  API's

@app.post("/blogs")
async def create_blog(request: Request):
    data = await request.json()
    topic = data.get("topic" , "")
    