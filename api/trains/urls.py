from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'public', views.index),
    url(r'private/(?P<train_line_id>\d+)', views.detail, name='detail')
    # path('', TemplateView.as_view(template_name='trains.html')),
    # # path('', views.index, name='index'),
    # path('<int:train_line_id>', views.detail, name='detail')
]
