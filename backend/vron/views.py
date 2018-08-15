from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from vron.serializers import BookSerializer
from vron.models import Student, Book, Progress, Word, Page, Sentence, Moment
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
import os
from backend import settings
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

@csrf_exempt
@api_view(['GET','POST'])
def book_list(request):
    """
    List all books of one level, or create a new book of this level
    """
    if not Student.objects.filter(user_id=request.user.id):
        return JsonResponse({'msg': 'This user have not related to a student.'})
    student = Student.objects.get(user_id=request.user.id)
    if request.method == 'GET':

        books = Book.objects.filter(level=student.level)
        if not books.exists():
            return JsonResponse({'msg': 'Cannot find book for this level'})
        else:
            bookinfos = []
            for book in books:
                progress = {}
                if not Progress.objects.filter(user_id=request.user.id, book=book):
                    Progress.objects.create(user_id=request.user.id, book=book, current_page=0)
                progress = Progress.objects.get(user_id=request.user.id, book=book)
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
            bookinfos = sorted(bookinfos, key=lambda x:x['progress']['latest_read_time'], reverse=True)
            return JsonResponse(bookinfos, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['level'] = student.level
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET','POST'])
def book_guidance(request, book_id):
    '''
    List guidance of a book, or add a guidance of a book.
    '''
    if request.method == 'GET':
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
                    word_info['audio'] = word.audio
                    word_info['meaning'] = word.meaning
                    parental_info['words'].append(word_info)
            return JsonResponse(parental_info)

        else:
            return JsonResponse({'msg': 'Book not found'}, status=404)

    else:
        return JsonResponse({'msg': 'Please use GET method'})

@csrf_exempt
@api_view(['GET','POST'])
def book_ebook(request, book_id):
    if request.method == 'GET':
        book_data = Book.objects.filter(id=book_id)
        if not book_data:
            return JsonResponse({'msg': 'Book not found'})

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
        return JsonResponse(ebook_infos, safe=False)
    else:
        return JsonResponse({'msg': 'Please use GET method'})

@csrf_exempt
@api_view(['GET','POST'])
def community_group(request, level):
    if request.method == 'GET':
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

        return JsonResponse(community_info, safe=False)
    else:
        return JsonResponse({'msg': 'Please use GET method.'})

@csrf_exempt
#@api_view(['POST'])
def upload_file(request):
    #assert False
    file = request.FILES.get('file', None)
    if not file:
        return JsonResponse({'msg': 'No file upload'})

    path = os.path.join(settings.BASE_DIR, 'static', 'upload', file.name)
    filepath = open(path, 'wb+')
    for chunk in file.chunks():
        filepath.write(chunk)
    filepath.close()
    response = {
        'msg': 'Upload success!',
        'savepath': os.path.join('static', 'upload', file.name),
    }
    return JsonResponse(response)
