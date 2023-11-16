from django.shortcuts import render
from .models import user
# Create your views here.
def contact(request):
    # new_entry = user(name='example', email='something@gmail.com')
    # new_entry.save()

    # object = user.objects.all()

    return render(request, 'base.html')