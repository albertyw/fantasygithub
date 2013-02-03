from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fantasygithub.public.home', name='home'),
    url(r'^login$', 'fantasygithub.public.login', name='login'), 
    url(r'^about$', 'fantasygithub.public.about', name='about'),
    url(r'^manage$', 'fantasygithub.view.manage', name='manage'),
    url(r'^play$', 'fantasygithub.view.play', name='play'),
    # url(r'^fantasygithub/', include('fantasygithub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
