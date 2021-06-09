from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.create, name="create"),
    path('Upload_form/<int:id>', views.update_book, name='update_book'),
    path('Update/<int:id>', views.updatebook, name='updatebook'),
    path('Delete/<int:id>', views.delete_book, name='delete_book'),

]
