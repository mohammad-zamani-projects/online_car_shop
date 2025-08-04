
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about-us'),
    path('car_list/', include('car_list.urls')),
    path('basket/', include('basket.urls')),
    path('shipping/', include('shipping.urls')),
    path('finance/', include('finance.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
