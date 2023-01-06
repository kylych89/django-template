from django.urls import path
from .views import (baseView,
                    regionsView,
                    areasesView,
                    loginView,
                    registerView,
                    createRegionsView,
                    updateRegionsView,
                    deleteRegionsView,
                    updateAreasView,
                    deleteAreasView,
                    createAreasView)

app_name = 'main'

urlpatterns = [
    path('base/', baseView, name='base'),

    # regions

    path('regions/<int:pk>/', regionsView, name='regions'),
    path('create_region/', createRegionsView, name='create_region'),
    path('update_region/<int:pk>/', updateRegionsView, name='update_region'),
    path('delete_region/<int:pk>/', deleteRegionsView, name='delete_region'),

    # areases

    path('areases/<int:pk>/', areasesView, name='areas'),
    path('create_areas/', createAreasView, name='create_areas'),
    path('update_area/<int:pk>/', updateAreasView, name='update_areas'),
    path('delete_area/<int:pk>/', deleteAreasView, name='delete_areas'),

    # authenticates

    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
]
