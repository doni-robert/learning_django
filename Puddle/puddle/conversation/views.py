from django.shortcuts import render, get_object_or_404, redirect

from .forms import ConversationMessageForm

from item.models import Item
from .models import Conversation

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass
    if request.method == 'P0ST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.member.add(request.user)
            conversation.member.add(item.created_by)
            conversation.save()

            conversation_message = form.save()