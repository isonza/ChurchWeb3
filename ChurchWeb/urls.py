"""ChurchWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import index

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',index.indexpage,name='indexpage'), #AYAW NYA! HAYS. KELANGAN ATA BLANK NA PAGE?
    path('homebase',index.homebasepage,name='homebasepage'),
    path('memberbase',index.memberbasepage,name='memberbasepage'),
    path('adminbase',index.adminbasepage,name='adminbasepage'),

    path('index',index.indexpage,name='indexpage'),
    path('aboutus',index.aboutuspage,name='aboutuspage'),
    path('contactus',index.contactuspage,name='contactuspage'),
    path('contactussuccess',index.contactussuccesspage,name='contactussuccesspage'),
    path('userlogin',index.userloginpage,name='userloginpage'),
    path('devoteesignup',index.devoteesignuppage,name='devoteesignuppage'),
    path('devoteedashboard',index.devoteedashboardpage,name='devoteedashboardpage'),
    path('adminlogin',index.adminloginpage,name='adminloginpage'),
    path('admin_dashboard',index.admin_dashboardpage,name='admin_dashboardpage'),

    path('trackcovid',index.trackcovidpage,name='trackcovidpage'),
    path('submitreport',index.submitreportpage,name='submitreportpage'),
    path('viewreport',index.viewreportpage,name='viewreportpage'),

    path('availableservice',index.availableservicespage,name='availableservicespage'),
    path('bookedservice',index.bookedservicepage,name='bookedservicepage'),
    path('download_ticket',index.download_ticketpage,name='download_ticketpage'),
    path('bookservice',index.bookservicepage,name='bookservicepage'),
    path('ask_booking_date',index.ask_booking_datepage,name='ask_booking_datepage'),
    path('ask_booking_date_bible',index.ask_booking_date_biblepage,name='ask_booking_date_biblepage'),
    path('choose_seat',index.choose_seatpage,name='choose_seatpage'),
    path('seat_booked',index.seat_bookedpage,name='seat_bookedpage'),

    path('testimonial',index.testimonialpage,name='testimonialpage'),
    path('requestsubmitted',index.requestsubmittedpage,name='requestsubmittedpage'),
    path('myprofile',index.myprofilepage,name='myprofilepage'),
    path('logout',index.logoutpage,name='logoutpage'),

    path('admin_member',index.admin_memberpage,name='admin_memberpage'),
    path('admin_testimonial',index.admin_testimonialpage,name='admin_testimonialpage'),
]



#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
