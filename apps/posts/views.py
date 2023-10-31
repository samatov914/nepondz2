from django.shortcuts import render

# Create your views here.
from apps.posts.models import Posts
from apps.telegram.models import Contacts
from apps.telegram.views import get_text

def index(request):
    index = Posts.objects.all().order_by('?')[:3]
    name, email, message, phone = "", "", "", ""  # Задаем значения по умолчанию
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        test = Contacts.objects.create(name=name, email=email, message=message, phone=phone)
        get_text(f""" Оставлен отзыв 
        Имя пользователя: {test.name}
        Адрес(email): {test.email}
        номер телефона: {test.phone}
        Текст: {test.message}
        """)
    return render(request, 'index_2.html', locals())
