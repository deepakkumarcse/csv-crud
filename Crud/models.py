from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name',
                            help_text="Name field you need to fill.")
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Email',
                              help_text="Email field you need to fill.")
    phone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Phone Number',
                             help_text="Phone Number field you need to fill.")

    def __str__(self):
        return self.name