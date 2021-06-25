from django.shortcuts import render,redirect,reverse
from . import models
from church.models import Devotee
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User


def devotee_signup_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')
        user = User()
        user.fullname=fullname
        user.email=email
        user.username=username
        user.set_password(password)
        #user.password=password
        user.save()
        devotee=models.Devotee()
        devotee.user=user
        devotee.fullname=fullname
        devotee.email=email
        devotee.address=address
        devotee.mobile=mobile
        devotee.profile_pic=profile_pic
        devotee.password=password
        devotee.save()


        my_devotee_group = Group.objects.get_or_create(name='DEVOTEE')
        my_devotee_group[0].user_set.add(user)
        return HttpResponseRedirect('/userlogin')
    return render(request,'devoteesignup.html')

def devotee_dashboard_view(request):
    return render(request,'devoteedashboard.html',context=None)


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'index.html')


def is_devotee(user):
    return user.groups.filter(name='DEVOTEE').exists()


def afterlogin_view(request):
    if is_devotee(request.user):      
        return redirect('/devotee-dashboard')
    else:
        return redirect('admin-dashboard')



def availableservices_view(request):
    return render(request,'availableservices.html')

def bookservice_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    covid = models.Covid.objects.all().filter(devotee=devotee).last()
    msg='x'
    if covid != None:
        if covid.status == 'ALLOWED':
            return render(request,'bookservice.html')
    return render(request,'trackcovid.html',{'msg':msg})
    


def bookservicesunday_view(request):
    if request.method=='POST':
        booking_date=request.POST['booking_date']

        import datetime
    
        b_date= datetime.datetime.strptime(booking_date, "%m-%d-%Y").strftime("%Y-%m-%d")
        seats=models.Seat.objects.get_or_create(date=b_date,service="servicesunday")
        seats=models.Seat.objects.get(date=b_date,service="servicesunday")

            
        response= render(request,'choose_seat.html',{'seats':seats})
        response.set_cookie('booking_date',booking_date)
        response.set_cookie('service',"servicesunday")
        return response
    return render(request,'ask_booking_date.html',context=None)


def chooseseat_view(request):
    booking_date=request.COOKIES['booking_date']
    import datetime
    
    b_date= datetime.datetime.strptime(booking_date, "%m-%d-%Y").strftime("%Y-%m-%d")
    seats=models.Seat.objects.get(date=b_date,service="servicesunday")
 
    return render(request,'choose_seat.html',{'seats':seats,})


