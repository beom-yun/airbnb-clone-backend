from .models import Category
from django.http import JsonResponse


def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse({"ok": True})
