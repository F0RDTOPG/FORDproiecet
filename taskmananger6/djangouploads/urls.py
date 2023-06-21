from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/<int:movie_id>", views.movie)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)