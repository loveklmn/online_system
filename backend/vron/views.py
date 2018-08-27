from vron.models import Notice, IsNoticeReaded, Student, Book, Progress, Word, Page, Sentence, Moment, Like, Comment, Homework, ActiveKey, MatchingGame, JigsawGame, RecognitionGame, ClozeGame
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import exception_handler, APIView
from rest_framework.exceptions import NotFound, PermissionDenied, ParseError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
import os
from backend import settings
from datetime import timedelta
from django.utils import timezone
import json, random, string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from rest_framework import status

STUDENTNOTEXIST = {'msg': 'This user have not related to a student.'}
BOOKNOTFOUND = {'msg': 'Book not found'}

def bit_to_num(bit):
    return 1 << (bit-1)

def num_to_bit(num):
    bit_array = []
    for i in range(32):
        if num%2:
            bit_array.append(i+1)
        num = num >> 1
    return bit_array

def manager_required(func):
    '''
    只能装饰APIView类post或get成员函数
    '''
    def warpper(*args, **kwargs):
        request = args[1]
        stu_query = Student.objects.filter(user=request.user)
        if stu_query.exists():
            raise PermissionDenied()
        else:
            return func(*args, **kwargs)
    return warpper


def stu_required(func):
    '''
    只能装饰APIView类post或get成员函数
    '''
    def warpper(*args, **kwargs):
        request = args[1]
        stu_query = Student.objects.filter(user=request.user)
        if not stu_query.exists():
            raise PermissionDenied()
        else:
            return func(*args, **kwargs)
    return warpper

def is_admin(user):
    return not Student.objects.filter(user=user).exists()

def get_book(**kwargs):
    '''
    require: id=book_id or level = book_level
    '''
    book_query = Book.objects.filter(**kwargs)
    if not book_query.exists():
        raise NotFound('Book({}) not found.'.format(kwargs))
    return book_query

def get_or_raise(data, attr):
    if data.get(attr):
        return data[attr]
    else:
        raise ParseError('Attr "{}" cannot be empty.'.format(attr))

def vron_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.data.get('detail'):
            response.data['msg'] = response.data['detail']
            del response.data['detail']
    return response


def create_auth_token(sender, instance=None, created=False, **kwargs):
    sender = sender
    kwargs = kwargs
    if created:
        Token.objects.create(user=instance)

def update_student_score(stu):
    score = 0
    progresses = Progress.objects.filter(user=stu)
    if progresses:
        for progress in progresses:
            score += progress.current_page * 10
            if progress.punched == True:
                score += progress.current_page * 3
    stu.score = score
    stu.save()

class BookList(APIView):
    def get(self, request):
        """
        List all books of one level, or create a new book of this level
        """
        isManager = False
        if is_admin(request.user):
            books = Book.objects.all()
            isManager = True
        else:
            student = Student.objects.get(user_id=request.user.id)
            books = get_book(level=student.level)

        bookinfos = []
        for book in books:

            bookinfo = {}
            bookinfo['id'] = book.id
            bookinfo['cover'] = book.cover
            bookinfo['title'] = book.title
            bookinfo['pages_num'] = book.pages_num
            bookinfo['type'] = book.read_type

            if not isManager:
                progress = {}
                if not Progress.objects.filter(user=student, book=book):
                    Progress.objects.create(
                        user=student, book=book, current_page=0)
                progress = Progress.objects.get(
                    user=student, book=book)
                bookinfo['progress'] = {
                    'current_page': progress.current_page,
                    'punched': progress.punched,
                    'latest_read_time': progress.latest_read_time
                }
            else:
                bookinfo['level'] = book.level

            bookinfos.append(bookinfo)
        if not isManager:
            bookinfos = sorted(
                bookinfos, key=lambda x: x['progress']['latest_read_time'], reverse=True)
        return Response(bookinfos)

    @manager_required
    def post(self, request):
        '''
        Add or update book info
        '''
        postdata = json.loads(request.body)
        book_id = int(postdata.get('id'))
        cover = postdata.get('cover')
        level = postdata.get('level')
        title = postdata.get('title')
        assignment = postdata.get('assignment')
        pages_num = postdata.get('pages_num')
        read_type = postdata.get('read_type')
        guidance = postdata.get('guidance')
        if book_id == -1:
            book = Book.objects.create(
                cover=cover,
                level=level,
                title=title,
                pages_num=pages_num,
                assignment=assignment,
                guidance=guidance,
                read_type=read_type)
        else:
            book = get_book(id=book_id)[0]
            if cover:
                book.cover = cover
            if level:
                book.level = level
            if title:
                book.title = title
            if assignment:
                book.assignment = assignment
            if pages_num:
                book.pages_num = pages_num
            if read_type:
                book.read_type = read_type
            if guidance:
                book.guidance = guidance
            book.save()
        return Response(BookSerializer(book).data, status=201)

