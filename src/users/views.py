from xml.dom.minidom import Identified
from django.shortcuts import render


def get_users_page(request):
    return render(request, 'auth/sign_in.html')


