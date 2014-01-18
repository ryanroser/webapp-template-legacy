"""
This script contains some example steps that correspond to the
features provided in first.feature

- *Author* - Ryan Roser
- *Date* - Blah

"""

from behave import *



@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
