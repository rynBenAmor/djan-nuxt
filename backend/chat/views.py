from django.shortcuts import render

# Create your views here.
def chat_page(request):
    return render(request, 'chat/chat_page.html')