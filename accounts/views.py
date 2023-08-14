from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
    # 회원가입 성공 후 리디렉션할 URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # 유저 로그인
        return super().form_valid(form)


class DashboardView(generic.TemplateView):
    template_name = 'accounts/dashboard.html'