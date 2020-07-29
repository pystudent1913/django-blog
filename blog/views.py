# Imports
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {}
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    context = {}
    return render(request, "blog/login.html", context)

# def test(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # context = {'latest_question_list': latest_question_list}
#     context = {}
#     return render(request, 'blog/index.html', context)