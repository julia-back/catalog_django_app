from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import login
import os
from dotenv import load_dotenv


load_dotenv()

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    @staticmethod
    def send_welcome_email(user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email, ]
        send_mail(subject, message, recipient_list=recipient_list, from_email=os.getenv("EMAIL_HOST_USER"))
