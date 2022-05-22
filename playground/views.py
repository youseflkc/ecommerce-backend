from django.db.models import query
from django.db.models.expressions import F, ExpressionWrapper
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django. http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from playground.tasks import notify_customers
from store.models import Cart, CartItem, Product, Customer, Collection, OrderItem, Order
from tags.apps import TagsConfig
from tags.models import TaggedItem
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recieved the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': "yo" })

# @cache_page(5*60)
# def say_hello(request):

#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name':'John'}
#         )
#         message.attach_file('playground/static/images/img1.png')
#         message.send(['johnsmith@domain.com'])
#         mail_admins('subject', 'message',html_message='<h1>message</h1>')
#     except BadHeaderError:
#         pass
