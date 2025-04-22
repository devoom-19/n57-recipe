from django.urls import path
from common.views import *

app_name = 'pages'

urlpatterns = [
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('category/', category_page, name='category'),
    path('recipe/', recipe_page, name='recipes'),
    path('', home_page),
]

