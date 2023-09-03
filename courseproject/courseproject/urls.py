from django.contrib import admin
from django.urls import path, include
from core.views import index, search
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('order.api.urls')),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('about.urls')),
    path('', include('bloq.urls')),
    path('', include('contact.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
