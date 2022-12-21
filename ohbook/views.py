from django.shortcuts import render, redirect
from ohbook.models import Article
from ohbook.models import Comment

def index(request):
    articles = Article.objects.all()
    return render(request, 'ohbook/base.html', { 'articles': articles })
    

def play(request):
    return render(request, 'ohbook/play.html')


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('author'),
            text=request.POST.get('text'),
            password=request.POST.get('password')
        )
        return redirect(f'/feed/{ article.pk }')

    return render(request, 'ohbook/detail_feed.html', {'feed': article})

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - 추신: 감사합니다.'

            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )

            # 새글 등록 끝
            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'ohbook/new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기

    return render(request, 'ohbook/remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')

        else:
            return redirect('/fail/')  # 비밀번호 오류 페이지 이동하기


    return render(request, 'ohbook/edit_feed.html', {'feed': article})

def fail(request):
    return render(request, 'ohbook/fail.html')