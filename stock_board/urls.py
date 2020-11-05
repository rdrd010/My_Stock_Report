from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'stock_board'

urlpatterns = [
    url(r'^$', views.Stock_list.as_view(), name='stock_board'),
    url(r'^insert/$', views.check_post, name='stock_board_insert'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)