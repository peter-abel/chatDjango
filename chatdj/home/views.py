from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import ChatMessage
#from .tasks import generate_llm_response


from .models import ChatMessage
import cohere



# Create your views here.
api_key= 'OE0Svq9tYCRbVEciPt2MD4Um55HP9UoLRolazvcv'
co = cohere.Client(api_key)


def home(request):

    messages = ChatMessage.objects.all()

    context = {
        'messages': messages
    }

    return render (request, 'chat.html', context)


def save_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        # Save user message to database
        user_chat_message = ChatMessage.objects.create(sender='user', message=user_message)

        # Call LLM API to generate response
        bot_response = generate_llm_response(user_message)

        # Update the saved ChatMessage with the generated response
        user_chat_message.message = bot_response
        user_chat_message.save()

        return redirect('home')

    return HttpResponse('Invalid request')

def generate_llm_response(user_message,request):
    user_message = request.POST.get('user_message', '')
    # Replace this with your actual LLM API call
    response = co.generate(
        model='command-nightly',
        prompt = user_message
        )
  
    bot_response = response.generations[0].text
    return bot_response

"""s
"
def save_message(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message', '')
        
        # Save user message to database
        user_chat_message = ChatMessage.objects.create(sender='bot', message=user_message)

        # Call LLM API to generate response
        response = co.generate(
        model='command-nightly',
        prompt = user_message
        )
        bot_response = response.generations[0].text

        # Update the saved ChatMessage with the generated response
        user_chat_message.message = bot_response
        user_chat_message.save()

        return redirect('home')


        """
        