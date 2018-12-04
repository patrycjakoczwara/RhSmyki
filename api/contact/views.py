from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import viewsets, status, response
from .serializers import ContactMessageSerializer


class ContactMessageView(viewsets.ViewSet):

    def create(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = EmailMessage(
            'Contact from {name}'.format(name=data.get('name')),
            data.get('content'),
            data.get('email'),
            [settings.EMAIL_HOST_USER],
            reply_to=[data.get('email')]
        )
        email.send(fail_silently=False)
        return response.Response(data='Email message has been sent.',
                                 status=status.HTTP_200_OK)
