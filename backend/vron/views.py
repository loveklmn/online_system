from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from vron.serializers import BookSerializer
from vron.models import Student, Book, Progress, Word, Page, Sentence
# Create your views here.

def login_require(func):
    def wrapper(*args, **kw):
        request = args[0]
        if request.user.is_authenticated:
            return func(*args, **kw)
        else:
            return JsonResponse({'msg': 'Please login first.'})
    return wrapper

@csrf_exempt
def login(request):
    """
    login function
    """

    #if request.user.is_authenticated:
     #   return JsonResponse({'msg': 'you have been logged in.'})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            userobj = User.objects.get_by_natural_key(username)
            if not Student.objects.filter(user=userobj):
                return JsonResponse({'msg': 'your account have not connect to a student'})
            student = Student.objects.get(user=userobj)
            return JsonResponse({'userid': userobj.id, 'level': student.level})
        else:
            return JsonResponse({'msg': 'username or password error.'})
    else:
        return JsonResponse({'msg': 'please use POST method to login'})

@csrf_exempt
@login_require
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
@login_require
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
@login_require
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

