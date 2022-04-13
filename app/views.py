from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question#{i}",
        "number": i,
    } for i in range(40)
]

ANSWERS = [
    {
        "text": f"hehe#{i}",
        "number": (i % 2),
    } for i in range(20)
]


TAG_QUESTIONS = [
    {
        "title": f"blabla #{i}",
        "text": f"This is text for question#{i}",
        "number": i,
    } for i in range(40)
]


def paginate(objects_list, request, html_page, per_page=10):
    paginator=Paginator(objects_list,per_page)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, html_page, {"questions":objects})

def index(request):
    return paginate(QUESTIONS,request,"index.html",10)

def hot(request):
    return paginate(QUESTIONS, request,"hot.html",10)


def tag(request, s: str):
    paginator = Paginator(TAG_QUESTIONS,10)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, "tag.html", {"tag":s, "questions":objects})


def question(request, i: int):
    paginator = Paginator(ANSWERS, 10)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, "question_page.html", {"answers":objects, "question": QUESTIONS[i]})

def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")

def ask(request):
    return render(request, "ask.html")