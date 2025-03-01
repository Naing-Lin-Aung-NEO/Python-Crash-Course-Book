# Testing a Function

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# print("Enter 'q' it any time to quit.")
# while True:
#     first = input("\nPlease give me your first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me your last name: ")
#     if last == 'q':
#         break
    
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly Formatted Name : {formatted_name}.")

# Unit Tests and Test Cases 

# -----------------------------------------------------------------------------

# A Passing Test 

# def get_formatted_name(first, last):
#     """Generate a neatly formatted name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# def test_first_last_name():
#     """Do name like 'Janis Joplin' work? """
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# -----------------------------------------------------------------------------

# A Failing Test 

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

# def test_first_last_name():
#     """Do name like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# -----------------------------------------------------------------------------

# Responding to A Failed Test 

# def get_formatted_name(first, last, middle=''):
#     """Generate a neatly formatted name."""
#     if middle:
#         fullname = f"{first} {middle} {last}"
#     else:
#         fullname = f"{first} {last}"
#     return fullname.title()


# def test_first_last_name():
#     """Do name like 'Neo Lin' work?"""
#     formatted_name = get_formatted_name('neo', 'lin')
#     assert formatted_name == 'Neo Lin'

# -----------------------------------------------------------------------------

# Adding New Test 

# def get_formatted_name(first, last, middle=''):
#     """Generate a neatly formatted name."""
#     if middle:
#         fullname = f"{first} {middle} {last}"
#     else:
#         fullname = f"{first} {last}"
#     return fullname.title()

# def test_first_last_middle_name():
#     """Do name like 'Naing Lin Aung' work? """
#     formatted_name = get_formatted_name('naing', 'aung', 'lin')
#     assert formatted_name == 'Naing Lin Aung'

# -----------------------------------------------------------------------------

# Exercises 

# City , Country 

# def city_country(city, country):
#     """Generate name like this 'City, Country'."""
#     name = f"{city}, {country}"
#     return name.title()

# def test_city_country():
#     """Do name like 'Yangon, Myanmar' work?"""
#     formatted_name = city_country('yangon', 'myanmar')
#     assert formatted_name == 'Yangon, Myanmar'

# -------------------------
# # Population 
# def city_country(city, country, population):
#     name = f"{city}, {country} - population {population}"
#     return name.title()


# # def test_city_country():
# #     """Do name like 'Yangon, Myanmar' work?"""
# #     formatted_name = city_country('yangon', 'myanmar')
# #     assert formatted_name == 'Yangon, Myanmar' ---> failed


# def test_city_country_population():
#     info = city_country('yangon', 'myanmar', '1m')
#     assert info == 'Yangon, Myanmar - Population 1M' ---> passed 


# -----------------------------------------------------------------------------

# A Class To Test 

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_result(self):
        """Show all the responses that have been given."""
        print("Survey Results: ")
        for response in self.responses:
            print(f"- {response}")


# # Define a questions, and make a survey 

# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)


# # Show the question, and store response to the question.
# language_survey.show_question()
# print("Enter 'q' at any time to quit!")
# while True:
#     response = input('Language: ')
#     if response == "q":
#         break
#     language_survey.store_response(response)


# # Show the survey results 
# print("\nThank you to everyone who participated in the survey.")
# language_survey.show_result()

# -----------------------------------------------------------------------------

# Testing The Class

# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses


# def test_store_three_responses():
#     """Test that three individual responses are stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_response(response)

#     for response in responses:
#         assert response in language_survey.responses

# -----------------------------------------------------------------------------

# Using Fixtures 
# import pytest 

# @pytest.fixture
# def language_survey():
#     """A survey that will be available to all test functions."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     return language_survey

# def test_store_single_response(language_survey):
#     """Test the a single respone is stored properly."""
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# def test_store_three_responses(language_survey):
#     """Test that three individual responses are stored properly."""
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_response(response)

#     for response in responses:
#         assert response in language_survey.responses
# 

# -----------------------------------------------------------------------------

# Exercises 

# Employee

# class Employee:
#     """A class that describe employee info."""

#     def __init__(self, first_name, last_name, annual_salary):
#         """Initilize the attributes for employee info"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.annual_salary = annual_salary

#     def give_raise(self, custom_raise=''):
#         """Raise employee salary custom or default."""
#         if custom_raise:
#             self.annual_salary += custom_raise
#         else:
#             self.annual_salary += 5000
#         return self.annual_salary

# # test

# import pytest

# @pytest.fixture
# def employee():
#     employee = Employee('aung', 'lin', 100000)
#     return employee

# def test_give_default_raise(employee):
#     annual_salary = employee.give_raise()
#     assert annual_salary == 105000

# def test_give_custom_raise(employee):
#     annual_salary = employee.give_raise(10000)
#     assert annual_salary == 110000
