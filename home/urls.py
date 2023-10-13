
from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ModelView.as_view()),
    path('login',views.loginInterfaceView.as_view(), name ='login'),
    path('singup',views.ModelsignupView.as_view(), name ='singup'),
    path('logout',views.logoutInterfaceView.as_view(), name='logout'),  #name is used in  as url in html 
    path('d/',views.ModelListView.as_view(), name='hell'),
    path('d/<int:pk>', views.ModelDetailView.as_view(), name='he'),
    path('d/<int:pk>/edit', views.ModelUpdateView.as_view(), name='note.edit'),
    path('e/', views.ModelCreateView.as_view(), name='note.new'),
    path('d/<int:pk>/del', views.ModelDeleteView.as_view(), name='note.delete'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

