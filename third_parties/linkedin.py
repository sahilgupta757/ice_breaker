import os
import requests
from dotenv import load_dotenv


load_dotenv()


def scrape_linkedin_profile(
    linkedin_profile_url: str,
    mock: bool = False,
) -> dict:
    """
    scrape linkedin information

    Args:
        linkedin_profile_url (str): linkedin profile url
        mock (bool, optional): set to True to mock response

    Returns:
        dict: linkedin information
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/sahilgupta757/67765d447fdd89e04c10029bd207ef2b/raw/bd67d14b7066986a39faea56b73bdd187c9b65ad/ice-breaker.json"

        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    else:
        endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        headers = {
            "Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}",
        }
        response = requests.get(
            endpoint, params={"url": linkedin_profile_url}, headers=headers, timeout=10
        )

    return {k: v for k, v in response.json().items() if v}


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            "https://www.linkedin.com/in/anthony-ndou/",
            mock=True,
        )
    )
