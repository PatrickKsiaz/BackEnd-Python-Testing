
from PayLoad import *
import configparser
import json
from utilities.configurations import *
from utilities.resources import *


import requests

url = getConfig['API']['endpoint']+ ApiResources.addBook
headers = {"Content-Type": "application/json"}
quey= 'select * from Books'
addBook_response = requests.post(url,json=buildPayloadFromDB("fefrewe"),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))


bookId = response_json['ID']

#Delete Book  - 

response_deleteBook = requests.post('http://216.10.245.166/Library/Deletebook.php',
              json={
"ID": bookId
              },headers={"Content-Type": "application/json"},
    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'

# Authentication
se = requests.Session() # Create a session object
se.auth = ('rahulshettyacademy', getPassword()) #Authentication using session



url = "https://api.github.com/user"
github_respones = requests.get(url,verify=False,auth=('rahulshettyacademy', getPassword()))

print(github_respones.status_code)


url2 = "https://api.github.com/user/repos"
response = se.get(url2,auth=('rahulshettyacademy', getPassword()))
print(response.status_code)


