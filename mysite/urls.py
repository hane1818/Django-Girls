from django.conf.urls import include, url
from django.contrib import admin
from trips.views import home, post_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^post/(?P<id>\d+)/$', post_detail, name='post_detail'),
]
