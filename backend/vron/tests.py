from django.test import TestCase
from django.test import Client

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory, APIClient
#from .models import Student
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .views import BookList
from .models import Book, Student, Word, Homework, Moment

class TokenTestCase(TestCase):

    client = Client()
    type = 'application/x-www-form-urlencoded'

    def setUp(self):
        User.objects.create_user(username='admin', password='admin')

    def test(self):
        data1 = {'username': 'admin','password': 'admin'}
        data2 = {'username': 'admin','password': 'asdasd'}
        response = self.client.post('/vron/get-token/', data=data1)
        self.assertContains(response, 'token')
        response = self.client.post('/vron/get-token/', data=data2)
        self.assertNotContains(response, 'token', status_code=400)
        response = self.client.get('/vron/get-token/', data=data1)
        self.assertNotContains(response, 'token', status_code=405)

class BookTestCase(TestCase):

    factory = APIRequestFactory()
    test_client = APIClient()

    def setUp(self):

        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = 'Token ' + Token.objects.get(user=self.user).key
        self.test_client.force_authenticate(user=self.user)
        stu = Student.objects.create(
            user=self.user, level=1, avatar="", score=0)

        for _ in range(10):
            book = Book.objects.create(cover='cover', level=1, title='title1',
                                pages_num=30, assignment='assign',
                                guidance='guide', read_type='IR')
            Word.objects.create(guidance=book, word='www', meaning='MMM')
            homework = Homework.objects.create(author=stu, book=book,
                                content='ssd')
            Moment.objects.create(homework=homework, level=1)
    def test_book_list(self):
        view = BookList.as_view()

        request = self.factory.get('/vron/books/')
        response = view(request)
        self.assertContains(response, 'msg', status_code=401)

        request = self.factory.post('/vron/books/')
        force_authenticate(request, self.user)
        response = view(request)
        self.assertContains(response, 'msg', status_code=405)

        request = self.factory.get('/vron/books/')
        force_authenticate(request, self.user)
        response = view(request)
        self.assertIn('id', response.data[0])
        self.assertIn('cover', response.data[0])
        self.assertIn('title', response.data[0])
        self.assertIn('pages_num', response.data[0])
        self.assertIn('progress', response.data[0])
        self.assertIn('type', response.data[0])
        self.assertNotIn('msg', response.data[0])

    def test_book_guidance(self):
        self.test_client.force_authenticate(user=self.user)
        response = self.test_client.get('/vron/books/1/guidance/')
        self.assertIn('guidance', response.data)
        self.assertIn('words', response.data)
        self.assertIn('word', response.data['words'][0])
        self.assertIn('meaning', response.data['words'][0])
        self.assertNotIn('msg', response.data)

    def test_community(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/community/1/')
        self.assertIn('author', response.data[0])
        self.assertIn('attactments', response.data[0])
