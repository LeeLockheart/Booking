from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addadvisor/',views.addadvisorPage,name="addadvisor"),
    path('booking/',views.bookingPage,name="booking"),
    # path('logout/',views.logoutUser,name="logout"),
    path('mainadmin/', views.mainadminPage, name="mainadmin"),
    path('register/', views.registerPage,name="register"),
    path('userdashboard/', views.userdashboardPage,name="userdashboard"),
    path('listofadvisors/', views.displayPage,name="list"),
    path('booking_info/', views.bookinginfoPage, name="book"),
    path('profilesetting/',views.profilePage,name='profilesetting'),
    path('',views.addadvisor,name="/"),
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)
