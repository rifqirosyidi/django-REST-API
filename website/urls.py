from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stocks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', views.StockList.as_view(), name='stock')
]
