from django.shortcuts import render
from myfiles.models import Student, Ishxona
# Create your views here.

def home(malumot):
    return render(malumot,'index.html')

def students(malumot):
    talabalar = Student.objects.all()
    return render(malumot,'students.html', {"studentlar":talabalar})

def ishxona_sahifasi(malumot):
    ishchilar = Ishxona.objects.all()
    return render(malumot, "ishxona.html", {'ishchi':ishchilar})
