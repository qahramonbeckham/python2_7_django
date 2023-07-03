from django.contrib import admin
from myfiles.models import Kurs,Student,Ishxona
# Register your models here.

class AdminKurs(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Kurs,AdminKurs)

class AdminStudent(admin.ModelAdmin):
    list_display = ['id','ism','familiya','yoshi','manzil','yonalish','date']

admin.site.register(Student,AdminStudent)


class AdminIshxona(admin.ModelAdmin):
    list_display = ['ism','familiya','yosh','lavozim','ish_staji','sana']

admin.site.register(Ishxona,AdminIshxona)