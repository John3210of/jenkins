from behave import given, when, then

@given('I have two numbers: {num1:d} and {num2:d}')
def step_given_two_numbers(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('the calculator sums them')
def step_when_sums(context):
    context.result = context.num1 + context.num2

@then('I receive {expected_result:d} as result')
def step_then_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"