def finalbook_view(request):
    booking_date=request.COOKIES['booking_date']
    service=request.COOKIES['service']
    import datetime

    booking_date= datetime.datetime.strptime(booking_date, "%m-%d-%Y").strftime("%Y-%m-%d")
    seats=models.Seat.objects.get_or_create(date=booking_date,service=service)
    seats=models.Seat.objects.get(date=booking_date,service=service)
    allNameVals=request.COOKIES['allNameVals']
    allNumberVals=request.COOKIES['allNumberVals']
    allSeatsVals=request.COOKIES['allSeatsVals']
    
    

    #make seat unavailable for other
    seat=allSeatsVals.split(',')
    for x in seat:
        if x=='A1':
            seats.A1=False
        elif x=='A2':
            seats.A2=False
        elif x=='A3':
            seats.A3=False
        elif x=='A4':
            seats.A4=False
        elif x=='A5':
            seats.A5=False
        elif x=='A6':
            seats.A6=False
        elif x=='A7':
            seats.A7=False
        elif x=='A8':
            seats.A8=False
        elif x=='A9':
            seats.A9=False
        elif x=='A10':
            seats.A10=False
        elif x=='A11':
            seats.A11=False
        elif x=='A12':
            seats.A12=False
        elif x=='B1':
            seats.B1=False
        elif x=='B2':
            seats.B2=False
        elif x=='B3':
            seats.B3=False
        elif x=='B4':
            seats.B4=False
        elif x=='B5':
            seats.B5=False
        elif x=='B6':
            seats.B6=False
        elif x=='B7':
            seats.B7=False
        elif x=='B8':
            seats.B8=False
        elif x=='B9':
            seats.B9=False
        elif x=='B10':
            seats.B10=False
        elif x=='B11':
            seats.B11=False
        elif x=='B12':
            seats.B12=False
        elif x=='C1':
            seats.C2=False
        elif x=='C3':
            seats.C3=False
        elif x=='C4':
            seats.C4=False
        elif x=='C5':
            seats.C6=False
        elif x=='C7':
            seats.C8=False
        elif x=='C9':
            seats.C9=False
        elif x=='C10':
            seats.C10=False
        elif x=='C11':
            seats.C11=False
        elif x=='C12':
            seats.C12=False
        elif x=='D1':
            seats.D1=False
        elif x=='D2':
            seats.D2=False
        elif x=='D3':
            seats.D3=False
        elif x=='D4':
            seats.D4=False
        elif x=='D5':
            seats.D5=False
        elif x=='D6':
            seats.D6=False
        elif x=='D7':
            seats.D7=False
        elif x=='D8':
            seats.D8=False
        elif x=='D9':
            seats.D9=False
        elif x=='D10':
            seats.D10=False
        elif x=='D11':
            seats.D11=False
        elif x=='D12':
            seats.D12=False
        elif x=='E1':
            seats.E1=False
        elif x=='E2':
            seats.E2=False
        elif x=='E3':
            seats.E3=False
        elif x=='E4':
            seats.E4=False
        elif x=='E5':
            seats.E5=False
        elif x=='E6':
            seats.E6=False
        elif x=='E7':
            seats.E7=False
        elif x=='E8':
            seats.E8=False
        elif x=='E9':
            seats.E9=False
        elif x=='E10':
            seats.E10=False
        elif x=='E11':
            seats.E11=False
        elif x=='E12':
            seats.E12=False
        elif x=='F1':
            seats.F1=False
        elif x=='F2':
            seats.F2=False
        elif x=='F3':
            seats.F3=False
        elif x=='F4':
            seats.F4=False
        elif x=='F5':
            seats.F5=False
        elif x=='F6':
            seats.F6=False
        elif x=='F7':
            seats.F7=False
        elif x=='F8':
            seats.F8=False
        elif x=='F9':
            seats.F9=False
        elif x=='F10':
            seats.F10=False
        elif x=='F11':
            seats.F11=False
        elif x=='F12':
            seats.F12=False
        elif x=='G1':
            seats.G1=False
        elif x=='G2':
            seats.G2=False
        elif x=='G3':
            seats.G3=False
        elif x=='G4':
            seats.G4=False
        elif x=='G5':
            seats.G5=False
        elif x=='G6':
            seats.G6=False
        elif x=='G7':
            seats.G7=False
        elif x=='G8':
            seats.G8=False
        elif x=='G9':
            seats.G9=False
        elif x=='G10':
            seats.G10=False
        elif x=='G11':
            seats.G11=False
        elif x=='G12':
            seats.G12=False
        elif x=='H1':
            seats.H1=False
        elif x=='H2':
            seats.H2=False
        elif x=='H3':
            seats.H3=False
        elif x=='H4':
            seats.H4=False
        elif x=='H5':
            seats.H5=False
        elif x=='H6':
            seats.H6=False
        elif x=='H7':
            seats.H7=False
        elif x=='H8':
            seats.H8=False
        elif x=='H9':
            seats.H9=False
        elif x=='H10':
            seats.H10=False
        elif x=='H11':
            seats.H11=False
        elif x=='H12':
            seats.H12=False
        elif x=='I1':
            seats.I1=False
        elif x=='I2':
            seats.I2=False
        elif x=='I3':
            seats.I3=False
        elif x=='I4':
            seats.I4=False
        elif x=='I5':
            seats.I5=False
        elif x=='I6':
            seats.I6=False
        elif x=='I7':
            seats.I7=False
        elif x=='I8':
            seats.I8=False
        elif x=='I9':
            seats.I9=False
        elif x=='I10':
            seats.I10=False
        elif x=='I11':
            seats.I11=False
        elif x=='I12':
            seats.I12=False
        elif x=='J1':
            seats.J1=False
        elif x=='J2':
            seats.J2=False
        elif x=='J3':
            seats.J3=False
        elif x=='J4':
            seats.J4=False
        elif x=='J5':
            seats.J5=False
        elif x=='J6':
            seats.J6=False
        elif x=='J7':
            seats.J7=False
        elif x=='J8':
            seats.J8=False
        elif x=='J9':
            seats.J9=False
        elif x=='J10':
            seats.J10=False
        elif x=='J11':
            seats.J11=False
        elif x=='J12':
            seats.J12=False

    seats.save()


    #create booking object
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    booking=models.Booking()
    booking.devotee=devotee
    booking.service=service
    
    booking.totalSeat=int(request.COOKIES['allNumberVals'])
    booking.seatNumber=allSeatsVals
    booking.date=seats.date
    booking.attendee=allNameVals
    booking.save()

    return render(request,'seat_booked.html')

