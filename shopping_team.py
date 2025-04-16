from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.firecrawl import FirecrawlTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

shopping_agent = Agent(
    name="shopping partner",
    model = Gemini(id="gemini-2.5-pro-exp-03-25"),
    instructions=[
        "You are a product recommender agent specializing in finding products that match user preferences.",
        "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%.",
        "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, Meesho, Nike, and other reputable platforms.",
        "Verify that each product recommendation is in stock and available for purchase.",
        "Avoid suggesting counterfeit or unverified products.",
        "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
        "Format the recommendations neatly and ensure clarity for ease of user understanding.",
    ],
    tools=[FirecrawlTools()],
)


web_agent = Agent(
    name = "Web agent",
    model = Gemini(id="gemini-2.5-pro-exp-03-25"),
    tools = [DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["always include sources"]
)

team_agent = Agent(
    team = [shopping_agent, web_agent],
    model = Gemini(id="gemini-2.5-pro-exp-03-25"),    
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data","always include sources"]
)

team_agent.print_response("I am looking for MCR shoes with the following preferences: Color: not black Size: UK7 Purpose: Comfortable for long-distance walking Budget: Under Rs. 10,000 and share latest developments on footwear for diabetic patients",stream=True)
