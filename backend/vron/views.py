from vron.models import Student, Book, Progress, Word, Page, Sentence, Moment, Like, Comment, Homework
from rest_framework.authtoken.models import Token
from rest_framework.views import exception_handler, APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
import os
from backend import settings
from datetime import datetime
import json

STUDENTNOTEXIST = {'msg': 'This user have not related to a student.'}
BOOKNOTFOUND = {'msg': 'Book not found'}

def vron_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.data.get('detail'):
            response.data['msg'] = response.data['detail']

    return response


def create_auth_token(sender, instance=None, created=False, **kwargs):
    sender = sender
    kwargs = kwargs
    if created:
        Token.objects.create(user=instance)


class BookList(APIView):
    def get(self, request):
        """
        List all books of one level, or create a new book of this level
        """
        if not Student.objects.filter(user_id=request.user.id):
            return Response({'msg': 'This user have not related to a student.'})
        student = Student.objects.get(user_id=request.user.id)

        books = Book.objects.filter(level=student.level)
        if not books.exists():
            return Response({'msg': 'Cannot find book for this level'}, status=404)
        else:
            bookinfos = []
            for book in books:
                progress = {}
                if not Progress.objects.filter(user_id=request.user.id, book=book):
                    Progress.objects.create(
                        user_id=request.user.id, book=book, current_page=0)
                progress = Progress.objects.get(
                    user_id=request.user.id, book=book)
                bookinfo = {}
                bookinfo['id'] = book.id
                bookinfo['cover'] = book.cover
                bookinfo['title'] = book.title
                bookinfo['pages_num'] = book.pages_num
                bookinfo['progress'] = {
                    'current_page': progress.current_page,
                    'punched': progress.punched,
                    'latest_read_time': progress.latest_read_time
                }
                bookinfo['type'] = book.read_type
                bookinfos.append(bookinfo)
            bookinfos = sorted(
                bookinfos, key=lambda x: x['progress']['latest_read_time'], reverse=True)
            return Response(bookinfos)


class BookGuidance(APIView):

    def get(self, request, book_id):
        '''
        List guidance of a book.
        '''
        book_data = Book.objects.filter(id=book_id)
        if book_data:
            book = book_data[0]
            words = Word.objects.filter(guidance=book)
            parental_info = {}
            parental_info['guidance'] = book.guidance
            parental_info['words'] = []
            if words:
                for word in words:
                    word_info = {}
                    word_info['word'] = word.word
                    #word_info['audio'] = word.audio
                    word_info['meaning'] = word.meaning
                    parental_info['words'].append(word_info)
            return Response(parental_info)

        else:
            return Response({'msg': 'Book not found'}, status=404)

class BookHomework(APIView):

    def get(self, request, book_id):
        '''
        GET User homework
        '''
        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response(STUDENTNOTEXIST, status=403)

        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return Response(BOOKNOTFOUND, status=404)

        homework_info = {}
        homework_info['assignment'] = book.assignment
        homework_info['homework'] = {}

        try:
            homework = Homework.objects.get(book_id=book_id, author=student)
            homework_info['homework']['content'] = homework.content
            homework_info['homework']['attachments'] = {}
            homework_info['homework']['attachments']['image'] = homework.images.split()
            homework_info['homework']['attachments']['video'] = homework.videos.split()
            homework_info['homework']['attachments']['audio'] = homework.audios.split()
        except ObjectDoesNotExist:
            pass

        return Response(homework_info)

    def post(self, request, book_id):
        '''
        POST: upload user homework
        '''
        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response(STUDENTNOTEXIST, status=403)

        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return Response(BOOKNOTFOUND, status=404)

        try:
            homework = Homework.objects.get(book=book, author=student)
        except ObjectDoesNotExist:
            homework = Homework.objects.create(book=book, author=student, content=' ')
        homework.content = request.POST.get('content', ' ')
        attachments = json.loads(request.POST.get('attachments',r'{}'))
        homework.images = ' '.join(attachments.get('image', ''))
        homework.videos = ' '.join(attachments.get('video', ''))
        homework.audios = ' '.join(attachments.get('audio', ''))
        homework.save()
        return Response(status=201)


