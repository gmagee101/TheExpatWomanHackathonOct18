from django.contrib import admin

# Register your models here.

from .models import Highlight
from .models import Reason

admin.site.register(Highlight)
admin.site.register(Reason)
