from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Admin Panel Title
admin.site.site_header="UKALIGNERS Admin Login"
admin.site.site_title="UKALIGNERS Administration"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients', views.patients, name='patients'),
    path('patientaccepted', views.patientaccepted, name='patientaccepted'),
    path('patientreview', views.patientreview, name='patientreview'),
    path('patientdeclined', views.patientdeclined, name='patientdeclined'),
    path('patients', views.patients, name='patients'),
    path('dentists', views.dentists, name='dentists'),
    path('addnewpatient', views.addnewpatient, name='addnewpatient'),
    path('patientdetail/<int:id>/', views.patientdetail, name='patientdetail'),
    path('login', views.loginuser, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutuser, name='logout'),
    
    #cdeditor
    path('ckeditor',include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
