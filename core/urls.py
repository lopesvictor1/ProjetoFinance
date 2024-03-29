from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('userProfile.urls')),
    path('extract/', include('extract.urls')),
    path('planning/', include('planning.urls')),
    path('bills/', include('bills.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
