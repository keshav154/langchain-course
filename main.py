from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field
class Source(BaseModel):
    """
    Schema for the source used by the agent
    """
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """
    Schema for the response returned by the agent
    """
    answer: str = Field(description="The answer to the user's query")
    sources: List[Source] = Field(description="List of sources used to generate the answer")

# from tavily import TavilyClient
load_dotenv()
# tavily = TavilyClient()
# @tool
# def search(query: str) -> str:
#     """
#     Search for information on the internet.
#     args:
#         query: the search query
#         returns: the search results
#     """
#     print(f"Searching the {query}")
#     return tavily.search(query=query, num_results=5)
llm = ChatOpenAI()
tools=[TavilySearch(num_results=1)]
agent = create_agent(llm, tools=tools, response_format=AgentResponse)
def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages": [HumanMessage(content="I want to get the latest 2 listing of job openings for Gen AI engineer in Noida, India with their job description")]})
    print(response)
if __name__ == "__main__":
    main()