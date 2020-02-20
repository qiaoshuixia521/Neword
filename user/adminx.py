import xadmin

from .models import UserProfile


class UserProfileAdmin(object):
    list_display = ["username","password"]
    search_fields = ["username"]
    list_filter = ["username"]

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
