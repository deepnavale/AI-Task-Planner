import os
import requests
from dotenv import load_dotenv
from datetime import datetime

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor

load_dotenv()

tavily_tool = TavilySearchResults(max_results=3)

def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key is not set."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The current weather in {city} is {weather_description} with a temperature of {temperature}°C."
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"
    except KeyError:
        return f"Could not find weather data for '{city}'."

weather_tool = Tool(
    name="WeatherFetcher",
    func=get_weather,
    description="Use this tool to get the current weather for a specific city. Input should be a city name.",
)

tools = [tavily_tool, weather_tool]

llm = ChatGroq(
    temperature=0,
    model_name="qwen/qwen3-32b",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt_template = """
You are an expert AI planning assistant. Your job is to create clear, actionable plans.
Answer the following goal as best you can. You have access to the following tools:
{tools}
Use the following format:
Goal: the user's goal you must create a plan for
Thought: you should always think about what to do to solve the goal.
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now have enough information to create the final plan.
Final Answer: [A comprehensive, well-structured plan in clean Markdown format. Your final plan MUST follow these rules:
1. Structure day-by-day plans with specific time slots (e.g., 9:00 AM - 11:00 AM, 1:00 PM - 3:00 PM).
2. Keep the description for each step concise and to the point.
3. If the goal involves a location, you MUST include the weather information you found.
]
Begin!
Goal: {input}
Thought:{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(prompt_template)

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def generate_plan(goal: str):
    try:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        enriched_goal = f"{goal}\n\n(Context: For your planning, today's date is {current_date}.)"
        response = agent_executor.invoke({"input": enriched_goal})
        return response["output"]
    except Exception as e:
        return f"An error occurred while generating the plan: {e}"

