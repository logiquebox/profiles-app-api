from django.contrib import admin
from profiles_api.models import UserProfile
from profiles_api.models import ProfileFeedItem

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
