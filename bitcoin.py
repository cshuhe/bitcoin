from requests_html import HTMLSession

session = HTMLSession()

url = 'https://api.blockcypher.com/v1/btc/test3/addrs/miAMpCdoM3SuRMRoEVHp8smFdDAz29WA9g'

response = session.get(url)

with open("Result.txt", "w") as f:
    f.write(response.html.full_text)
