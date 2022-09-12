import logging
from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

# Create your models here.

log = logging.getLogger(__name__)


class Ad(models.Model):

    # usual fields
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    text = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    # link to the internal auth mechanism - user-owner of the item
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # link to the Comments table in the app DB
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      through='Comment', related_name='comments_owned')

    # auto-populated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # picture
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file')

    # Shows up in the admin list
    def __str__(self):
        return f"({self.price}$) (owner: {self.owner}) {self.title}"

    def __repr__(self) -> str:
        return f"({self.price})$ [{self.title}] [{self.text}] [{self.owner}]"


class Comment(models.Model):

    # comment text
    text = models.TextField(validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")])

    # foreign keys - to auth table and to Ad table
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # standard auto-populated fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15:
            return self.text

        return self.text[:11] + ' ...'
