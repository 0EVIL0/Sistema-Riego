from django.contrib import admin
from django.urls import path, include, re_path

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),

#patc(r'courses/', include('course.urls')),
# path('',views.index,name='Home'),

path('',include('app.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)