from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import index, contact, about, privacy_policy, term_of_use

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('term_of_use/', term_of_use, name='term_of_use'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
