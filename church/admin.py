from django.contrib import admin
from church.models import Booking, Covid, PrayerTestimony, Devotee, Seat, Donation
# Register your models here.

admin.site.register(Booking)
admin.site.register(Covid)
admin.site.register(PrayerTestimony)
admin.site.register(Devotee)
admin.site.register(Seat)
admin.site.register(Donation)