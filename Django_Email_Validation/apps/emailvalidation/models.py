from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
    def validate_add(self, request, address):
        if address == '':
            messages.info(request, 'Email address cannot be blank!')
            return False
        elif not EMAIL_REGEX.match(address):
            messages.info(request, 'Please enter a valid email address!')
            return False
        elif Email.emailManager.filter(address=address):
            messages.info(request, 'Email address ' + address + ' already registered!')
            return False
        else:
            addemail = Email.emailManager.create(address=address)
            addemail.save
            messages.info(request, 'Email ' + addemail.address + ' added to database!')
            return True

    # def remove(self, request, id):
    #     remove_email = Email.emailManager.get(id=id)
    #     remove_email.delete()
    #     messages.info(request, 'Email ' + remove_email.address + ' successfully removed.')
    #     return True

class Email(models.Model):
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    emailManager = EmailManager()
