from django.http import JsonResponse
from .models import Quiz

def get_quizzes(request):
    quizzes = Quiz.objects.all().values()
    return JsonResponse(list(quizzes), safe=False)
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_quiz(request):
    if request.method == "POST":
        data = json.loads(request.body)

        quiz = Quiz.objects.create(
            title=data.get("title"),
            description=data.get("description")
        )

        return JsonResponse({"message": "Quiz created successfully"})