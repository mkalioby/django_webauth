from django.conf.urls import include, url
import views,api

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_webauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home,name = "home"),
    url(r'^login/', views.login,name = "login"),

    url(r'getChallenge',api.BeginMakeCredential,name="getChallenage")

]
