from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Cart)
admin.site.register(models.Item)
admin.site.register(models.Order)