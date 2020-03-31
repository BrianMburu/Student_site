from django.contrib import admin
from .models import Search,Member,UserProfileInfo

# Register your models here.
admin.site.register(Search)
admin.site.register(Member)
admin.site.register(UserProfileInfo)