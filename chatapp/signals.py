# from django.db.models.signals import post_save, pre_delete
# from customer.models import Customer
# from customer.forms import CustomerForm
from django.dispatch import Signal,receiver
from .models import ChatRoom
 
 
# @receiver(post_save, sender=Customer)
# def build_chatroom(sender, instance, created, **kwargs):
#     if created:
#         item = Customer.objects.get(sender.pk)
#         # # cleaned_data = item.cleaned_data
#         # print(iitem)
#         # print("done")
#         # item = CustomerForm(instance=iitem)
#         # username = item.cleaned_data['name']
#         # useremail = item.cleaned_data['email']
#         # form = ChatRoom.objects.create(user = username,slug = useremail)
#         # form.save()
#         ChatRoom.objects.create(name = item.cleaned_data['name'])

        
  
# @receiver(post_save, sender=Customer)
# def save_chatroom(sender, instance, **kwargs):
#         instance.chatroom.save()

notification = Signal()

@receiver(notification)
def create_chatroom(sender,username,useremail,**kwargs):
    # print(useremail)
    # print(username)
    ChatRoom.objects.create(name = username ,slug = username)
