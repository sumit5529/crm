# emailapp/models.py

from django.db import models

class EmailContent(models.Model):
    recipient_email = models.EmailField()
    message_text = models.TextField()

    def __str__(self):
        return self.recipient_email  # Display recipient email in admin panel
