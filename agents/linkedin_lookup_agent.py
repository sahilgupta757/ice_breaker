import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts.prompt import PromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def get_profile_url_tavily(name:str):
    """
    searches for LinkedIN or Twitter profile page
    """

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]

def lookup(name: str) -> str:
    """ """
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.0-pro")

    template = """Given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page. Your answer should contain only a URL."""

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile",
            func=get_profile_url_tavily,
            description="Lookup a person's LinkedIn profile URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    return result["output"]


if __name__ == "__main__":
    linkedin_url = lookup("Sahil Gupta EY UIET")
    print(linkedin_url)
