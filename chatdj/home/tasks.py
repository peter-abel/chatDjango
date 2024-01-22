# myapp/tasks.py
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import ChatMessage
from .views import generate_llm_response

@shared_task
def process_user_message(channel_name, user_message):
    # Save user message to the database
    user_chat_message = ChatMessage.objects.create(sender='user', message=user_message)

    # Call LLM API to generate response
    bot_response = generate_llm_response(user_message)

    # Update the saved ChatMessage with the generated response
    user_chat_message.message = bot_response
    user_chat_message.save()

    # Send the bot's response to the user via WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(channel_name, {
        'type': 'chat.message',
        'message': bot_response,
        'status': 'Bot response ready',
    })