class BookGuidance(APIView):

    def get(self, request, book_id):
        '''
        List guidance of a book.
        '''
        book_data = get_book(id=book_id)
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

    @manager_required
    def post(self, request, book_id):
        book_query = get_book(id=book_id)
        postdata = json.loads(request.body)
        response_info = {}
        book = book_query[0]
        guidance = postdata.get('guidance')
        book.guidance = guidance
        book.save()
        response_info['guidance'] = book.guidance
        words = postdata.get('words')
        Word.objects.filter(guidance=book).delete()

        response_info['words'] = []
        for word in words:
            word_created = Word.objects.create(
                guidance=book,
                word=word['word'],
                meaning=word['meaning'])
            response_info['words'].append({
                'word': word_created.word,
                'meaning': word_created.meaning
            })
        return Response(response_info, status=201)

class BookHomework(APIView):

    def get(self, request, book_id):
        '''
        stu:GET User homework
        manager:Only get homework assignment
        '''

        book = get_book(id=book_id)[0]

        if not is_admin(request.user):
            student = Student.objects.get(user=request.user)

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
        else:
            homework_info = {'assignment': book.assignment}

        return Response(homework_info)

    def post(self, request, book_id):
        '''
        Student: upload user homework
        Manager: Update book assignment
        '''
        book = get_book(id=book_id)[0]
        postdata = json.loads(request.body)
        if not is_admin(request.user):
            student = Student.objects.get(user=request.user)
            progress = Progress.objects.get_or_create(user=student, book=book)[0]
            progress.punched = True
            progress.save()
            try:
                homework = Homework.objects.get(book=book, author=student)
            except ObjectDoesNotExist:
                homework = Homework.objects.create(book=book, author=student, content=' ')
            homework.content = postdata.get('content', ' ')
            attachments = postdata.get('attachments',r'{}')
            homework.images = ' '.join(attachments.get('image', ''))
            homework.videos = ' '.join(attachments.get('video', ''))
            homework.audios = ' '.join(attachments.get('audio', ''))
            homework.save()
            return Response(status=201)
        else:
            book.assignment = postdata.get('assignment')
            return Response({
                'id': book.id,
                'assignment': book.assignment
            }, status=201)


class BookProgress(APIView):

    @stu_required
    def post(self, request, book_id):
        postdata = json.loads(request.body)
        book = get_book(id=book_id)[0]
        student = Student.objects.get(user=request.user)
        try:
            progress = Progress.objects.get(user=student, book=book)
            progress.current_page = postdata.get('current_page', progress.current_page)
            progress.latest_read_time = timezone.now()
            progress.save()
        except ObjectDoesNotExist:
            Progress.objects.create(user=student, book=book, current_page=postdata.get('current_page',0))
        update_student_score(student)
        return Response(status=201)


