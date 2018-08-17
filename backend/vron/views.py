from vron.models import Student, Book, Progress, Word, Page, Sentence, Moment
from rest_framework.authtoken.models import Token
from rest_framework.views import exception_handler, APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import os
from backend import settings
from datetime import datetime
# Create your views here.


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

class BookProgress(APIView):

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            return Response({'msg': 'Book not found.'}, status=404)

        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response({'msg': 'This user have not related to a student.'}, status=403)

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
        if moments:
            for moment in moments:
                community_message = {}
                homework = moment.homework
                community_message['author'] = homework.author.user.username
                community_message['book'] = homework.book.title
                community_message['created_time'] = moment.created_time
                community_message['content'] = homework.content
                community_message['vote_count'] = moment.vote_count
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
