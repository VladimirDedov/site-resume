from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User
from .forms import SendMailForm


class ViewIndex(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'resume/index.html'
    context_object_name = 'user'
    print(f'{context_object_name } + 123')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        form = SendMailForm()
        context['form']=form
        return context


# def ViewIndex(request):
#     return render(request, 'resume/base.html')