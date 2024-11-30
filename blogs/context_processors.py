from .models import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

# categories = nombre de la propiedad
# categories = data