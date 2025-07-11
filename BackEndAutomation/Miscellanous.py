import requests

#http://rahulshettyacademy.com

#'visit-month'
cookie = {'visit-month': 'February',}
response = requests.get('https://rahulshettyacademy.com',allow_redirects=False,cookies=cookie)
#301,200
print(response.history)
print(response.status_code)


se = requests.session()
se.cookies.update({'visit-month': 'February',}) 


res = requests.get("https://httpbin.org/cookies", cookies={'visit-month': '2022',})
print(res.text)


