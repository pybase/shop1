from django.urls import path

from . import views

app_name = 'eshop'

urlpatterns = [

   path('',views.Allprdtcat,name='Allprdtcat'),
   path('<slug:c_slug>/',views.Allprdtcat,name='product_by_catogery'),
   path('<slug:c_slug>/<slug:product_slug>/',views.PrdtDetails,name='PrdtDetails')
]
