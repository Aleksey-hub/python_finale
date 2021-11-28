from django.urls import path

from catalog.views import index

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:catalog_section_pk>/', index, name='section'),
]
