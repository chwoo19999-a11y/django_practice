# polls/views.py에 간단한 뷰 작성
from django.http import HttpResponse

# 장고 페이지 구성의 핵심
from django.shortcuts import render
from .models import Article, Memo

# index에서 context 만들어서 보내기기
def index(request):
    memos = Memo.objects.all()
    context = {
        "name":"lion",
        "title":"장고 학습",
        "memos":memos
    }
    return render(request=request, template_name="mypolls/index.html", context=context)

def lion(request, name):
    return HttpResponse(f"""{name}가 장고를 배웁니다!!""")

def dubug_request(request):
    # request 의 메서드와
    # request 의 path
    # request 의 META.REMOTE_ADDR를 화면에 표시하자!!
    content = f"""이것이 request가 가지고 있는 정보의 예시입니다.<br>
    request.path = {request.path}    <br>
    request.method = {request.method}    <br>
    request.META.REMOTE_ADDR = {request.META.get('REMOTE_ADDR', 'Unknown')}    <br>
    """
    return HttpResponse(content)

def memo_list(request):  # ✅ self -> request로 수정
    # 메모 전체 가져오기
    all_memo = Memo.objects.all()
    # content 구성하기
    content = ""
    for memo in all_memo:
        content += "제목 : " + memo.title + "<br>"
        content += "내용 : " + memo.content + "<br>"
        content += "----" * 10
        content += "<br>"
    return HttpResponse(content)

def one_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    content = f"""<h1>제목 : {memo.title}</h1> <br><br> 
    내용 : {memo.content}<br>
    {memo.is_important}<br>
    {memo.created_at}
    """
    return HttpResponse(content)