from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('about-us/', TemplateView.as_view(template_name="about_us.html"), name='about-us'),
    path('join-us/', TemplateView.as_view(template_name="join_us.html"), name='join-us'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('price-list/', TemplateView.as_view(template_name="price_list.html"), name='price-list'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
