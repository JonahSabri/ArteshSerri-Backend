from datetime import datetime, timedelta
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from extensions.spiliter import spiliter

from extensions.utils import format_text_color, generate_otp
from . import models

import datetime

class SendOTPToPhoneView(View):
    def get(self, request, *args, **kwargs):
        raise Http404()

    def post(self, request, *args, **kwargs):
        phone = request.POST.get("phone")
        otp = generate_otp()
        obj, created = models.OTPCode.objects.update_or_create(
            phone=phone,
            defaults={"otp_code": otp, "expire_at": datetime.now() + timedelta(seconds=150)},
        )
        print(format_text_color(f"OTP Code Requested at {datetime.now()} >>>>>>>>> {otp}", bg_color="red"))
        return JsonResponse({"message": "Code Has Been Sent"}, status=200)


class VerifyOTPFromPhoneView(View):
    def get(self, request, *args, **kwargs):
        raise Http404()

    def post(self, request, *args, **kwargs):
        phone = request.POST.get("phone")
        otp_code = request.POST.get("otp_code")
        if not models.OTPCode.objects.filter(phone=phone):
            return JsonResponse({"message": "Not Any OTP Code for this Phone"}, status=404)
        user_otp_obj = models.OTPCode.objects.get(phone=phone)
        if user_otp_obj.otp_code == otp_code:
            if user_otp_obj.expire_at < datetime.now():
                return JsonResponse({"message": "OTP Code has Expired"}, status=408)
            return JsonResponse({"message": "OTP is OK"}, status=200)
        return JsonResponse({"message": "OTP is Wrong"}, status=400)
        



class LoginView(View):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("/")

    def post(self, request, *args, **kwargs):

        Phone = request.POST.get("phone")
        password = request.POST.get("password")
        
        user = authenticate(request, phone=Phone, password=password)
        
        if user is not None:

            login(request, user)
            user = get_object_or_404(models.User, pk=request.user.pk)
            return redirect("/")

        return {"sttaus": False}


class SignupView(FormView):

    def post(self, request, *args, **kwargs):

        phone = request.POST.get("phone")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        

        user:models.User = models.User.objects.create_user(phone=phone, passwd= password,password=password, firstname=firstname, lastname=lastname, email=email)
        login(request, user)
        return {"status": True}

