# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import chain
from operator import attrgetter
from ..LogReg.models import userDB
from ..Wall.models import Message, Comment
from .models import Note

def profile(request):
    #Confirm user id is logged in to view that page
    if "user" in request.session:
    #User information in session and can be displayed on the page through the template
        context = {
            'user': userDB.objects.get(id=request.session['user']['id']),
        }
    #Display user page
        return render(request, 'User/profile.html', context)
    return redirect('LogReg:index')

#validates information and updates user accordingly
def edit(request):
    print(request)
    #Content from edit form
    if request.method == 'POST':
    #Validate content from form
        response = userDB.objects.check_info_edit(request.POST, request.session['user']['id'])
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
        #Update session user
        request.session['user'] = {
            "first_name": response[1].first_name,
            "last_name": response[1].last_name,
            "id": response[1].id,
        }
    #Redirect user to user profile page
    return redirect('User:profile')

def delete(request):
    #Confirm user wants to delete their account

    #Consider whether to Cascade delete user's information, messages, and comments from the database

    #Potential for 'recover account' for users which will bring back all their data

    #Return former user to landing page
    return redirect('LogReg:index')

def note(request, user_id):
    #Content from message
    #Validate content
    #Put message in database
    #Return message to page for display
    if request.method == "POST":
        author = userDB.objects.get(id=request.session['user']['id'])
        response = Note.objects.note_check(request.POST, author, user_id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1], extra_tags='message')
    user = userDB.objects.get(id = user_id)
    all_messages = Message.objects.filter(author=user).order_by('id').reverse()

    all_notes =  Note.objects.filter(recipient=user).order_by('id').reverse()

    all_user_correspondence = sorted(
    chain(all_notes, all_messages),
    key=attrgetter('created_at'))

    context = {
        'user': user,
        'all_correspondence': all_user_correspondence,
        'comments': Comment.objects.all().order_by('id')
    }
    return render(request, 'User/user.html', context)

def comment(request, message_id, user_id):
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
    user = userDB.objects.get(id = user_id)
    all_messages = Message.objects.filter(author=user).order_by('id').reverse()

    all_notes =  Note.objects.filter(recipient=user).order_by('id').reverse()

    all_user_correspondence = sorted(
    chain(all_notes, all_messages),
    key=attrgetter('created_at'))

    context = {
        'user': user,
        'all_correspondence': all_user_correspondence,
        'comments': Comment.objects.all().order_by('id')
    }
    return render(request, 'User/user.html', context)

def deleteMessage(request, message_id):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete message from database

    #Return user to page through redirect
    return redirect('User:user')

def deleteComment(request, comment_id):
    #Figure out how to do confirmation for deletion (possibly pop up alert)

    #Delete comment from database

    #Return user to page through redirect
    return redirect('User:user')

#display user page with their messages and comments
def show_user(request, user_id):
    recipient = userDB.objects.get(id = user_id)
    all_messages = Message.objects.filter(author=recipient).order_by('id').reverse()

    all_notes =  Note.objects.filter(recipient=recipient).order_by('id').reverse()

    all_recipient_correspondence = sorted(
    chain(all_notes, all_messages),
    key=attrgetter('created_at'))

    context = {
        'user': recipient,
        'all_correspondence': all_recipient_correspondence,
        'comments': Comment.objects.all().order_by('id')
    }
    return render(request, 'User/user.html', context)

# Create your views here.
