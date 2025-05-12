# Test Your Code 

# Installing pytest 


# Testing a Function 

# from functions_module_testing import get_formatted_name

# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break

#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly formatted name: {formatted_name}")


# Unit Tests and Test Cases 

# A Passing Test 

# from functions_module_testing import get_formatted_name

# def test_first_last_name():
#     """Do names like 'Neo Lin' work?"""
#     formatted_name = get_formatted_name('neo', 'lin')
#     assert formatted_name == 'Neo Lin'

# Running a Test 


# A Failing Test 

# from functions_module_testing import get_formatted_name2

# def test_frist_last_name():
#     """Do names like 'Neo Lin' work?"""
#     fullname = get_formatted_name2('neo', 'lin')
#     assert fullname == 'Neo Lin'


# Responding to a Failed Test 

# from functions_module_testing import get_formatted_name3

# def test_first_last_name():
#     """Do names like 'Neo Lin' work?"""
#     fullname = get_formatted_name3('neo', 'lin')
#     assert fullname == 'Neo Lin'

# Adding New Tests 

# from functions_module_testing import get_formatted_name3

# def test_first_middle_name():
#     """Do names like 'Naing Lin Ang' work?"""
#     fullname = get_formatted_name3('naing', 'aung', 'lin')
#     assert fullname == "Naing Lin Aung"

# -----------------------------------------------------------------------------

# Exercises 

# 11.1 City, Country 

# def city_function(city, country):
#     """Generate a neatly formatted for cities and their countries."""
#     formatted_name = f"{city}, {country}"
#     return formatted_name.title()

# def test_city_country_name():
#     """Do names like 'Yangon, Myanmar' work?"""
#     formatted_name = city_function('yangon', 'myanmar')
#     assert formatted_name == 'Yangon, Myanmar'


# 10.2 Population 

# def city_function(city, country, population):
#     """Generate a neatly formatted text for cites, country and population."""
#     formatted_text = f"{city.title()}, {country.title()} - population {population}"
#     return formatted_text

# def test_city_country_population():
#     """Verify the name like 'Yangon, Myanmar - population 1000000' work?"""
#     fomatted_text = city_function('yangon', 'myanmar', 1000000)
#     assert fomatted_text == 'Yangon, Myanmar - population 1000000'

# -----------------------------------------------------------------------------

# Testing a Class 


# A Variety of Assertion 


# A Class to Test 

# from functions_classes_module_testing import AnonymousSurvey

# # Define a question, and make a survey. 
# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)

# # Show the question, and store responses to the question
# language_survey.show_question()
# print("Enter 'q' at any time to quit.")

# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     language_survey.store_response(response)

# # Show the Survey Result 
# print("\nThank you to everyone who participated in the survey!")
# language_survey.show_results()


# Testing the AnonymousSurvey Class 

# from functions_classes_module_testing import AnonymousSurvey

# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# def test_store_three_responses():
#     """Test that three responses is stored properly."""
#     question = "What language did you first learn to speak?"
#     langauage_survey = AnonymousSurvey(question)
#     responses = ['English', 'Burmese', 'Spanish']
#     for response in responses:
#         langauage_survey.store_response(response)

#     for response in responses:
#         assert response in langauage_survey.responses


# Using Fixture 

# import pytest
# from functions_classes_module_testing import AnonymousSurvey

# @pytest.fixture
# def language_survey():
#     """A survey that will be available to all test functions."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     return language_survey

# def test_store_single_response(language_survey):
#     """Test that a single response is stored properly."""
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# def test_store_theree_responses(language_survey):
#     """Test that three responses is stored properly."""
#     responses = ['English', 'Spanish', 'Burmese']
#     for response in responses:
#         language_survey.store_response(response)

#     for response in responses:
#         assert response in language_survey.responses

# -----------------------------------------------------------------------------

# Exercises 

# 11.3 Employee

# class Employee():
#     """Model of the Employee information."""

#     def __init__(self, first_name, last_name, annual_salary):
#         """Initilize to model an employee."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.annual_salary = annual_salary

#     def give_raise(self, amount=5000):
#         """Give rasie to annual salary."""
#         self.annual_salary += amount

# No Fixture 

# def test_give_default_raise():
#     """Test that default amount is added to salary properly."""
#     employee = Employee('neo', 'lin', 50000)
#     employee.give_raise()
#     assert 55000 == employee.annual_salary

# def test_give_custom_rasie():
#     """Test that custom amount is added to salary properly."""
#     employee = Employee('neo', 'lin', 50000)
#     employee.give_raise(10000)
#     assert 60000 == employee.annual_salary


# import pytest

# @pytest.fixture
# def employee():
#     """An employee function that will be available for all tests."""
#     employee = Employee('neo', 'lin', 50000)
#     return employee

# def test_give_default_raise(employee):
#     """Test that default amount is added to salary properly."""
#     employee.give_raise()
#     assert 55000 == employee.annual_salary

# def test_give_custom_raise(employee):
#     """Test that default amount is added to salary properly."""
#     employee.give_raise(10000)
#     assert 60000 == employee.annual_salary    