#!/usr/bin/python3
"""
based on this tutorial
https://intranet.hbtn.io/rltoken/L2HhLK0iyncmurlkigh5yw
"""


from lxml import html
import requests


page = 'http://158.69.76.135/level0.php'


vote = {
    "id":"1448",
    "holdthedoor": "Submit"
}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(page, data=vote)
