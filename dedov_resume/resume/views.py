from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import User
from .forms import SendMailForm


class ViewIndex(ListView):
    """Класс представления главной страницы"""
    model = User
    queryset = User.objects.all()
    template_name = 'resume/index.html'
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        """Добавление формы в context"""
        context = super().get_context_data(*args, **kwargs)
        form = SendMailForm()
        context['form'] = form
        return context


def send_message(content):
    '''Отправка письма через google'''
    send_mail(
        'Письмо с сайта резюме',
        content,
        'vldedov53@gmail.com',
        ['vldedov@bk.ru'],
        fail_silently=False
    )


def send_form(request):
    '''представление формы отправки и валидации'''
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            content = ('\n').join([form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['content']])
            send_message(content)
            return render(request, 'resume/redirect.html')
    return render(request, 'resume/captcha_error.html')
