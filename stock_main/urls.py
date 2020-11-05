from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'stock_main'

urlpatterns = [
    url(r'^$', views.Stock_main.as_view(), name='stock_main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)