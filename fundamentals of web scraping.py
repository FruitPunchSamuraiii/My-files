from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/forms/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html') # parses the info in html format
print(soup.prettify())

soup.find('div') #finds first div tag
soup.find_all('div') #finds every div tag, href is hyperlink
soup.find_all("div", class_ = "col-md-12")
soup.find_all("p", class_ = "lead")
soup.find("p", class_ = "lead").text #find all does not allow you to use text 