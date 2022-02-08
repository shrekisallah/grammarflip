
import json
import os
from time import sleep

import requests


def parse(data, thing):
    pre = data[thing]
    q = pre['questions']
    for i in range(10):
        temp = q[i-1]
        qa = temp['text'].split('>')
        if 'span style' in str(qa):
            qs = qa[2].split('<')
        else:
            qs = qa[1].split('<')
        an0 = temp['options'].split('*||*')
        if 'true' in an0[0]:
            an1 = json.loads(an0[0])
        elif 'true' in an0[1]:
            an1 = json.loads(an0[1])
        elif 'true' in an0[2]:
            an1 = json.loads(an0[2])
        else:
            an1 = json.loads(an0[3])
        ans = an1['option']
        print(f'\nQuestion: {qs[0]}\nAnswer: {ans}')
        if qs[0] == '':
            print(f'Something went wrong\nQuestion Data: {qs}')
        if an1 == '':
            print(f'Something went wrong\nAnswer Data: {an0}')


def main():
    with open("config.json", 'r+') as f:
        text = f.read()
        qwe = json.loads(text)
        api = qwe["apikey"]
    if api == '':
        print('No apikey in config.json found')
        exit(404)
    lid = input('Enter grammarflip url: ')
    try:
        typ = int(input('Enter 1 for pre-test, 2 for PE1, etc: '))
    except ValueError:
        print("Enter a number this time.")
        main()
    typ -= 1
    pd = lid.split('/')
    url = f'https://api-curriculum.grammarflip.com/quiz/getall?lessonID={pd[-1]}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0',
               'Accept': 'application/json', 'apikey': f'{api}'}
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        print('Success!')
        sleep(0.5)
        # pc.copy(r.text)
        # print('Copied to clipboard')
        parse(r.json(), typ)
    else:
        print(f'Error: {r.status_code}')
    input('Press any key to exit...')


if __name__ == '__main__':
    if os.name == 'nt':
        os.system('title Grammarflip Helper')
    main()
else:
    exit(69)
