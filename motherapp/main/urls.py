from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import SearchResultView


app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    #path('customer/', views.customer_page, name='customer'),
    path('leadparty/', views.lead_party, name='leadparty'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('register/', views.register_page, name='register'),
    path('<identity>/', views.customer_page, name='detail_view'),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)