import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


def download_ticket_view(request):
    import datetime
    booking_date=request.COOKIES['booking_date']
    service=request.COOKIES['service']
    b_date= datetime.datetime.strptime(booking_date, "%m-%d-%Y").strftime("%Y-%m-%d")
    seats=models.Seat.objects.get(date=b_date,service=service)

    mydict={
    'service':service,
    'devotee':models.Devotee.objects.get(user_id=request.user.id),
    'seats':seats,
    'allNameVals':request.COOKIES['allNameVals'],
    'allNumberVals':request.COOKIES['allNumberVals'],
    'allSeatsVals':request.COOKIES['allSeatsVals'],
    
    }
    return render_to_pdf('download_ticket.html',mydict)



def bookbiblestudy_view(request):
    if request.method=='POST':
        booking_date=request.POST['booking_date']

        import datetime
    
        b_date= datetime.datetime.strptime(booking_date, "%m-%d-%Y").strftime("%Y-%m-%d")
        seats=models.Seat.objects.get_or_create(date=b_date,service="biblestudy")
        seats=models.Seat.objects.get(date=b_date,service="biblestudy")

            
        response= render(request,'choose_seat.html',{'seats':seats})
        response.set_cookie('booking_date',booking_date)
        response.set_cookie('service',"biblestudy")
        return response
    return render(request,'ask_booking_date_bible.html',context=None)


def bookedservice_view(request):
    devotee= models.Devotee.objects.get(user_id=request.user.id)
    bookings= models.Booking.objects.all().filter(devotee=devotee.id)
    #print(bookings)
    return render(request,'bookedservice.html',{'bookings':bookings})
    

def member_download_ticket_view(request,pk):
    booking= models.Booking.objects.get(id=pk)
    mydict={
    'service':booking.service,
    'devotee':booking.devotee,
    'servicedate':booking.date,
    'allNameVals':booking.attendee,
    'allNumberVals':booking.totalSeat,
    'allSeatsVals':booking.seatNumber,
    
    }
    return render_to_pdf('download_ticket.html',mydict)


def trackcovid_view(request):
    return render(request,'trackcovid.html')

def submitreport_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    if request.method=='POST':
        covid = models.Covid()
        covid.devotee=devotee
        covid.COVID_positive_interaction=request.POST.get('INTERACTION')
        covid.symptoms=request.POST.get('SYMPTOMS')
        covid.travel_outside=request.POST.get('TRAVEL')
        covid.high_COVID_area=request.POST.get('AREA')
        if request.POST.get('INTERACTION')=='YES' or request.POST.get('SYMPTOMS')=='YES' or request.POST.get('TRAVEL')=='YES' or request.POST.get('AREA')=='YES' :
            covid.status="NOT-ALLOWED"
        else:
            covid.status="ALLOWED"
        covid.save()
        return redirect('viewreport')
    return render(request,'submitreport.html')

