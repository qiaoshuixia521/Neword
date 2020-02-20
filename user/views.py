from django.shortcuts import render
from django.views import View
from user.form import RegForm, UserProfileForm
# Create your views here.
from user.models import UserProfile




class Register(View):

    def get(self,request):
        return render(request,"register.html")

    def post(self,request):
        name = request.POST.get("name")
        print(name)
        form_obj = RegForm( request.POST)
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            name = form_obj.cleaned_data["name"]
            password = form_obj.cleaned_data["password"]
            UserProfile(username=name,password=password).save()
            print(UserProfile.objects.all())

            print("form表单验证成功")
            return render(request, "login.html")
        else:
            error = form_obj.errors
            dir(error)
            print(error.items)
            # print(error.data)
            print(error["name"][0])
            return render(request,"register.html",{"error":error})

class Login(View):

    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        user = UserProfileForm(request.POST)
        if user.is_valid():
            print("用户验证通过")
            return render(request, "index.html")
        else:
            print(user.errors)
            return render(request,"login.html")

