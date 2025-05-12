# Function 1 

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    fullname = f"{first} {last}"
    return fullname.title()

# Function 2 

def get_formatted_name2(first, middle, last):
    """Generate a neatly formatted full name."""
    fullname = f"{first} {middle} {last}"
    return fullname.title()

# Function 3

def get_formatted_name3(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.title()

 
# Class 1 


class AnonymousSurvey():
    """Collect anonymous answers to a survey questions."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey Result:")
        for response in self.responses:
            print(f"- {response}")

        