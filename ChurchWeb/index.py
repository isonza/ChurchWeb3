"""from django.http import HttpResponse
from django.shortcuts import render

#navbar and attention
def indexpage(request):
		return render(request,'church/index.html')

def aboutuspage(request):
		return render(request,'church/aboutus.html')

def contactuspage(request):
		return render(request,'church/contactus.html')

def contactussuccesspage(request):
		return render(request,'church/contactussuccess.html')

def userloginpage(request):
		return render(request,'user/userlogin.html')

def devoteesignuppage(request):
		return render(request,'user/devoteesignup.html')

def devoteedashboardpage(request):
		return render(request,'user/devoteedashboard.html')

def adminloginpage(request):
		return render(request,'church/adminlogin.html')

def admin_dashboardpage(request):
		return render(request,'church/admin_dashboard.html')


#navbar for home, member and admin pages
def homebasepage(request):
		return render(request,'church/homebase.html')

def memberbasepage(request):
		return render(request,'user/memberbase.html')

def adminbasepage(request):
		return render(request,'church/adminbase.html')


#pages for other stuffs in member dashboard
#covid/contact tracing

def trackcovidpage(request):
		return render(request,'user/trackcovid.html')

def submitreportpage(request):
		return render(request,'user/submitreport.html')

def viewreportpage(request):
		return render(request,'user/viewreport.html')


#booking
def availableservicespage(request):
		return render(request,'user/availableservices.html')

def bookedservicepage(request):
		return render(request,'user/bookedservice.html')

def download_ticketpage(request):
		return render(request,'user/download_ticket.html')

def bookservicepage(request):
		return render(request,'user/bookservice.html')

def ask_booking_datepage(request):
		return render(request,'user/ask_booking_date.html')

def ask_booking_date_biblepage(request):
		return render(request,'user/ask_booking_date_bible.html')

def choose_seatpage(request):
		return render(request,'user/choose_seat.html')

def seat_bookedpage(request):
		return render(request,'user/seat_booked.html')


#testimony/prayer request

def testimonialpage(request):
		return render(request,'user/testimonial.html')

def requestsubmittedpage(request):
		return render(request,'user/requestsubmitted.html')


#myprofile page

def myprofilepage(request):
		return render(request,'user/myprofile.html')

#logout page
def logoutpage(request):
		return render(request,'church/logout.html')


#pages for other stuffs in admin dashboard
#adminmember
def admin_memberpage(request):
		return render(request,'church/admin_member.html')

#adminmember
def admin_testimonialpage(request):
		return render(request,'church/admin_testimonial.html')

"""