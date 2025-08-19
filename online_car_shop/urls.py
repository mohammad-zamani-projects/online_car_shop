
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about-us'),
    path('car_list/', include('car_list.urls')),
    path('basket/', include('basket.urls')),
    path('shipping/', include('shipping.urls')),
    path('finance/', include('finance.urls')),
    path('package/', include('package.urls')),
    path('purchase/', include('purchase.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]



