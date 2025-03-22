from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

class Question:
    def __init__(self, question_id):
        self.question_text = str(question_id) + '_text'
        self.id = question_id
        self.choice_set = ['answer_1', 'answer_2', 'answer_3']

latest_question_list = []
for i in range(5):
    latest_question_list.append(Question(i))

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     # latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question": question})

    try:
        question = latest_question_list[question_id] #Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)