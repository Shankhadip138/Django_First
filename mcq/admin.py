from django.contrib import admin
from mcq.models import Question,Choice
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
