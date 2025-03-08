from django.urls import path
from common.views import home_page, about_page

app_name = 'pages'

urlpatterns = [
    path('about/', about_page, name='about'),
    path('', home_page),
]

