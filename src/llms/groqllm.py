from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

class GroqLLM:
    def __init__(self):
        load_dotenv()

        

    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
            self.llm = ChatGroq(api_key=self.groq_api_key , model = "llama-3.1-8b-instant")
            return self.llm
        except Exception as e:
            print(f"Error occurred while getting LLM: {e}")
            return None
        
        
