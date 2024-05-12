import os

from dotenv import load_dotenv
from pprint import pprint
from langchain.chains import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile

def ice_break_with(name: str) -> str:
    """
    Ice break with a person
    """

    linkedin_profile_url = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url, mock=True)

    summary_template = """
        given the information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-1.0-pro")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": linkedin_data})
    pprint(res)



if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    ice_break_with(name="Eden Marco")
