from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Avatar

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fields = ('puntos', 'naves')

    



# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Avatar)
admin.site.register(Profile)

