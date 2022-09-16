# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'connectToQuickbooks/', views.connectToQuickbooks, name='connectToQuickbooks'),
    path(r'signInWithIntuit/', views.signInWithIntuit, name='signInWithIntuit'),
    path(r'getAppNow/', views.getAppNow, name='getAppNow'),
    path(r'authCodeHandler/', views.authCodeHandler, name='authCodeHandler'),
    path(r'disconnect/', views.disconnect, name='disconnect'),
    path(r'apiCall/', views.apiCall, name='apiCall'),
    path(r'connected/', views.connected, name='connected'),
    path(r'refreshTokenCall/', views.refreshTokenCall, name='refreshTokenCall')
]
