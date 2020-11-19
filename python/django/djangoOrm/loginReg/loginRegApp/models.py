from django.db import models
import re
import bcrypt

class userManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if postData['firstName'].isalpha():
            pass
        else:
            errors["firstName"] = "First Name must only contain letters!"
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First Name must be at least 2 characters!"
        if postData['lastName'].isalpha():
            pass
        else:
            errors["lastName"] = "Last Name must only contain letters!"
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last Name must be at least 2 characters!"
        email_regex = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors["email"] = "Invalid Email Address!"
        if postData['password'] != postData['cnfmpw']:
            errors["password"] = "Passwords must match!"
        return errors
    
    def loginValidator(self, postData):
        errors = {}
        emailMatch = users.objects.filter(email= postData['email'])
        if len(postData['email']) == 0:
            errors["email"] = "Email is required"
        elif len(emailMatch) == 0:
            errors['emailNoMatch'] = "Email does not exist!"
        if bcrypt.checkpw(postData['password'].encode(), emailMatch[0].password.encode()):
            pass
        else:
            errors['pwmatch'] = "Incorrect Password!"
        return errors

class users(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = userManager()
