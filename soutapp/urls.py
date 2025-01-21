from django.urls import path
from . import crud

urlpatterns = [
    # Superviser CRUD URLs
    path('supervisers/', crud.list_supervisers, name='list_supervisers'),
    path('supervisers/create/', crud.create_superviser, name='create_superviser'),
    path('supervisers/update/<int:id>/', crud.update_superviser, name='update_superviser'),
    path('supervisers/delete/<int:id>/', crud.delete_superviser, name='delete_superviser'),

    # Apprecier CRUD URLs
    path('apprecies/', crud.list_apprecies, name='list_apprecies'),
    path('apprecies/create/', crud.create_apprecier, name='create_apprecier'),
    path('apprecies/update/<int:id>/', crud.update_apprecier, name='update_apprecier'),
    path('apprecies/delete/<int:id>/', crud.delete_apprecier, name='delete_apprecier'),
]
