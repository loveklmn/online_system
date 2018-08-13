# from django.shortcuts import render

# Create your views here.

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
            student = Student.objects.get(user=userobj)
            return JsonResponse({'userid': userobj.id, 'level': student.level})
        else:
            return JsonResponse({'msg': 'username or password error.'})
    else:
        return JsonResponse({'msg': 'please use POST method to login'})

@csrf_exempt
def book_list(request):
    """
    List all books of one level, or create a new book of this level
    """
    if not request.user.is_authenticated:
        return JsonResponse({'msg': 'Please login first.'})

    if request.method == 'GET':
        if not Student.objects.filter(user_id=request.user.id):
            return JsonResponse({'msg': 'This user have not related to a student.'})
        student = Student.objects.get(user_id=request.user.id)
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
        data['level'] = level
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
