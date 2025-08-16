from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(description = "The title of the blog post")
    content: str = Field(description = "The content of the blog post")
    

class BlogState(TypedDict):
    """
    Represents the state of a blog post.
    """
    topic: str
    blog: str
    current_language : str

