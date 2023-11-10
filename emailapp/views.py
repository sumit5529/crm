# emailapp/views.py

from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .forms import EmailForm
from .models import EmailContent

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            message_text = form.cleaned_data['message_text']

            # Save email content to the database (optional)
            EmailContent.objects.create(recipient_email=recipient_email, message_text=message_text)

            # Send the email
            send_mail(
                'Subject here',  
                message_text, 
                '20bec044@nith.ac.in',  
                [recipient_email], 
                fail_silently=False,
            )
            return redirect('send-email')
    else:
        form = EmailForm()

    return render(request, 'email_form.html', {'form': form})
