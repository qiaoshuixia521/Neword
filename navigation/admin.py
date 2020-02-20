from django.contrib import admin
from navigation import models

class CardAdmin(admin.ModelAdmin):
    list_display = ("name","describe")
    search_fields = ("name",)


# Register your models here.
admin.site.register(models.Card,CardAdmin)

