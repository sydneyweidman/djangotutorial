from django.shortcuts import render_to_response
from polls.models import Question
# Create your views here.

def index(request):
    context = Question.objects.all()
    return render_to_response("polls/index.html", context={'context':context})