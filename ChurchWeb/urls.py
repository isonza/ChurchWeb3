from django.contrib import admin
from church import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('usersignup', views.devotee_signup_view,name='usersignup'),
    path('userlogin', LoginView.as_view(template_name='userlogin.html'),name='userlogin'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('devotee-dashboard', views.devotee_dashboard_view,name='devotee-dashboard'),
    path('availableservices', views.availableservices_view,name='availableservices'),
    path('bookservice', views.bookservice_view,name='bookservice'),
    path('bookservicesunday', views.bookservicesunday_view,name='bookservicesunday'),
    path('choose-seat', views.chooseseat_view,name='choose-seat'),
    path('finalbook', views.finalbook_view,name='finalbook'),
    path('downloadticket', views.download_ticket_view,name='downloadticket'),
    path('bookedservice', views.bookedservice_view,name='bookedservice'),
    #path('delete-bookedservice', views.delete_bookedservice_view,name='delete-bookedservice'),
    path('member-download-ticket/<int:pk>', views.member_download_ticket_view,name='member-download-ticket'),
    path('bookbiblestudy', views.bookbiblestudy_view,name='bookbiblestudy'),
    path('trackcovid', views.trackcovid_view,name='trackcovid'),
    path('submitreport', views.submitreport_view,name='submitreport'),
    path('viewreport', views.viewreport_view,name='viewreport'),
    path('testimonial', views.testimonial_view,name='testimonial'),
    path('myprofile', views.myprofile_view,name='myprofile'),
    path('edit-myprofile', views.edit_myprofile_view,name='edit-myprofile'),
    path('donate', views.donate_view,name='donate'),
    path('contactus', views.contactus_view,name='contactus'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('viewbookedservice', views.viewbookedservice_view,name='viewbookedservice'),
    path('delete-adminbooking/<int:pk>', views.delete_adminbooking_view,name='delete-adminbooking'),
    #path('edit-adminbooking', views.edit_adminbooking_view,name='edit-adminbooking'),
    path('member', views.member_view,name='member'),
    url(r'^create$', views.create_member_view, name='create'),
    path('delete-member/<int:pk>', views.delete_member_view,name='delete-member'),
    path('viewtestimonial', views.viewtestimonial_view,name='viewtestimonial'),
    path('delete-testimonial/<int:pk>', views.deletetestimonial_view,name='delete-testimonial'),
    path('viewdonation', views.viewdonation_view,name='viewdonation'),
    path('delete-donation/<int:pk>', views.deletedonation_view,name='delete-donation'),
]

"""
from django.contrib import admin
from django.urls import path, include
from church import views
from django.contrib.auth.views import LogoutView,LoginView

from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('user/',include('user.urls')),
    #path('',views.home_view,name=''), #lumabas na si sign up page after icomment yung below
    path('',index.indexpage,name='indexpage'), #AYAW NYA! HAYS. KELANGAN ATA BLANK NA PAGE? ps: need lang pala naka indicate folder user or church/bja.html
    path('homebase',index.homebasepage,name='homebasepage'),
    path('memberbase',index.memberbasepage,name='memberbasepage'),
    path('adminbase',index.adminbasepage,name='adminbasepage'),

    path('aboutus',index.aboutuspage,name='aboutuspage'),
    path('contactus',index.contactuspage,name='contactuspage'),
    path('contactussuccess',index.contactussuccesspage,name='contactussuccesspage'),

    path('userlogin',index.userloginpage,name='userloginpage'),
    #path('userlogin', LoginView.as_view(template_name='user/userlogin.html'),name='userlogin'),
    #path('afterlogin', views.afterlogin_view,name='afterlogin'),
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
"""