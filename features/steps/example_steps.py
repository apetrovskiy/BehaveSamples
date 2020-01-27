from behave import given, when, then, step


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.my_data = "my string data"
    print(number)
    context.tests_count = number


@then('behave will test them for us!')
def step_impl(context):
    print("context output")
    print(context.tests_count)
    print(context.my_data)
    print("end")
    assert context.failed is False
    assert context.tests_count >= 0