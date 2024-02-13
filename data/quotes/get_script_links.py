"""Create valid episode script links from parsing the HTML from
a URL containing each script link."""

import enum
import requests
from bs4 import BeautifulSoup


# URL containing links for all scripts
ALL_SCRIPTS_URL = "https://seinfeldscripts.com/seinfeld-scripts.html"
# The base URL for each page containing an episode's script
BASE_SCRIPT_URL = "https://seinfeldscripts.com/"
# The first episode endpoint, for finding within the list of links
FIRST_EPISODE_ENDPOINT = "TheSeinfeldChronicles.htm"
# Total number of episodes
TOTAL_EPISODES = 180
# A list of User-Agent headers to use with requests, just in case one doesn't work.
HEADERS = [
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    },
    {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    },
]
# Request site HTML
REQ = requests.get(ALL_SCRIPTS_URL, headers=HEADERS[0])
# Create a soup object with page HTML
SOUP = BeautifulSoup(REQ.text, "html.parser")


def find_soup_links(soup):
    """Find all of the links in a soup object containing the
    extensions .htm or .html, and save to a list of links (strings).
    """
    links = []
    for link in soup.find_all("a"):
        # Convert the link object to a string
        link = str(link)
        # Check for the .htm/.html extension
        if ".htm" in link:
            links.append(str(link))
    # Return a list of link strings
    return links


# Extract desired links from a list of links (strings, not soup tag objects)
def extract_endpoints(links):
    """
    Right now, an item in the links list looks like this:
        <a href="TheMoney.html">The Money</a>

    The episode script links have either an '.htm' or '.html' extension.
    The link endpoints are enclosed by double quotes and extraneous text.
    """
    endpoints = []
    # links is a list of 'href' objects converted to strings
    for link in links:
        # The endpoints are encased in double quotes
        first_quote_index = link.find('"') + 1
        last_quote_index = link.rfind('"')
        # The endpoint text may not be for a valid script link at
        # this point - handled later
        endpoint_text = link[first_quote_index:last_quote_index].strip()
        endpoints.append(endpoint_text)
    # Return a list of strings, for enpoints extracted from links
    return endpoints


def find_episode_endpoints(endpoints):
    # Find where the script endpoints begin and end in the list of endpoints
    for i, endpoint in enumerate(endpoints):
        if FIRST_EPISODE_ENDPOINT in endpoint:
            start_index = i
    end_index = start_index + TOTAL_EPISODES
    script_endpoints = endpoints[start_index:end_index]
    return script_endpoints


def generate_script_links(episode_endpoints):
    # Create URLs using the base URL and the endpoints for each script's
    # page URL
    script_links = [f"{BASE_SCRIPT_URL}{endpoint}" for endpoint in episode_endpoints]
    return script_links


# Save links with .htm or .html extensions and convert to strings.
links = find_soup_links(SOUP)
# Extract the endpoints
endpoints = extract_endpoints(links)
# Find episode endpoints
episode_endpoints = find_episode_endpoints(endpoints)
# Create script page links
script_links = generate_script_links(episode_endpoints)
