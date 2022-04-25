#!/usr/bin/env python3

import requests

def main() -> None:
    param = { 'id':'dvere', 'key':'helloworld'}
    response = requests.post("https://turing.gjh.sk/", data=param)
    print(response.json())

if __name__ == "__main__":
    main()
