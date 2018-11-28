from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'catmaze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.main, name='main'),
    url(r'^riddle/(?P<answer>.+)/$', views.riddle, name='riddle'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^riddle_new/$', views.riddle_new, name='riddle_new'),
]