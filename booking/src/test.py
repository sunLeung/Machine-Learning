#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import random
import hashlib

if __name__ == '__main__':
    s = requests.session()
    print(s.cookies)
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    print(s.cookies)
    r = s.get("http://httpbin.org/cookies")
    print(s.cookies)
    print(r.text)
