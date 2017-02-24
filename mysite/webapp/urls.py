from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.login, name = 'login'),
			   url(r'^registerUser',views.registerUser, name = 'registerUser'),
			   url(r'^registerRest',views.registerRest, name = 'registerRest'),
			   url(r'^regSuccessUser',views.regSuccessUser, name = 'regSuccessUser'),
			   url(r'^regSuccessRest',views.regSuccessRest, name = 'regSuccessRest'), 
			   url(r'^loginCheckUser',views.loginCheckUser, name = 'loginCheckUser'),
			   url(r'^loginCheckRest',views.loginCheckRest, name = 'loginCheckRest'),
			   url(r'^uWelcome',views.uWelcome,name='uWelcome'),
			   url(r'^rWelcome',views.rWelcome,name='rWelcome')
			   ]
  