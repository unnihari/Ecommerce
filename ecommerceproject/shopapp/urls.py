from . import views
from django.urls import path

app_name = 'shopapp'

urlpatterns = [

    path('', views.AllPodcast, name='AllPodcast'),
    path('<slug:c_slug>/', views.AllPodcast, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.ProDetails, name='product_details')
]