class UserProgress(APIView):
    @manager_required
    def get(self, request, user_id):
        stu_query = Student.objects.filter(id=user_id)
        if not stu_query.exists():
            return Response({
                'msg': 'Student(id={}) mot exists.'.format(user_id)
            }, status=404)
        stu = stu_query[0]
        progress_infos = []
        progress_query = Progress.objects.filter(user=stu)
        for progress in progress_query:
            homework_id = -1
            homework_query = Homework.objects.filter(author=stu,
                                                    book=progress.book)
            if homework_query.exists():
                homework_id = homework_query[0].id
            progress_info = {

                'id': progress.id,
                'level': progress.book.level,
                'cover': progress.book.title,
                'pages_num': progress.book.pages_num,
                'homework': homework_id,
                'progress': {
                    'current_page': progress.current_page,
                    'punched': progress.punched,
                    'latest_read_time': progress.latest_read_time
                },
                'type': progress.book.read_type,
            }
            progress_infos.append(progress_info)
        return Response(progress_infos)

class UserHomework(APIView):
    @manager_required
    def get(self, request, homework_id):
        homework_query = Homework.objects.filter(id=homework_id)
        if not homework_query.exists():
            return Response({
                'msg': 'Homework(id={}) not found'.format(homework_id)
            }, status=404)
        homework = homework_query[0]
        return Response({
            'content': homework.content,
            'attachments': {
                'image': homework.images.split(),
                'video': homework.videos.split(),
                'audio': homework.audios.split(),
            }
        })


class BookEbook(APIView):

    def get(self, request, book_id):
        get_book(id=book_id)
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

    @manager_required
    def post(self, request, book_id):
        book = get_book(id=book_id)[0]
        postdata = json.loads(request.body)
        book.pages_num = len(postdata)
        book.save()
        old_pages = Page.objects.filter(book=book)
        if old_pages.exists():
            old_pages.delete()
        for page in postdata:
            number = get_or_raise(page, 'number')
            picture = get_or_raise(page, 'picture')
            sentences = page.get('sentences')
            newpage = Page.objects.get_or_create(book=book,
                                            number=number,
                                            picture=picture)[0]
            if Sentence.objects.filter(page=newpage).exists():
                Sentence.objects.filter(page=newpage).delete()
            if sentences:
                for sentence_info in sentences:
                    Sentence.objects.create(
                        page=newpage,
                        content=get_or_raise(sentence_info, 'content'),
                        audio=get_or_raise(sentence_info, 'audio'),
                        translated=get_or_raise(sentence_info, 'translated'),
                        x1=get_or_raise(sentence_info, 'x1'),
                        y1=get_or_raise(sentence_info, 'y1'),
                        x2=get_or_raise(sentence_info, 'x2'),
                        y2=get_or_raise(sentence_info, 'y2')
                    )
        return Response(status=201)


class CommunityGroup(APIView):

    @stu_required
    def get(self, request):
        community_info = []
        student = Student.objects.get(user=request.user)
        level = student.level
        moments = Moment.objects.filter(level=level)
        if moments:
            for moment in moments:
                community_message = {}
                homework = moment.homework
                community_message['id'] = moment.id
                community_message['author'] = {}
                community_message['author']['username'] = homework.author.nickname
                community_message['author']['avatar'] = homework.author.avatar
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

    @stu_required
    def post(self, request):
        postdata = json.loads(request.body)
        book_id = get_or_raise(postdata, 'book')
        book = get_book(id=book_id)[0]
        student = Student.objects.get(user=request.user)
        homework_query = Homework.objects.filter(author=student, book=book)
        if not homework_query.exists():
            raise NotFound('Homework for book(id={}) not found.'.format(book_id))
        homework = homework_query[0]
        level = student.level
        moment_query = Moment.objects.filter(homework=homework, level=level)
        if moment_query.exists():
            return Response({'msg': 'Cannot punch more than once.'}, status=403)
        Moment.objects.create(homework=homework, level=level)
        return Response(status=201)

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


