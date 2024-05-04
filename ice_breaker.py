import os

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")

    information = scrape_linkedin_profile(
        "https://www.linkedin.com/in/anthony-ndou/",
        mock=True,
    )

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
    res = chain.invoke(input={"information": information})

    print(res)
