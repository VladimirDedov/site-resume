from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from .models import User
from .forms import SendMailForm


class ViewIndex(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'resume/index.html'
    context_object_name = 'user'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        form = SendMailForm()
        context['form']=form
        return context

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return redirect('index')

# def ViewIndex(request):
#     return render(request, 'resume/base.html')