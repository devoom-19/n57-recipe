from django.urls import path
from common.views import *

app_name = 'pages'

urlpatterns = [
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('category/', category_page, name='category'),
<<<<<<< HEAD
    path('blog/', blog_page, name='blog'),
=======
>>>>>>> 031e4426d2755a8cbeb24e504ca6808c015cc87a
    path('recipe/', recipe_page, name='recipes'),
    path('', home_page),
]

