from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'homepage/dashboard.html'


class DiaryView(TemplateView):
    template_name = 'homepage/Diary.html'


class PictureView(TemplateView):
    template_name = 'homepage/Picture.html'


class GuestbookView(TemplateView):
    template_name = 'homepage/Guestbook.html'


class LoginView(TemplateView):
    template_name = 'accounts/login.html'


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'