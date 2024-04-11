from django.http import JsonResponse
from tika import parser

def extract_text(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        parsed = parser.from_file(file.read())
        text = parsed['content']
        return JsonResponse({'text': text})
    return JsonResponse({'error': 'no file provided'}, status=400)
