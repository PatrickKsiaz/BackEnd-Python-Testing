import json


courses = '{"name": "Patryk Ksiazek","languages": ["Python","Java"]}'

#Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

#Get my the first language taught by trainer
#list_language = dict_courses(['languages'])
#print(type(list_language))
#print(list_language[0])

print(dict_courses['lanugages'][0])  # This will raise a KeyError because 'lanugages' is misspelled







