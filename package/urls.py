from django.urls import path
from django.views.generic import TemplateView

from package.views import PricingView

urlpatterns = [
    # path('show/', TemplateView.as_view(template_name='package/pricing.html'), name='pricing-show')
    path('show/', PricingView.as_view())
]

