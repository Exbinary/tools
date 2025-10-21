#USAGE: cat wordlist.txt | python3 APIfuzzer.py
import requests
import sys

def loop():
    for word in sys.stdin:
        response = requests.get(url=f"0.0.0.0")
        if response.status_code == 404:
            loop()
        else:
            print(response)
            data = response.json()
            print(data)
            print(word)
                  

loop()
