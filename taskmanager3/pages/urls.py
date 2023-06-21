
from django.urls import path
from . import views

app_name = 'articles' # 2 apps
urlpatterns=[
  path('',views.index, name='index'),
  path('<int:article_id>/',views.number, name='number' )
]