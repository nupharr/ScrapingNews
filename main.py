import requests
from bs4 import BeautifulSoup
import csv


url = "https://ria.ru/"
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "lxml")


content = soup.find("div", class_="cell-list__list")


a_titles = content.find_all("a", "cell-list__item-link color-font-hover-only")
a_dates = content.find_all("div", class_="cell-info__date")

titles = [x["title"] for x in a_titles]
links = [x["href"] for x in a_titles]
dates = [x.text for x in a_dates]

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(("Название", "Дата", "Ссылка"))

    for title, date, link in zip(titles, dates, links):
        writer.writerow([title, date, link])
