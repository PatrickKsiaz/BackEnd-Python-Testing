from behave import *

@given('The Book details which needs to be added to Library')
def step_impl(context):
    #
    url = getConfig['API']['endpoint'] + ApiResources.addBook
    headers = {"Content-Type": "application/json"}
    pass

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    
@then ('Book is successfully added') 