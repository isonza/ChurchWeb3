from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.contrib.auth.models import User


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'church/index.html')


def is_devotee(user):
    return user.groups.filter(name='DEVOTEE').exists()

def afterlogin_view(request):
    if is_devotee(request.user):      
        return redirect('user/devotee-dashboard')
    else:
        return redirect('admin-dashboard')

def contactus_view(request):

    if request.method == 'POST':
            
            email = request.POST.get('email')
            name=request.POST.get('name')
            message = request.POST.get('message')
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'church/contactussuccess.html')
    return render(request, 'church/contactus.html')