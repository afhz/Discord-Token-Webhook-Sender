import time, requests, json
from colorama import init
from colorama import init, Fore, Back, Style

init()

messages = open('tokens.txt', 'r').readlines()
webhook_url = "webhok"

latest = -1
def get_latest_message():
    global latest
    latest += 1
    if latest > len(messages):
        latest = 0
    return messages[latest].strip("\n")

while True:
    time.sleep(1)
    print(Fore.GREEN + '[+] Token has been sent')

    requests.post(webhook_url, headers={"content-type":"application/json"}, json={'content':get_latest_message()})

init(convert=True)