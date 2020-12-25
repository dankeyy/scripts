#!/usr/bin/env python

from requests import get

url = lambda n: f'https://www.digitalwhisper.co.il/files/Zines/0x{n:02X}/DigitalWhisper{n}.pdf'
saveas = lambda n: f'/tmp/dw{n}.pdf'

n = int(input('issue to download?\n>'))
response = get(url(n)).content

with open(saveas(n), 'wb') as fil:
    fil.write(response)