import requests


requests.post('http://216.10.245.166/Library/Addbook.php',
              json={
    "name": "Learn Appium with Java",
    "isbn": "bcd",
    "aisle": "227",
    "author": "John Foe"
},headers={"Content-Type": "application/json"},)

print(addbook_response.json())
response_json = addbook_response.json()
print(type(response_json))

bookId = response_json['ID']

#Delete Book 