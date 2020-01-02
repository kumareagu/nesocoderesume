from django.shortcuts import render
from resume .models import*
# Create your views here.
def resume(request):
    return render (request,"resume/index.html")

def Resumes(request):
    per=Profile.objects.all()
    exp=Experience.objects.all()
    Edu=Education.objects.all()
    trin=Training.objects.all()
    my_dict={"per":per,"exp":exp,"Edu":Edu,'trin':trin}
    return render(request,"resume/empdetails.html",context=my_dict)
