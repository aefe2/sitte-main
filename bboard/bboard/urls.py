from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.views.decorators.cache import never_cache
from django.views.static import serve

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('main.urls', namespace='')),
]

if settings.DEBUG:
   urlpatterns.append(path('static/<path:path>', never_cache(serve)))
