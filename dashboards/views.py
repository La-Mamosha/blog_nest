from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from dashboards.forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

# Create your views here.
def categories(request):
    return render(request, 'dashboard/categories.html')


###############################################################################################################################################
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST) #Viene con los datos tipiado
        if form.is_valid(): #Validando los datos
            form.save() #Guardando los datos
            return redirect('categories') #Redireccionando a la pagina principal
    
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)

###############################################################################################################################################
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)

###############################################################################################################################################
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

###############################################################################################################################################
def posts(request):
    posts = Blog.objects.all() # Consulta la BD para devolver todos los posts
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)

###############################################################################################################################################
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES) #Viene con los datos tipiado y con archivos 
        if form.is_valid(): 
            post = form.save(commit=False) # Estara en memoria pero no en la BD aun
            post.author = request.user # Agregando el autor
            post.save() 
            
            title = form.cleaned_data['title'] # Capturar el titulo del post
            post.slug = slugify(title) + '-' + str(post.id) # Creando el slug a partir del titulo
            post.save()
            return redirect('posts') 
    
    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)


###############################################################################################################################################
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post =form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)

###############################################################################################################################################
def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')