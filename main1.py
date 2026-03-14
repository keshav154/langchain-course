from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field
from langchain.agents.structured_output import ToolStrategy
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


load_dotenv()
llm = ChatOllama(model="qwen3.5:0.8b")
tools=[TavilySearch(num_results=1)]
agent = create_agent(llm, tools=tools, response_format=ToolStrategy(AgentResponse))
def main():
    print("Hello from AI agent")
    response = agent.invoke({"messages": [HumanMessage(content="Give me the two best job listings in Noida Uttar pradesh for Senios devops engineer positions on Linkedin mentioning the URL and description of it")]})
    print(response)
if __name__ == "__main__":
    main()