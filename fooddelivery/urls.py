from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from onlfoods import views

urlpatterns = [
    #admin
    #=========================================================================================
    path('admin/', admin.site.urls),

    #User
    #==========================================================================================
    path('user/<str:pk>/', views.get_user),
    path('adit-user/<str:pk>/', views.edit_user),
    path('signup/', views.signup),

    # food
    # ==========================================================================================
    path('food/', views.get_foods),
    path('food/<str:pk>/', views.get_food),
    path('add-food/', views.add_food),
    path('food/<str:pk>/update/', views.update_food),
    path('food/<str:pk>/delete/', views.delete_food),

    # offers 
    path('offers/', views.offers),
    path('offer/<str:pk>/', views.offer),
    path('admin-dash/', views.adm_dashboard),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
