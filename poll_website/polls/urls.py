from django.urls import path, include
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', include([
        path('', views.detail, name='detail'),
        path('results/', views.results, name='results'),
        path('vote/', views.vote, name='vote'),
    ])),
]
