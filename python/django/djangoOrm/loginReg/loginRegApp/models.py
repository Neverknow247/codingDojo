from django.db import models

class userManager(models.Manager):
    def basicValidator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First name must be at least 2 character"
        if postData['firstName'].isalpha():
            pass
        else:
            errors["firstName"] = "First name must only contain letters"
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last name must be at least 2 characters"
        return errors

class users(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = userManager()
