from django.urls import path

from catalog.views import index, catalog_section

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('<int:catalog_section_pk>/', catalog_section, name='section'),
]
