import requests
import pyperclip as pc
import json
import os
from time import sleep


def parse(data):
    pre = data[0]
    q = pre['questions']
    a = 0
    for i in range(10):
        temp = q[a]
        qa = temp['text']
        temp2 = qa.split('>')
        qs = temp2[1].split('<')
        an0 = temp['options'].split('*||*')
        if 'true' in an0[0]:
            an1 = json.loads(an0[0])
        else:
            an1 = json.loads(an0[1])
        ans = an1['option']
        print(f'Question: {qs[0]}\nAnswer: {ans}')
        a += 1


def main():
    lid = input('Enter grammarflip url: ')
    pd = lid.split('/')
    url = f'https://api-curriculum.grammarflip.com/quiz/getall?lessonID={pd[-1]}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0',
               'Accept': 'application/json', 'apikey': 'put api key here'}
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        print('Success!')
        sleep(1)
        # pc.copy(r.text)
        # print('Copied to clipboard')
        print('Parsing pre-test...')
        sleep(1)
        parse(r.json())
    else:
        print(f'Error: {r.status_code}')


if __name__ == '__main__':
    if os.name == 'nt':
        os.system('title "Grammarflip Helper"')
    main()
else:
    exit(69)
