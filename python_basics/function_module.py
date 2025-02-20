#module 1

# def make_pizza(size, *toppings):
#     """Summarize a pizza what we are about to make!"""
#     print(f"\nWe are making {size}-size pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# module 2 

def print_models(unprinted_designs,completed_models):
    """ Simulate printing each design, util none are left """
    """Move each design to completed_models after printing """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing design: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Diplay all completed models """
    print("\nThe following models are printed:")
    for completed_model in completed_models:
        print(f"- {completed_model}")


