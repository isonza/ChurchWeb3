from django.db import models
from django.contrib.auth.models import User
from user import models as UMODEL

class Booking(models.Model):
    devotee=models.ForeignKey(UMODEL.Devotee,on_delete=models.CASCADE,null=True)
    seatNumber=models.CharField(max_length=500)
    service = models.CharField(max_length=200)
    totalSeat=models.CharField(max_length=3) 
    date=models.DateField()
    attendee=models.CharField(max_length=500,null=True)
    bookingDate=models.DateField(auto_now=True)
    def __str__(self):
        return self.seatNumber

class Covid(models.Model):
    devotee=models.ForeignKey(UMODEL.Devotee,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default="NOT-ALLOWED")
    COVID_INTERACTION=models.CharField(max_length=20)
    HAVE_FEVER=models.CharField(max_length=20)
    OUTSIDE_TRAVEL=models.CharField(max_length=20)
    AREA=models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Testimonial(models.Model):
    devotee=models.ForeignKey(UMODEL.Devotee,on_delete=models.CASCADE,null=True)
    testimonial_or_prayer=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.testimonial_or_prayer
