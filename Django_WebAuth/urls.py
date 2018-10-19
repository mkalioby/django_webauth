from django.conf.urls import include, url
from django.contrib import admin
import django_webauth
urlpatterns = [
    # Examples:
    # url(r'^$', 'django_webauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(django_webauth.urls)),

]