def viewreport_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    covid = models.Covid.objects.all().filter(devotee=devotee).last()
    msg="CONGRATULATIONS. YOU ARE ALLOWED TO ATTEND F2F SERVICES. PLEASE PROCEED TO 'BOOK SERVICE'."
    if covid != None:
        if covid.status == 'NOT-ALLOWED':
            msg="SORRY BUT YOU ARE NOT ALLOWED TO ATTEND F2F SERVICES BUT YOU CAN STILL JOIN THROUGH LIVE SERVICE ON FACEBOOK. PLEASE TRY AGAIN AFTER 14 DAYS. ALWAYS KEEP SAFE."
    return render(request,'viewreport.html',{'msg':msg})


def testimonial_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    if request.method=='POST':
        testimonial=models.PrayerTestimony()
        testimonial.devotee=devotee
        testimonial.message=request.POST.get('msg')
        testimonial.testimonial_or_prayer=request.POST.get('messagetype')
        testimonial.save()
        return render(request,'testimonial.html')
    return render(request,'testimonial.html')

def donate_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    if request.method=='POST':
        donation=models.Donation()
        donation.devotee=devotee
        donation.amount=request.POST.get('amount')
        donation.payment_method=request.POST.get('method')
        donation.gcash_method=request.POST.get('gcash')
        donation.bank_method=request.POST.get('bank')
        donation.save()
        return render(request,'donate.html')
    return render(request,'donate.html')

def myprofile_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    return render(request,'my_profile.html',{'devotee':devotee})

#may mali di nauupdate
def edit_myprofile_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    return render(request,'edit_myprofile.html',context=None)

#dipa naayos waitsssu
def edit_customer_profile_view(request):
    devotee=models.Devotee.objects.get(user_id=request.user.id)
    user=models.User.objects.get(id=devotee.user_id)
    if request.method=='POST':
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('edit-myprofile')
    return render(request,'edit_myprofile.html',context=mydict)


def admin_dashboard_view(request):
    return render(request,'admin_dashboard.html')

def viewbookedservice_view(request):
    bookings= models.Booking.objects.all()
    #print(bookings)
    return render(request,'admin_bookedservice.html',{'bookings':bookings})

def delete_adminbooking_view(request,pk):
    bookings=models.Booking.objects.get(id=pk)
    bookings.delete()
    return HttpResponseRedirect('/viewbookedservice')

def member_view(request):
    members=models.Devotee.objects.all()
    return render(request,'admin_member.html',{'members':members})

def create_member_view(request):
    member=models.Devotee.objects.create(
    fullname=request.POST['fullname'], 
    address=request.POST['address'],)
    return redirect('/')

def delete_member_view(request,pk):
    member=models.Devotee.objects.get(id=pk)
    user=User.objects.get(id=member.user_id)
    user.delete()
    member.delete()
    return HttpResponseRedirect('/member')

def viewtestimonial_view(request):
    testimonial=models.PrayerTestimony.objects.all()
    return render(request,'admin_testimonial.html',{'testimonial':testimonial})

def deletetestimonial_view(request,pk):
    testimonial=models.PrayerTestimony.objects.get(id=pk)
    testimonial.delete()
    return HttpResponseRedirect('/viewtestimonial')

def viewdonation_view(request):
    donation=models.Donation.objects.all()
    return render(request,'admin_donation.html',{'donation':donation})

def deletedonation_view(request,pk):
    donation=models.Donation.objects.get(id=pk)
    donation.delete()
    return HttpResponseRedirect('/viewdonation')










def aboutus_view(request):
    return render(request,'aboutus.html')

def contactus_view(request):

    if request.method == 'POST':
            
            email = request.POST.get('email')
            name=request.POST.get('name')
            message = request.POST.get('message')
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            #return render(request, 'church/contactussuccess.html')
    return render(request, 'contactus.html')