import bs4
import requests

URL = "https://www.addgene.org/50917/"
if __name__ == "__main__":

    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    references = soup.select(".indent.well.well-sm")
    m_m_reference = references[0].small.string
    print(m_m_reference)
