from django.contrib import admin
from tiffin.models import *

# Register your models here.
admin.site.register(tiffin_user)
admin.site.register(kitchen)

admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
admin.site.register(Menu_card)
