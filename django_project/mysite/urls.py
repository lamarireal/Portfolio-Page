"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    prefix_default_language=False,
)

import os

# In development Django serves media files when DEBUG=True. For simple
# production setups where you cannot configure a separate media server,
# set DJANGO_SERVE_MEDIA=1 to let Django serve media (not recommended
# for high-load public sites).
if settings.DEBUG or os.environ.get('DJANGO_SERVE_MEDIA') == '1':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
