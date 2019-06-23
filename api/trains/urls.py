from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='trains.html')),
    # path('', views.index, name='index'),
    path('<int:train_line_id>', views.detail, name='detail')
]
