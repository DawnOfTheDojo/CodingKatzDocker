# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LogReg.models import userDB
# Create your models here.

class noteManager(models.Manager):
    def note_check(self, data, author, user_id):
        errors = []
        if len(data['note'])  < 1:
            errors.append(['note', 'Note must be entered.'])

        if errors:
            return [False, errors]
        else:
            recipient = userDB.objects.get(id = user_id)
            newNote = Note.objects.create(note=data['note'], author=author, recipient=recipient)
            return [True]

class Note(models.Model):
    note = models.TextField()
    author = models.ForeignKey(userDB, related_name='note_author', on_delete=models.PROTECT)
    recipient = models.ForeignKey(userDB, related_name='note_recipient', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = noteManager()
