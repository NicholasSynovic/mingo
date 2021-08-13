from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from requests import get


def getPage(page: str) -> BeautifulSoup:
    page = get(url=page).text

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


def exportProgrammingLanguages(data: set) -> None:
    with open(file="languages.txt", mode="w") as file:
        file.writelines(data)
        file.close()
