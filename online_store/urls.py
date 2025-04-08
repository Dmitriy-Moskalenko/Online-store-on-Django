from django.contrib import admin
from django.urls import path, include

from online_store import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cart.urls')),
    path('', include('comments.urls')),
    path('', include('homepage.urls')),
    path('', include('products.urls')),
    path('', include('user_profile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)