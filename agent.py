from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

from tools.weather_tool import get_weather
from tools.news_tool import get_latest_news

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

tools = [get_weather, get_latest_news]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are Global Insight Agent.

Your job:
1. Get current weather for the location.
2. Get latest news for the same location.
3. Combine both into a clear final answer.

Always use both tools.
Keep answer short and useful.
"""
)

# if __name__ == "__main__":
#     response = agent.invoke(
#         {
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": "Give me current weather and latest news for Delhi"
#                 }
#             ]
#         }
#     )
#
#     print(response["messages"][-1].content)