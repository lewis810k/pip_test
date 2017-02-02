"""
requests를 테스트 해본다.
"""

import requests

r = requests.get('http://naver.com')
print(r.text)