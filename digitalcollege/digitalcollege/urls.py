"""digitalcollege URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls.static import static
from django.contrib import admin
from digital import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view),
	 url(r'^password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
	 url(r'^password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
	 url(r'^password_reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
	 url(r'^password_reset-complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    url(r'^logout/', views.logout_view),
    url(r'^Create-my-file/', views.create_view),
    url(r'^get-my-results/', views.results_view),
    url(r'^get-my-saved-documents/', views.document_view),
    url(r'^attendence-chart/', views.attendence_view),
    url(r'^latest-osmania-notes/', views.ounotes_view),
	url(r'^search/$',views.search_view),
	url(r'^previous-papers/$',views.previouspapers_view),
	url(r'^previous-papers-search/$',views.previous_paper_search_view),
	url(r'^CSE-Facuilty/$', views.cse_view),
	url(r'^EEE-Facuilty/$', views.eee_view),
	url(r'^ECE-Facuilty/$', views.ece_view),
	url(r'^Time-Table-Chart/$', views.timetable_view),
	url(r'^Syllabus-Chart/$', views.syllabus_view),
	url(r'^College-library/$', views.library_view),
	url(r'^My-profile/$', views.profile_view),
	url(r'^My-updates-page/$', views.update_view),
	url(r'^Raise-your-query/$', views.query_view),
	url(r'^Share-mail/$', views.mail_send_view),
    url(r'^College-events-images/$', views.gallary_view),
    url(r'^Search-college-events-images/$', views.gallary_search_view),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<gallary>[-\w]+)/$', views.get_selected_gallary_view,name='gallary'),
    url(r'^(?P<previous>[-\w]+)/$',views.get_selected_paper_view,name='image'),
	url(r'^accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
