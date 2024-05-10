from django.shortcuts import render
import datetime
from django.utils.timezone import make_aware
from polls.models import Phone

def index(request):
    phones = Phone.objects.all()
    date = datetime.datetime(2025, 1, 1)
    phones_since_2025 = Phone.objects.filter(created_at__lte=make_aware(date))
    context = {'Phones': phones, 'phones_since_2025': phones_since_2025}
    return render(request, 'index.html', context)

