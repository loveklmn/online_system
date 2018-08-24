from django.test import TestCase
from django.test import Client

from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory, APIClient
#from .models import Student
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .views import BookList
from .models import Book, Student, Word, Homework, Moment, Notice, ActiveKey, Page, Sentence
import json


class TokenTestCase(TestCase):

    client = Client()
    type = 'application/x-www-form-urlencoded'

    def setUp(self):
        User.objects.create_user(username='admin', password='admin')

    def test(self):
        data1 = {'username': 'admin', 'password': 'admin'}
        data2 = {'username': 'admin', 'password': 'asdasd'}
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

        self.user = User.objects.create_user(username='stu', password='stu')
        self.admin = User.objects.create_user(
            username='admin', password='admin')
        self.user_err_level = User.objects.create_user(username='err')
        self.token = 'Token ' + Token.objects.get(user=self.user).key
        self.test_client.force_authenticate(user=self.user)
        stu = Student.objects.create(
            user=self.user, level=1, avatar="", score=0)
        Student.objects.create(
            user=self.user_err_level,
            level=-1,
            avatar="",
            score=0
        )
        Book.objects.all().delete()
        for ID in range(10):
            book = Book.objects.create(id=ID+1, cover='cover', level=1, title='title1',
                                       pages_num=30, assignment='assign',
                                       guidance='guide', read_type='IR')
            Word.objects.create(guidance=book, word='www', meaning='MMM')
            homework = Homework.objects.create(author=stu, book=book,
                                               content='ssd')
            page = Page.objects.create(book=book, number=1, picture='pic')
            Sentence(page=page, content='empty',
                    audio='audio', translated='trans',
                    x1=1, x2=2, y1=3, y2=4)
            Moment.objects.create(homework=homework, level=1)
            Notice.objects.create(id=ID+1, content="Notice{}".format(ID))
        ActiveKey.objects.create(level=1, key="114514")

    def test_book_list1(self):
        view = BookList.as_view()
        request = self.factory.get('/vron/books/')
        response = view(request)
        self.assertContains(response, 'msg', status_code=401)

    def test_book_list2(self):
        view = BookList.as_view()
        request = self.factory.post('/vron/books/')
        force_authenticate(request, self.user)
        response = view(request)
        self.assertContains(response, 'msg', status_code=403)

    def test_book_list3(self):
        #User get booklist
        view = BookList.as_view()
        request = self.factory.get('/vron/books/')
        force_authenticate(request, self.user)
        response = view(request)
        attrs = ['id',  'title', 'cover', 'type', 'pages_num', 'progress']
        for attr in attrs:
            self.assertIn(attr, response.data[0])
        self.assertNotIn('msg', response.data[0])

    def test_book_list4(self):
        #Admin get BookList
        view = BookList.as_view()
        request = self.factory.get('/vron/books/')
        force_authenticate(request, self.admin)
        response = view(request)
        attrs = ['id', 'level', 'title', 'cover', 'type', 'pages_num']
        for attr in attrs:
            self.assertIn(attr, response.data[0])

    def test_book_list5(self):
        #User with error level get BookList
        view = BookList.as_view()
        request = self.factory.get('/vron/books/')
        force_authenticate(request, self.user_err_level)
        response = view(request)
        self.assertIn('msg', response.data)

    def test_book_list6(self):
        #User post BookList：Denied
        view = BookList.as_view()
        request = self.factory.post('/vron/books/')
        force_authenticate(request, self.user)
        response = view(request)
        self.assertContains(response, 'msg', status_code=403)

    def test_book_list7(self):
        #Add new book
        view = BookList.as_view()
        data = {
            'id': -1, 'cover': 'cover',
            'level': 1, 'title': 'title',
            'pages_num': 20, 'assignment': 'assign',
            'guidance': 'guidance', 'read_type': 'ER'
        }
        request = self.factory.post(
            '/vron/books/', json.dumps(data),
            content_type="application/json")
        force_authenticate(request, self.admin)
        response = view(request)
        attrs = ['id', 'cover', 'level', 'title', 'assignment',
                 'guidance', 'pages_num', 'read_type']
        for attr in attrs:
            self.assertContains(response, attr, status_code=201)

    def test_book_list8(self):
        #All data update
        attrs = ['id', 'cover', 'level', 'title', 'assignment',
                 'guidance', 'pages_num', 'read_type']
        view = BookList.as_view()
        data = {
            'id': 3, 'cover': 'cover', 'level': 1, 'title': 'title',
            'pages_num': 20, 'assignment': 'assign',
            'guidance': 'guidance', 'read_type': 'ER'
        }
        request = self.factory.post(
            '/vron/books/', json.dumps(data),
            content_type="application/json")
        force_authenticate(request, self.admin)
        response = view(request)
        for attr in attrs:
            self.assertContains(response,
                                attr,
                                status_code=201)

    def test_book_list9(self):
        #No data update
        attrs = ['id', 'cover', 'level', 'title', 'assignment',
                 'guidance', 'pages_num', 'read_type']
        view = BookList.as_view()
        request = self.factory.post(
            '/vron/books/', json.dumps({'id': 2}),
            content_type="application/json")
        force_authenticate(request, self.admin)
        response = view(request)
        for attr in attrs:
            self.assertContains(response, attr, status_code=201)

    def test_book_guidance1(self):
        #User get guidance
        self.test_client.force_authenticate(user=self.user)
        response = self.test_client.get('/vron/books/2/guidance/')
        self.assertIn('guidance', response.data)
        self.assertIn('words', response.data)
        self.assertIn('word', response.data['words'][0])
        self.assertIn('meaning', response.data['words'][0])
        self.assertNotIn('msg', response.data)

    def test_book_guidance2(self):
        '''
        Admin post guidance
        '''
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.post('/vron/books/2/guidance/',
                               json.dumps({
                                   'guidance': 'guidance',
                                   'words': [
                                       {
                                           'word': 'word',
                                           'meaning': 'meaning'
                                       }
                                   ]
                               }), content_type="application/json")
        attrs = ['guidance', 'words']
        for attr in attrs:
            self.assertIn(attr, response.data)
        self.assertEqual('word', response.data['words'][0]['word'])
        self.assertEqual('meaning', response.data['words'][0]['meaning'])

    def test_community(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/community/')
        attrs = ['author', 'action', 'book', 'created_time', 'content',
                 'attactments', 'vote_count', 'comment_count']
        for attr in attrs:
            self.assertIn(attr, response.data[0])

    def test_homework1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/books/3/homework/')
        attrs = ['assignment', 'homework']
        for attr in attrs:
            self.assertIn(attr, response.data)

    def test_homework2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.get('/vron/books/3/homework/')
        self.assertIn('assignment', response.data)

    def test_homework3(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {
            'content': 'content',
            'attachments': {
                'image': [
                    'img_path1',
                    'img_path2'
                ],
                'video': [
                    'v_path1',
                    'v_path2'
                ],
                'audio': [
                    'a_path1',
                    'a_path2'
                ]
            }
        }
        data_str = json.dumps(data)
        response = client.post('/vron/books/3/homework/',
                               data_str, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_homework4(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        data = {
            'assignment': 'assign'
        }
        response = client.post('/vron/books/3/homework/',
                               json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('assignment'), 'assign')
        self.assertIn('id', response.data)

    def test_progress1(self):
        client = APIClient()
        data = {
            'current_page': 20
        }
        client.force_authenticate(user=self.user)
        response = client.post('/vron/books/4/progress/',
                               json.dumps(data), content_type="application/json")
        self.assertEqual(201, response.status_code)

    def test_progress2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.post('/vron/books/4/progress/',
                               json.dumps({}), content_type="application/json")
        self.assertEqual(403, response.status_code)

    def test_book_ebook1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/books/4/ebook/')
        attrs = ['number', 'picture', 'sentences']
        for attr in attrs:
            self.assertIn(attr, response.data[0])

    def test_book_ebook2(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/vron/books/4/ebook/')
        self.assertEqual(403, response.status_code)

    def test_book_ebook3(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        data = {
            'number': 5,
            'picture': "http://a/x",
            'sentences': [
                {
                    'content': "I do something",
                    'audio': "http://a/b",
                    'translated': "trans",
                    'x1': 100,
                    'y1': 50,
                    'x2': 20,
                    'y2': 10
                },
                {
                    'content': "I did something",
                    'audio': "http://a/b",
                    'translated': "trans",
                    'x1': 100,
                    'y1': 50,
                    'x2': 20,
                    'y2': 50
                }
            ]
        }
        response = client.post('/vron/books/4/ebook/',
                               json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_user_info1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/userinfo/')
        self.assertEqual(200, response.status_code)
        attrs = ['nickname', 'avatar', 'level']
        for attr in attrs:
            self.assertIn(attr, response.data)

    def test_user_info2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.get('/vron/userinfo/')
        self.assertEqual(403, response.status_code)
        self.assertIn('msg', response.data)

    def test_user_info3(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            '/vron/userinfo/', json.dumps({}), content_type="application/json")
        self.assertEqual(201, response.status_code)

    def test_user_info4(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        data = {
            'nickname': 'foo',
            'avatar': 'Im Chinese'
        }
        response = client.post(
            '/vron/userinfo/', json.dumps(data), content_type="application/json")
        self.assertEqual(201, response.status_code)

    def test_user_info5(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.post(
            '/vron/userinfo/', json.dumps({}), content_type="application/json")
        self.assertEqual(403, response.status_code)
        self.assertIn('msg', response.data)

    def test_notice_info1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/notices/')
        attrs = ['id', 'content', 'have_read', 'created_time']
        for attr in attrs:
            self.assertIn(attr, response.data[0])

    def test_notice_info2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.get('/vron/notices/')
        self.assertIn('msg', response.data)
        self.assertEqual(403, response.status_code)

    def test_notice_info3(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/vron/notices/')
        self.assertEqual(405, response.status_code)

    def test_notice_mark1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/vron/notices/readed/',
                               json.dumps({'id': 1}), content_type="application/json")
        self.assertEqual(201, response.status_code)

    def test_notice_mark2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.post('/vron/notices/readed/',
                               json.dumps({}), content_type="application/json")
        self.assertEqual(403, response.status_code)

    def test_student_list1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/vron/students/')
        self.assertEqual(403, response.status_code)

    def test_student_list2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.get('/vron/students/')
        attrs = ['username', 'level', 'nickname', 'score']
        for attr in attrs:
            self.assertIn(attr, response.data[0])

    def test_key_gen1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/vron/generatekey/',
                               json.dumps({'level': 1, 'count': 10}),
                               content_type="application/json")
        self.assertEqual(403, response.status_code)

    def test_key_gen2(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.post('/vron/generatekey/',
                               json.dumps({'level': 1, 'count': 10}),
                               content_type="application/json")
        self.assertEqual(201, response.status_code)
        self.assertEqual(10, len(response.data))

    def test_change_password1(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        password = 'asdfghjklqewq'
        response = client.post('/vron/userinfo/change-password/',
                               json.dumps({'password': password}),
                               content_type="application/json")
        self.assertEqual(200, response.status_code)

    def test_change_password2(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        password = 'asd'
        response = client.post('/vron/userinfo/change-password/',
                               json.dumps({'password': password}),
                               content_type="application/json")
        self.assertEqual(400, response.status_code)

    def test_change_password3(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/vron/userinfo/change-password/',
                               json.dumps({}),
                               content_type="application/json")
        self.assertEqual(400, response.status_code)

    def test_register1(self):
        client = APIClient()
        data = {
            'username': 'foo',
            'password': 'imchinese',
            'key': '114514'
        }
        response = client.post('/vron/register/',
                               json.dumps(data),
                               content_type="application/json")
        self.assertEqual(201, response.status_code)

    def test_register2(self):
        client = APIClient()
        data = {
            'username': 'foo',
            'password': 'imchinese',
            'key': '810'
        }
        response = client.post('/vron/register/',
                               json.dumps(data),
                               content_type="application/json")
        self.assertEqual(403, response.status_code)

    def test_register3(self):
        client = APIClient()
        data = {
            'username': 'stu',
            'password': 'imchinese',
            'key': '114514'
        }
        response = client.post('/vron/register/',
                               json.dumps(data),
                               content_type="application/json")
        self.assertEqual(403, response.status_code)
