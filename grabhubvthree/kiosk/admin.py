from django.contrib import admin

# Register your models here.
from .models import User
admin.site.register(User)

from .models import Food
admin.site.register(Food)

from .models import Customer
admin.site.register(Customer)

from .models import Order
admin.site.register(Order)