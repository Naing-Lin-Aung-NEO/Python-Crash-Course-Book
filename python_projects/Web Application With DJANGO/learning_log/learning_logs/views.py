from django.shortcuts import render

def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')