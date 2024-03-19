from django.shortcuts import render
from django.views.generic import View
from core.tasks import send_email_task


# Create your views here.


class IndexView(View):
    template_name = "core/home_page.html"

    def get(self, request):
        # if self.request.user.is_authenticated:
        user_email = "abdallah@gmail.com"
        send_email_task.delay(user_email, "Welcome to our site")

        return render(request, self.template_name)

