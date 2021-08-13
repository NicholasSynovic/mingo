from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from requests import get


def getPage(wikipediaPage: str) -> BeautifulSoup:
    page = get(url=wikipediaPage).text

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


if __name__ == "__main__":
    soup: BeautifulSoup = getPage(
        wikipediaPage="https://en.wikipedia.org/wiki/List_of_programming_languages"
    )

    languages: set = getProgrammingLanguage(soup=soup)

    exportProgrammingLanguages(data=languages)
