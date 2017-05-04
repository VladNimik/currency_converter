from bs4 import BeautifulSoup


def parseTable():
    # table from http://www.xe.com/symbols.php
    html = open("CommonCurrency.html", 'r')

    # http://stackoverflow.com/questions/18544634/convert-a-html-table-to-json
    html = [[cell.text for cell in row("td")]
            for row in BeautifulSoup(html, "html.parser")("tr")]

    dictionary = {}
    for obj in html:
        dictionary[obj[1]] = obj[3]

    return dictionary
