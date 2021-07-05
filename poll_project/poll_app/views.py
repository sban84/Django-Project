from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    #return HttpResponse("Hello World, You are in the poll index app")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll_app/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll_app/detail.html', {'question': question})

# def detail(request, question_id):
#     return HttpResponse(f"You are looking at question {question_id}")


# def results(request, question_id):
#     return HttpResponse(f"You are looking at results of the question {question_id}")

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll_app/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse(f"You are Voting on question {question_id}")


# In Class 5
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll_app/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_app:results', args=(question.id,)))


# Start Creating in Class 5 , to make use of Generic view feature of Django
class IndexView(generic.ListView):

    template_name = 'poll_app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll_app/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll_app/results.html'

# End Creating in Class 5  , to make use of Generic view feature of Django