from django.shortcuts import render,redirect
from Account.models import User
from .validation import *

# Create your views here.
def Signup(request):

    if request.method == "POST":
        
        username = request.POST['username']
        pw = request.POST['pw']
        pw2 = request.POST['pw2']
        email = request.POST['email']
        print(username,email)

        res_data={}

        if pw!=pw2:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
            return render(request,"Account/Signup.html",res_data)
        if username == "" or email == "" or pw == "" or pw2 == "":
            res_data['error'] = "입력되지 않은 값이 있습니다."
            return render(request,"Account/Signup.html",res_data)
        if "true_pw" != validate_password(pw):
            res_data['error'] = "비밀번호는 4자리이상10자리이하."
            return render(request,"Account/Signup.html",res_data)
        if "false_email" == validate_email(email):
            res_data['error'] = "이메일이 올바르지 않습니다."
            return render(request,"Account/Signup.html",res_data)

        member = User

        if member.objects.filter(email=email).exists():
            res_data['error'] = "이미 가입된 이메일[ID]입니다"
            return render(request,"Account/Signup.html",res_data)
        if member.objects.filter(username=username).exists():
            res_data['error'] = "이미 있는 닉네임입니다"
            return render(request,"Account/Signup.html",res_data)
        else:
            member(username = username, email = email, password = pw).save()
            return redirect('/')

    else: 
        return render(request,'Account/Signup.html')