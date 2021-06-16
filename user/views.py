from django.shortcuts import render,redirect,reverse
from . import models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from user import models as UMODEL


def devotee_signup_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        profile_pic = request.FILES.get('profile_pic')
        user = User()
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.set_password(password)
        #user.password=password
        user.save()
        devotee=models.Devotee()
        devotee.user=user
        devotee.address=address
        devotee.mobile=mobile
        devotee.profile_pic=profile_pic
        devotee.save()


        my_devotee_group = Group.objects.get_or_create(name='DEVOTEE')
        my_devotee_group[0].user_set.add(user)
        return HttpResponseRedirect('/userlogin')
    return render(request,'user/devoteesignup.html')

def devotee_dashboard_view(request):
    return render(request,'user/devoteedashboard.html',context=None)
