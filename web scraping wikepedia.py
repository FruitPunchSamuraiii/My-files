import requests
from bs4 import BeautifulSoup

# 1. Always set a User-Agent header (required for Wikipedia)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# 2. Instead of using index numbers (e.g. soup.find_all('table')[2]),
# target the table specifically by class or parent class
target_table = soup.find('table', {'class': 'wikitable'})

# Print the table rows
if target_table:
    rows = target_table.find_all('tr')
    for row in rows[:5]:  # First 5 rows
        print([cell.text.strip() for cell in row.find_all(['th', 'td'])])