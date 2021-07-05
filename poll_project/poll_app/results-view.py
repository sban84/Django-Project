from django.shortcuts import get_object_or_404, render

from poll_app.models import Question


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll_app/results.html', {'question': question})
