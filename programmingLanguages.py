from bs4.element import ResultSet, Tag
from requests import get
from bs4 import BeautifulSoup

def getWikiPage()    ->  BeautifulSoup:
    page = get(url="https://en.wikipedia.org/wiki/List_of_programming_languages").text

    return BeautifulSoup(markup=page, features="lxml")

def getProgrammingLanguage(soup: BeautifulSoup) ->  set:
    data: set = set()

    letters: ResultSet = getWikiPage().findChildren(name="div", attrs={"class":"div-col"})



q: BeautifulSoup = getProgrammingLanguage()

x: Tag
for x in t:
    data: ResultSet = x.findChildren(name="li")

    print(data)
