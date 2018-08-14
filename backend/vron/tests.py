from django.test import TestCase
from django.test import Client
from .models import Student
from django.contrib.auth.models import User
import json
from urllib.parse import urlencode

class LoginTestCase(TestCase):
    
    client = Client()
    url = '/vron/login/'
    type = 'application/x-www-form-urlencoded'

    def setUp(self):
        user1 = User.objects.create_user(username = 'zhangsan', password = '][po][po')
        student1 = Student.objects.create(user = user1, level = 2, score = 0)
        user2 = User.objects.create_user(username = 'lisi', password = '][po][po')

    def post_tool(self, input, output):

        data = urlencode(input)
        response = self.client.post(self.url, data = data, content_type = self.type)
        self.assertEqual(json.loads(response.content),output)

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(json.loads(response.content), {'msg': 'please use POST method to login'})

        input = {'username':'zhangsan', 'password':'][po][po'}
        output = {'userid': 1, 'level': 2}
        self.post_tool(input,output)

        input = {'username':'zhangsan', 'password':''}
        output = {'msg': 'username or password error.'}
        self.post_tool(input,output)

        input = {'username':'', 'password':'asdf'}
        output = {'msg': 'username or password error.'}
        self.post_tool(input,output)

        input = {'username':'lisi', 'password':'][po][po'}
        output = {'msg': 'your account have not connect to a student'}
        self.post_tool(input,output)