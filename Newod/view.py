from django.http import HttpResponse #主要以字符串的形式传递数据
from django.template import Template,Context    #Cont ext的操作和dict类似，Template只能接收字符串的形式，不能接收文件，
from django.template.loader import get_template # get_template可以接收文件
from django.shortcuts import render
from django.views import View

from datetime import datetime


def hello(request,bookid):
    return HttpResponse("hello world" + str(bookid))


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>it is now %s </body></html>"% now
    return HttpResponse(html)


def sendemail(request):
    #t = Template("sendemail.html")#这样的写法是错误的
    # t = get_template("sendemail.html")
    # c = Context({'person_name': "张浩",
    #              'product': 'Super Lawn Mower',
    #              'company': 'Outdoor Equipment',
    #              'ship_date': datetime.now(),
    #              'ordered_warranty': True})
    # html = t.render(c) #这样传递，由于版本的问题，会倒错 context must be a dict rather than Context. 解决https://blog.csdn.net/u014770372/article/details/76038248
    # return HttpResponse(html)

    return render(request,"sendemail.html",{'person_name': "张浩",#标准的返回状态
                             'product': 'Super Lawn Mower',
                             'company': 'Outdoor Equipment',
                             'ship_date': datetime.now(),
                             'ordered_warranty': True})


class Index(View):
    def get(self,request):
        return render(request,"index.html")


