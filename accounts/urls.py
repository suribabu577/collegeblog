from django.conf.urls import url
from django.conf import settings
from .import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^management/$',views.management,name='management'),
    url(r'^cse/$',views.cse,name='cse'),
    url(r'^ece/$',views.ece,name='ece'),
    url(r'^eee/$',views.eee,name='eee'),
    url(r'^it/$',views.it,name='it'),
    url(r'^mech/$',views.mech,name='mech'),
    url(r'^civil/$',views.civil,name='civil'),
    url(r'^hod/$',views.hod,name='hod'),
    url(r'^la/$',views.la,name='la'),
    url(r'^af/$',views.civil,name='af'),
    url(r'^admin/$',views.admin_login,name='admin'),
    url(r'^associats/$',views.associats,name='associats'),
    url(r'^students/$',views.students,name='students'),
    url(r'^addstaff/$',views.add_staff,name='add_staff'),
    url(r'^addstudent/$',views.add_student,name='add_student'),
    url(r'^upload/$',views.post,name='upload'),
    url(r'^newsfeed/$',views.news_feed,name='newsfeed'),
    url(r'^studentnf/$',views.snf,name='snf'),
    url(r'^staffnf/$',views.ssnf,name='ssnf'),
    url(r'^staffpost/$',views.staff_post,name='spost'),
    url(r'^logout/$',views.logout_request,name='logout'),
    #url(r'^user/', include('user_register_login.urls')),
    #url(r'^accounts/login/', include('user_register_login.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

