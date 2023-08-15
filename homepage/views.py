from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'homepage/dashboard.html'


class DiaryView(TemplateView):
    template_name = 'homepage/Diary.html'


class PictureView(TemplateView):
    template_name = 'homepage/Picture.html'


class GuestbookView(TemplateView):
    template_name = 'homepage/Guestbook.html'