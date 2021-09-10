import requests

from bs4 import BeautifulSoup


url = "https://www.youtube.com/"
response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")


for i in soup.find_all("a"):
    print(i)
    print("************************************************")