class LikeAction(APIView):
    @stu_required
    def post(self, request, moment_id):
        stu = Student.objects.get(user=request.user)
        moment_query = Moment.objects.filter(id=moment_id)
        if not moment_query.exists():
            return Response({
                'msg': 'Moment(id={}) not found.'.format(moment_id)
            }, status=404)
        moment = moment_query[0]
        like_query = Like.objects.filter(actor=stu, target=moment)
        if not like_query.exists():
            Like.objects.create(actor=stu, target=moment)
            moment.vote_count += 1
        else:
            moment.vote_count -= len(like_query)
            like_query.delete()
        moment.save()
        return Response({
            'vote_count': moment.vote_count
        })

class UserInfo(APIView):

    @stu_required
    def get(self, request):

        student = Student.objects.get(user=request.user)
        nickname = student.nickname if student.nickname else request.user.username
        avatar = student.avatar
        level = student.level

        userinfo = {
            'nickname': nickname,
            'avatar': avatar,
            'level': level
        }

        return Response(userinfo)

    @stu_required
    def post(self, request):
        postdata = json.loads(request.body)
        student = Student.objects.get(user=request.user)
        student.nickname = postdata.get('nickname', student.nickname)
        student.avatar = postdata.get('avatar', student.avatar)
        student.save()
        return Response(status=201)

class ChangePassword(APIView):

    def post(self, request):
        user = request.user
        password = json.loads(request.body).get('password')
        self.verify_password(password)
        user.set_password(password)
        user.save()
        return Response(status=200)

    def verify_password(self, password):
        if not password:
            raise ParseError(detail='Password cannot be empty.')
        if len(password)<8:
            detail = 'This password is too simple or too young'
            raise ParseError(detail=detail)

class NoticeInfo(APIView):

    def get(self, request):
        if not is_admin(request.user):
            student = Student.objects.get(user=request.user)
        notice_infos = []
        notices = Notice.objects.all()
        if notices.exists():
            for notice in notices:
                notice_info = {}
                notice_info['id'] = notice.id
                notice_info['content'] = notice.content
                if not is_admin(request.user):
                    notice_info['have_read'] = IsNoticeReaded.objects.filter(notice=notice, student=student).exists()
                notice_info['created_time'] = notice.created_time
                notice_infos.append(notice_info)

        return Response(notice_infos)

    @manager_required
    def post(self, request):
        postdata = json.loads(request.body)
        content = get_or_raise(postdata, 'content')
        notice = Notice.objects.create(content=content)
        return Response({
            'id': notice.id
        }, status=201)

class NoticeAction(APIView):
    @manager_required
    def delete(self, request, notice_id):
        notice_query = Notice.objects.filter(id=notice_id)
        if notice_query.exists():
            notice_query.delete()
            return Response(status=200)
        else:
            return Response({
                'msg': 'Notice(id={}) not found.'.format(notice_id)
            }, status=404)


class MarkNotice(APIView):

    @stu_required
    def post(self, request):
        postdata = json.loads(request.body)
        notice_id = get_or_raise(postdata, 'id')
        notice_query = Notice.objects.filter(id=notice_id)
        if not notice_query.exists():
            return Response({'msg': 'Notice not found'}, status=404)
        notice = notice_query[0]
        student = Student.objects.get(user=request.user)
        IsNoticeReaded.objects.get_or_create(notice=notice, student=student)
        return Response(status=201)


class StudentList(APIView):

    @manager_required
    def get(self, request):

        student_list = []
        students_query = Student.objects.all()
        if students_query.exists():
            for student in students_query:
                info = {}
                info['id'] = student.id
                info['username'] = student.user.username
                info['level'] = student.level
                info['nickname'] = student.nickname
                info['score'] = student.score
                student_list.append(info)
        return Response(student_list)


class KeyGenerator(APIView):

    @manager_required
    def post(self, request):
        postdata = json.loads(request.body)
        level = int(postdata.get('level'))
        count = int(postdata.get('count'))
        keys = []

        for _ in range(count):
            key = self.getRandomKey()
            while ActiveKey.objects.filter(key=key).exists():
                key = self.getRandomKey()
            ActiveKey.objects.create(level=level, key=key)
            keys.append(key)

        return Response(keys, status=201)

    def getRandomKey(self, size=18):
        alphas = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(alphas) for _ in range(size))

