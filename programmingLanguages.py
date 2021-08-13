from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from requests import get


def getWikiPage() -> BeautifulSoup:
    page = get(url="https://en.wikipedia.org/wiki/List_of_programming_languages").text

    return BeautifulSoup(markup=page, features="lxml")


def getProgrammingLanguage(soup: BeautifulSoup) -> set:
    data: set = set()

    letters: ResultSet = soup.findChildren(name="div", attrs={"class": "div-col"})

    letter: Tag
    for letter in letters:

        languages: ResultSet = letter.findAll("li")

        language: Tag
        for language in languages:
            data.add(language.text)

    return sorted(data)
