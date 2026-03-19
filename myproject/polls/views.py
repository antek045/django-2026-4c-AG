from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')
def list_of_question(request):
    return render(request, 'polls/list_of_question.html')
