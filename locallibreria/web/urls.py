from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('novedades/',views.novedades,name='novedades'),
    path('dulces/',views.dulces,name='dulces'),
    path('saladas/',views.saladas,name='saladas'),
    path('pret/',views.pret,name='pret'),
    path('pie/',views.pie,name='pie'),
    path('capu/',views.capu,name='capu'),
    path('bebidas/',views.bebidas,name='bebidas'),
    path('receta/<int:pk>', views.RecetaDetailView.as_view(), name='RECETA-'),
]

urlpatterns += [
    path('receta/create/',views.RecetaCreate.as_view(), name='receta_create'),
    path('receta/<int:pk>/update/',views.RecetaUpdate.as_view(), name='receta_update'),
    path('receta/<int:pk>/delete/',views.RecetaDelete.as_view(), name='receta_delete'),

]