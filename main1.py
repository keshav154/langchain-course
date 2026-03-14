from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
load_dotenv()
llm = ChatOllama(model="qwen3.5:0.8b")
tools=[TavilySearch(num_results=1)]
agent = create_agent(llm, tools=tools)
def main():
    print("Hello from AI agent")
    response = agent.invoke({"messages": [HumanMessage(content="Give me the two best job openings in Noida Uttar pradesh for Senios devops engineer positions on Linkedin mentioning the URL and description of it")]})
    print(response)
if __name__ == "__main__":
    main()