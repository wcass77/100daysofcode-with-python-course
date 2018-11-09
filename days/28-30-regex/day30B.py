import re

import art
import requests

if __name__ == "__main__":
    # Get the front page of io9
    r = requests.get("https://io9.gizmodo.com/")
    # Get a list of the headlines, with HTML
    headlines = re.findall(
        r'<h1 class="headline entry-title js_entry-title">.*?<a.*?>(.*?)</a>', r.text
    )
    # Remove empty titles (these are not actual articles, but non-article links)
    headlines = [headline for headline in headlines if headline != ""]
    # Delete tags, fix non-breaking space, and apostrophes
    headlines = [
        re.sub(r"<.+?>", "", headline).replace(u"\xa0", u" ").replace("&#39;", "'")
        for headline in headlines
    ]
    # Make into ascii art, shorten so it doesn't wrap and print
    headlines = [art.text2art(headline[:24]) for headline in headlines]
    print(*headlines, sep="\n")
