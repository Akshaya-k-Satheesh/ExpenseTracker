# Expense/context_processors.py

from .models import Category

def menu_links(request):
    # Fetch all categories from the Category model
    categories = Category.objects.all()
    return {'links': categories}
