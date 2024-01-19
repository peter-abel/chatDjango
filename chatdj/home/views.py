from django.shortcuts import redirect, render, HttpResponse

from .models import ChatMessage

# Create your views here.


def home(request):

    messages = ChatMessage.objects.all()

    context = {
        'messages': messages
    }

    return render (request, 'chat.html', context)



def save_message(request):
    if request.method == 'POST':
    
        message = request.POST.get('user_message')
        ChatMessage.objects.create( message=message)
        return redirect('home')
    