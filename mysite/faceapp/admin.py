from django.contrib import admin
from faceapp.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=(
     'face_id',
     'name',
     'phone',
     'job',
     'email',
     'address',
    )

admin.site.register(UserProfile, UserProfileAdmin)
