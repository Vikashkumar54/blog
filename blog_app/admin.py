from django.contrib import admin

from .models import signform
from .models import add
from .models import contactu
from .models import proimage
from .models import leavecomment
from .models import feedback


# Register your models here.

admin.site.register(signform)
admin.site.register(add)
admin.site.register(contactu)
admin.site.register(proimage)
admin.site.register(leavecomment)
admin.site.register(feedback)


