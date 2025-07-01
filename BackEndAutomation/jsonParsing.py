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


#****************** Parse content present in JSON file

with open('C:\\Users\\Owner\\Documents\\course.json') as f:
    data = json.load(f)  # This will parse the JSON file and return a dictionary
    print(data)
    print(type(data))
    print(data['courses'][1]['title']) # Accessing the title of the second course
    print(data(['dashboard']['website'])) # Accessing the website under dashboard
    print(type(data['dashboard']))  # This will print the type of the dashboard key, which is a dictionary

#price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
            print(course)
            if course['title'] == 'RPA':
                print(course['price'])
                assert course['price'] == 45

with open('C:\\Users\\Owner\\Documents\\course1.json') as fi:
    data2 = json.load(fi)  # This will parse the JSON file and return a dictionary
    assert data == data2  # This will compare the two dictionaries













