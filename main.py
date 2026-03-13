from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
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
agent = create_agent(llm, tools=tools)
def main():
    print("Hello from langchain-course!")
    response = agent.invoke({"messages": [HumanMessage(content="I want to get the listing of job openings in Linkeding for Gen AI engineer in Noida, India with their job description")]})
    print(response)
if __name__ == "__main__":
    main()