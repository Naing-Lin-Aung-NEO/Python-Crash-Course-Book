from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Store the name of user."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return the name for the admin stie."""
        return self.name
    
class Topping(models.Model):
    """Store pizza name & toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    tp_name = models.TextField()

    def __str__(self):
        """Return toppings name."""
        return self.tp_name

