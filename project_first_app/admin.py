from django.contrib import admin
# Register your models here.
from .models import car_owner, ownership, car, drivers_license, User
admin.site.register(car_owner)
admin.site.register(ownership)
admin.site.register(car)
admin.site.register(drivers_license)
admin.site.register(User)