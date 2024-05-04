import os
import requests
from dotenv import load_dotenv


load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape linkedin information
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/sahilgupta757/67765d447fdd89e04c10029bd207ef2b/raw/1a9639ff9771cbb455e58428fd2e905bdd143389/ice-breaker.json"

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

    return response


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            "https://www.linkedin.com/in/anthony-ndou/",
            mock=True
        )
    )
