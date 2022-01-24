import uuid
from django.db import models
from django.urls import reverse

from content_pr.utils import image_path_generator


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=image_path_generator, null=True, default=None, verbose_name='product images')

    FREE_STATUS = 'رایگان'
    PAYMENT_STATUS = 'پولی'

    PAYMENT_CHOICES_FIELD = (
        (FREE_STATUS, 'رایگان'),
        (PAYMENT_STATUS, 'پولی')
    )

    payment_status = models.CharField(max_length=50, choices=PAYMENT_CHOICES_FIELD, default=FREE_STATUS)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('content:content-view', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.title} -> {self.payment_status}'

