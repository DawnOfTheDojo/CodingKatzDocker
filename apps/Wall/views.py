# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..LogReg.models import userDB
from .models import Message, Comment

def wall(request):
    #Retrieve all messages and comments related to user in session and put in context
    #Render wall template
    if "user" in request.session:
        author = userDB.objects.get(id=request.session['user']['id'])
        context = {
            'user': author,
            'all_messages': Message.objects.all().order_by('id').reverse(),
            'comments': Comment.objects.all().order_by('id')
        }
        return render(request, 'Wall/wall.html', context)
    return redirect('LogReg:index')

def message(request):
    #Content from message
    #Validate content
    #Put message in database
    #Return message to page for display
    if request.method == "POST":
        author = userDB.objects.get(id=request.session['user']['id'])
        response = Message.objects.message_check(request.POST, author)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1], extra_tags='message')
    return redirect('Wall:wall')

def comment(request, message_id):
    #Content from comment
    #Validate content
    #Put comment in database
    #Return comment to page for display
    if request.method == "POST":
        author = userDB.objects.get(id=request.session['user']['id'])
        response = Comment.objects.comment_check(request.POST, author, message_id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1], extra_tags = message_id)
    return redirect('Wall:wall')

def deleteMessage(request, message_id):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete message from database

    #Return user to page through redirect
    return redirect('Wall:wall')

def deleteComment(request, comment_id):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete comment from database

    #Return user to page through redirect
    return redirect('Wall:wall')

#display user page with their messages and comments
# def show_user(request, user_id):
#     author = userDB.objects.get(id = user_id)
#     context = {
#         'user': author,
#         'all_messages': Message.objects.filter(author=author).order_by('id').reverse(),
#         'comments': Comment.objects.all().order_by('id')
#     }
#     return render(request, 'Wall/user.html', context)



# Create your views here.