class RankList(APIView):

    @stu_required
    def get(self, request):
        level = Student.objects.get(user=request.user).level
        students = Student.objects.filter(level=level).order_by('-score')
        rank_list = []
        for stu in students:
            stu_info = {
                'nickname': stu.nickname,
                'avatar': stu.avatar,
                'score': stu.score
            }
            if not stu_info['nickname']:
                stu_info['nickname'] = stu.user.username
            rank_list.append(stu_info)
        return Response(rank_list)

class UserLevel(APIView):

    @stu_required
    def get(self, request):
        stu = Student.objects.get(user=request.user)
        return Response(num_to_bit(stu.accept_level))

    @stu_required
    def post(self, request):
        stu = Student.objects.get(user=request.user)
        postdata = json.loads(request.body)
        level = get_or_raise(postdata, 'level')
        accept_level = stu.accept_level
        if bit_to_num(level)&accept_level:
            stu.level = level
            stu.save()
            return Response(status=200)
        else:
            return Response({'msg': '没有当前级别的权限'}, status=401)


class UserData(APIView):
    def activity(self):
        time_list = [(x.user.id, x.latest_read_time)
                     for x in Progress.objects.all()]
        student_activity = {}
        for (user, time) in time_list:
            if user not in student_activity:
                student_activity[user] = time
            else:
                if student_activity[user] > time:
                    student_activity[user] = time
        data = list(student_activity.values())
        result = {}
        now = timezone.now()
        last_day = now - timedelta(days=1)
        last_week = now - timedelta(days=7)
        last_month = now - timedelta(days=30)
        result['day'] = len(list(filter(lambda time: time > last_day, data)))
        result['week'] = len(list(filter(lambda time: time > last_week, data)))
        result['month'] = len(list(filter(lambda time: time > last_month, data)))
        return result

    def level(self):
        result = {}
        for level in range(1, 10):
            result[level] = len(Student.objects.filter(level=level))
        return result

    def book(self):
        result = {}
        for level in range(1, 10):
            result[level] = len(Book.objects.filter(level=level))
        return result

    def get(self, request):
        result = {}
        result['all_user'] = len(Student.objects.all())
        result['activity_user'] = self.activity()
        result['level_user'] = self.level()
        result['level_book'] = self.book()
        return Response(result)


class UserLevelUpdate(APIView):

    @stu_required
    def post(self, request):
        stu = Student.objects.get(user=request.user)
        postdata = json.loads(request.body)
        key = get_or_raise(postdata, 'code')
        key_query = ActiveKey.objects.filter(key=key)
        if not key_query.exists():
            return Response({'msg': '激活码无效'}, status=400)
        new_level = key_query[0].level
        stu.accept_level |= bit_to_num(new_level)
        stu.save()
        key_query.delete()
        return Response({'level': new_level})


