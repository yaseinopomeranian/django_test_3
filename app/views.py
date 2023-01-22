from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")

