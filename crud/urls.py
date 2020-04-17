from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('laptops', views.display_laptop, name='laptops'),
    path('desktops', views.display_desktop, name='desktops'),
    path('mobiles', views.display_mobile, name='mobiles'),

    path('add_laptop', views.add_laptop, name='add_laptop'),
    path('add_desktop', views.add_desktop, name='add_desktop'),
    path('add_mobile', views.add_mobile, name='add_mobile'),

    path('del_laptop/<int:pk>', views.del_laptop, name='del_laptop'),
    path('del_desktop/<int:pk>', views.del_desktop, name='del_desktop'),
    path('del_mobile/<int:pk>', views.del_mobile, name='del_mobile'),

    path('edit_laptop/<int:pk>', views.edit_laptop, name='edit_laptop'),
    path('edit_desktop/<int:pk>', views.edit_desktop, name='edit_desktop'),
    path('edit_mobile/<int:pk>', views.edit_mobile, name='edit_mobile'),
]