class BookProgress(APIView):

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return Response({'msg': 'Book not found.'}, status=404)

        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response(STUDENTNOTEXIST, status=403)

        try:
            progress = Progress.objects.get(user=student, book=book)
            progress.current_page = request.POST.get('current_page', progress.current_page)
            progress.latest_read_time = datetime.now()
            progress.save()
        except ObjectDoesNotExist:
            Progress.objects.create(user=student, book=book, current_page=request.POST.get('current_page',0))
        return Response(status=201)

class BookEbook(APIView):

    def get(self, request, book_id):
        book_data = Book.objects.filter(id=book_id)
        if not book_data:
            return Response({'msg': 'Book not found'}, status=404)

        pages = Page.objects.filter(book_id=book_id).order_by('number')
        ebook_infos = []
        if pages:
            for page in pages:
                page_info = {}
                page_info['number'] = page.number
                page_info['picture'] = page.picture
                page_info['sentences'] = []
                sentences = Sentence.objects.filter(page=page)
                if sentences:
                    for sentence in sentences:
                        sentence_info = {}
                        sentence_info['content'] = sentence.content
                        sentence_info['audio'] = sentence.audio
                        sentence_info['translated'] = sentence.translated
                        sentence_info['x1'] = sentence.x1
                        sentence_info['y1'] = sentence.y1
                        sentence_info['x2'] = sentence.x2
                        sentence_info['y2'] = sentence.y2
                        page_info['sentences'].append(sentence_info)
                ebook_infos.append(page_info)
        return Response(ebook_infos)

class CommunityGroup(APIView):
    def get(self, request, level):
        community_info = []
        moments = Moment.objects.filter(level=level)
        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response(STUDENTNOTEXIST, status=403)
        if moments:
            for moment in moments:
                community_message = {}
                homework = moment.homework

                community_message['author'] = {}
                community_message['author']['username'] = homework.author.user.username
                community_message['author']['avatar'] = student.avatar

                community_message['action'] = {}
                community_message['action']['liked'] = False
                like = Like.objects.filter(actor=student, target=moment)
                if like and like[0].liked==True:
                    community_message['action']['liked'] = True

                community_message['book'] = {}
                community_message['book']['title'] = homework.book.title
                community_message['book']['cover'] = homework.book.cover

                community_message['created_time'] = moment.created_time

                community_message['content'] = homework.content

                community_message['attactments'] = {}
                community_message['attactments']['image'] = homework.images.split()
                community_message['attactments']['video'] = homework.videos.split()

                community_message['vote_count'] = moment.vote_count
                community_message['comment_count'] = len(Comment.objects.filter(target=moment))
                community_info.append(community_message)

        return Response(community_info)

class UploadFile(APIView):
    def post(self, request):
        file = request.FILES.get('file', None)
        if not file:
            return Response({'msg': 'No file upload'}, status=400)

        path = os.path.join(settings.BASE_DIR, 'static', 'upload', file.name)
        filepath = open(path, 'wb+')
        for chunk in file.chunks():
            filepath.write(chunk)
        filepath.close()
        response = {
            'msg': 'Upload success!',
            'savepath': os.path.join('static', 'upload', file.name),
        }
        return Response(response, status=201)

class UserInfo(APIView):
    def get(self, request):
        student_query = Student.objects.filter(user=request.user)
        if not student_query.exists():
            return Response(STUDENTNOTEXIST, status=404)

        student = student_query[0]
        nickname = student.nickname if student.nickname else request.user.username
        avatar = student.avatar
        level = student.level

        userinfo = {
            'nickname': nickname,
            'avatar': avatar,
            'level': level
        }

        return Response(userinfo)

    def post(self, request):
        student_query = Student.objects.filter(user=request.user)
        if not student_query.exists():
            return Response(STUDENTNOTEXIST, status=404)

        student = student_query[0]
        student.nickname = request.POST.get('nickname', student.nickname)
        student.avatar = request.POST.get('avatar', student.avatar)

        student.save()
        return Response(status=201)


