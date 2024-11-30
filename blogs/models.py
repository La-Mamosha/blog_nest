from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    #Atributos de Category
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Metodos de Category
    # Es heredado desde el Models.model y tiene un metodo que se llama VerboseName
    class Meta: 
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.category_name



STATUS_CHOICES = (
    ('Draft', 'Borrador'), 
    ('Publish', 'Publicado') 
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Relacion con otra tabla 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.TextField(max_length=20, choices=STATUS_CHOICES, default='Draft') #Publicado o modo borrador
    is_featured = models.BooleanField(default=False) #Destacado
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



"""from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=(('Draft', 'Borrador'), ('Published', 'Publicado')), default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Verifica si el slug ya existe y si es nulo o vacío
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Blog, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        # Verifica si el slug ya existe en la base de datos y genera uno único
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def __str__(self):
        return self.title
"""

