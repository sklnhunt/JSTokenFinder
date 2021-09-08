# import requests

# def alivechecker(domain):
#     try:
#         prefixdomain = 'http://'+ domain 
#         if requests.head(prefixdomain).status_code == 200:
#             print(prefixdomain)

#         prefixdomain = 'https://' + domain
#         if requests.head(prefixdomain).status_code == 301:
#             print(prefixdomain)

#     except requests.exceptions as err:
#         print(err)            

# alivechecker('example.com')


import http.client
from urllib.parse import urlparse

def alivechecker(url):
    url = urlparse(url)
    conn = http.client.HTTPSConnection(url.netloc)
    conn.request('HEAD', url.path)
    if conn.getresponse():
        return True
    else:
        return False


if __name__ == '__main__':
    url = 'http://dell.com'
    url_https = 'https://' + url.split("//")[1]
    if alivechecker(url_https):
        print('https working')
    else:
        if alivechecker(url):
            print('only http')
    if alivechecker(url):
        print('it load with http too!!')        
