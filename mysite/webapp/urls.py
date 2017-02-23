from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.login, name = 'login'),
			   url(r'^register',views.register, name = 'register'),
			   url(r'^regSuccess',views.regSuccess, name = 'regSuccess'),
			   url(r'^loginCheck',views.loginCheck, name = 'loginCheck')
			   ]