class MatchingGameView(APIView):
    def get(self, request, book_id):
        book = get_book(id=book_id)[0]
        games = MatchingGame.objects.filter(book=book)
        if len(games) == 0:
            content = {'msg': '当前游戏未导入'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        else:
            response_data = []
            for data in games:
                response_data.append({
                    'img': data.img,
                    'word': data.word
                })
            return Response(response_data)

    @manager_required
    def post(self, request, book_id):
        book = get_book(id=book_id)[0]
        post_data = json.loads(request.body)
        MatchingGame.objects.filter(book=book).delete()
        for data in post_data:
            MatchingGame.objects.create(
                book=book,
                img=get_or_raise(data, 'img'),
                word=get_or_raise(data, 'word')
            )
        return Response(status=201)


class JigsawGameView(APIView):
    def get(self, request, book_id):
        book = get_book(id=book_id)[0]
        games = JigsawGame.objects.filter(book=book)
        if len(games) == 1:
            content = {'msg': '当前游戏未导入'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        response_data = {}
        for data in games:
            response_data[data.num] = data.img
        return Response(response_data)

    @manager_required
    def post(self, request, book_id):
        book = get_book(id=book_id)[0]
        post_data = json.loads(request.body)
        JigsawGame.objects.filter(book=book).delete()
        for num in range(1,10):
            if num in post_data:
                MatchingGame.objects.create(
                    book=book,
                    num=num,
                    img=get_or_raise(post_data, num)
                )
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=201)


class RecognitionGameView(APIView):
    def get(self, request, book_id):
        book = get_book(id=book_id)[0]
        games = RecognitionGame.objects.filter(book=book)
        if len(games) == 1:
            return Response({
                'img': games[0].img,
                'correct_word': games[0].correct_word,
                'wrong_word_1': games[0].wrong_word_1,
                'wrong_word_2': games[0].wrong_word_2,
            })
        else:
            content = {'msg': '当前游戏未导入'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    @manager_required
    def post(self, request, book_id):
        book = get_book(id=book_id)[0]
        data = json.loads(request.body)
        RecognitionGame.objects.filter(book=book).delete()
        RecognitionGame.objects.create(
            book=book,
            img=get_or_raise(data, 'img'),
            correct_word=get_or_raise(data, 'correct_word'),
            wrong_word_1=get_or_raise(data, 'wrong_word_1'),
            wrong_word_2=get_or_raise(data, 'wrong_word_2'),
        )
        return Response(status=201)


class ClozeGameView(APIView):
    def get(self, request, book_id):
        book = get_book(id=book_id)[0]
        games = ClozeGame.objects.filter(book=book)
        if len(games) == 1:
            return Response({
                'sentence': games[0].sentence,
                'corerct_word': games[0].correct_word,
                'wrong_word_1': games[0].wrong_word_1,
                'wrong_word_2': games[0].wrong_word_2,
                'wrong_word_3': games[0].wrong_word_3,
            })
        else:
            content = {'msg': '当前游戏未导入'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


    @manager_required
    def post(self, request, book_id):
        book = get_book(id=book_id)[0]
        data = json.loads(request.body)
        ClozeGame.objects.filter(book=book).delete()
        ClozeGame.objects.create(
            book=book,
            sentence=get_or_raise(data, 'sentence'),
            correct_word=get_or_raise(data, 'corerct_word'),
            wrong_word_1=get_or_raise(data, 'wrong_word_1'),
            wrong_word_2=get_or_raise(data, 'wrong_word_2'),
            wrong_word_3=get_or_raise(data, 'wrong_word_3'),
        )
        return Response(status=201)

@csrf_exempt
def register_view(request):
    if request.method == 'GET':
        return JsonResponse({'msg': 'Method "GET" not allowed.'}, status=405)
    postdata = json.loads(request.body)
    username = postdata.get('username')
    password = postdata.get('password')
    key = postdata.get('key')
    key_query = ActiveKey.objects.filter(key=key)
    if not key_query.exists():
        return JsonResponse({'msg': '激活码无效'}, status=403)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'msg': '用户名已被注册'}, status=403)
    level = key_query[0].level
    key_query.delete()
    user = User.objects.create_user(username=username, password=password)
    Student.objects.create(user=user, level=level, accept_level=bit_to_num(level), avatar='')
    return JsonResponse({'msg': '注册成功'}, status=201)

@csrf_exempt
def manager_token(request):
    if request.method=='GET':
        return JsonResponse({'msg': 'Method "GET" not allowed.'}, status=405)
    postdata = json.loads(request.body)
    username = get_or_raise(postdata, 'username')
    password = get_or_raise(postdata, 'password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if is_admin(user):
            return JsonResponse({
                'token': Token.objects.get(user=user).key
            })
        else:
            return JsonResponse({
                'msg': 'You are not a manager.'
            }, status=403)
    else:
        return JsonResponse({'msg': 'Username or password incorrect.'}, status=403)
