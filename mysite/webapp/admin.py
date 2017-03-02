from django.contrib import admin

from webapp.models import *

admin.site.register(user)
admin.site.register(restaurant)
admin.site.register(order)
admin.site.register(menu)
admin.site.register(cart)


# Register your models here.
