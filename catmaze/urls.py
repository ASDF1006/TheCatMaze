from django.conf.urls.static import static
from django.conf.urls import include, url
# from django.conf.urls import handler404
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.admin import sites

urlpatterns = [
    # Examples:
    # url(r'^$', 'catmaze.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'accounts/login/$', login, name='login'),
    url(r'accounts/logout/$', logout, name='logout', kwargs={'next_page':'/'}),
]

#404 url
# handler404 = 'blog.views.page_not_found'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)