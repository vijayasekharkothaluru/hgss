from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Hgs_Form
class Hgs_View(View):
    template_name = 'hgs.html'
    def get(self, request, *args, **kwargs):
        context = {}
        context["hform"] = Hgs_Form()
        return render(request,'hgs.html',context)
    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == "POST":
            hform = Hgs_Form(request.POST)
            if hform.is_valid():
                context["hform"] = hform
                return render(request, 'hgs.html', context)
            else:
                return render(request, 'hgs.html', {'hform': hform})




