# Testing The Code 

# Testing a Function 

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     fullname = f"{first} {last}"
#     return fullname.title()

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

# -----------------------------------------------------------------------------

# Unit Tests and Test Cases 

# -----------------------------------------------------------------------------

# A passing Test 

# def get_formatted_name(first, last):
#     """Genterate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()

# def test_first_last_name():
#     """Do names like 'janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# -----------------------------------------------------------------------------

# A failing test 

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()

# def test_first_last_name():
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# -----------------------------------------------------------------------------

# Responding to a Failed Test 

# def get_formatted_name(first, last, middle=''):
#     """Generate a neatly formatted full name."""
#     if middle:
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()

# def test_first_last_name():
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formatted_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'

# def test_first_middle_last_name():
#     """Do names like 'Naing Lin Aung' work?"""
#     formatted_name = get_formatted_name('naing', 'aung', 'lin')
#     assert formatted_name == 'Naing Lin Aung'

# -----------------------------------------------------------------------------

# Exercises 

# City, Country 

# def get_city_country_name(city, country):
#     """Generate City, Country names."""
#     names = f"{city}, {country}"
#     return names.title()

# def test_city_country():
#     """Do names like 'Santiago, Chile' work?"""
#     names = get_city_country_name('santiago', 'chile')
#     assert names == 'Santiago, Chile'

#     # <Passed>

# -----------------------

# Population 

# def get_city_country_name(city, country, population):
#     """Generate City, Country names."""
#     names = f"{city}, {country} - population {population}"
#     return names.title()

# def test_city_country():
#     """Do names like 'Santiago, Chile' work?"""
#     names = get_city_country_name('santiago', 'chile')
#     assert names == 'Santiago, Chile'

#     <Error>

# def get_city_country_population(city, country, population=''):
#     """Generate City, Country and Population."""
#     if population:
#         names = f"{city}, {country} - population {population}"
#     else:
#         names = f"{city}, {country}"
#     return names.title()

# def test_city_country():
#     """Do names like 'Santiago, Chile' work?"""
#     names = get_city_country_population('santiago', 'chile')
#     assert names == 'Santiago, Chile'

# def test_city_country_population():
#     """Don names like 'Santiago, Chile - Population 500000' work?"""
#     names = get_city_country_population('santiago', 'chile', 500000)
#     assert names == 'Santiago, Chile - Population 500000'

# -----------------------------------------------------------------------------

# Testing a Class 

# A variety of Assertions 

# A Class to a Test 

class AnonymousSurvey:
    """Collect anonyomus answers to a servey questions."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_responses(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

# # Define a question, and make a survey 
# question = "What language did you first learn to speak? "
# language_survey = AnonymousSurvey(question)

# # Show the question, and store responses to the question
# language_survey.show_question()
# print("Enter 'q' to at any time to exit.\n")
# while True:
#     response = input(question)
#     if response == 'q':
#         break
#     language_survey.store_responses(response)

# # Show the survey results
# print("\nThank you to everyone who participated in the survey.")
# language_survey.show_results()


# -----------------------------------------------------------------------------

# Testing the AnonymousSurvey Class 

# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak? "
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_responses('English')
#     assert 'English' in language_survey.responses

# def test_store_three_responses():
#     """Test that three individual responses are stored properly."""
#     question = "What language did you first learn to speak? "
#     language_survey = AnonymousSurvey(question)
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_responses(response)
    
#     for response in responses:
#         assert response in language_survey.responses

# -----------------------------------------------------------------------------

# Using Fixtures 

