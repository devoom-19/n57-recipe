from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'pages/about.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

def category_page(request):
    return render(request, 'recipes/category.html')

def recipe_page(request):
    return render(request, 'recipes/recipe-with-sidebar.html')

def blog_page(request):
    return render(request, 'blogs/blog-grid.html')

def submit_page(request):
    return render(request, 'recipes/submit-recipe.html')

def login_page(request):
    return render(request, 'auth/login.html')