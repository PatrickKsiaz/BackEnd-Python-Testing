import requests

#http://rahulshettyacademy.com

#'visit-month'
cookie = {'visit-month': 'February',}
response = requests.get('https://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)    # allow_redirects=False will not follow the redirect
#301,200
print(response.history)
print(response.status_code)


se = requests.session()
se.cookies.update({'visit-month': 'February',}) 


res = requests.get("https://httpbin.org/cookies", cookies={'visit-month': '2022',})
print(res.text)


#Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r = requests.post(url,files = files)
print(r.status_code)
print(r.text)

