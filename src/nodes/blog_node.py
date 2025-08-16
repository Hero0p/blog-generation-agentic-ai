from src.states.blogstate import BlogState


class BlogNode:
    def __init__(self,llm):
        self.llm = llm

    def title_creation(self , state:BlogState):
        """
        creates the title
        """

        if "topic" in state and state["topic"]:
            prompt = """
                you are an expert blog content writer. Use Markdown formatting. Generate blog title 
                for the topic : {topic} .The title should be creative and SEO friendly
            """

            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog" : {"title":response.content}}
        
    def content_generation(self , state:BlogState):
        """
        creates the content
        """

        if "topic" in state and state["topic"]:
            prompt = """
                you are an expert blog content writer. Use Markdown formatting. Generate a detailed blog content with a detailed breakdown
                for the topic : {topic} .The content should be informative and engaging
            """

            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog" : {"content":response.content}}
        