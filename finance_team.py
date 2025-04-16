from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent_web = Agent(
    name = "Web agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["always include sources"]
)



agent_finance = Agent(
    name = "Finance agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data"]
)


agent_team = Agent(
    team = [agent_web, agent_finance],
    model = Groq(id="llama-3.3-70b-versatile"),    
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources","Use tables to display data"]
)
agent_team.print_response("Summarize analyst recommendations and share the latest news for TSLA",stream=True)