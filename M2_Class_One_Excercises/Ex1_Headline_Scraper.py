# Build a headline scraper, using Beautiful Soup

import requests

# Download the desired page (in this case, the National Weather Service Norman Forecast Office main page)
nws_oun_page = requests.get('https://www.weather.gov/oun')
nws_oun_page.raise_for_status()

# to be completed later