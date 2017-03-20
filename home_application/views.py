# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse('ok')

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

"""
第一个app
"""
from forms import AddForm


# def index(request):
#     if request.method == 'POST':
#         form = AddForm(request.POST)
#         ask = form.cleaned_data['ask']
#         answer = form.cleaned_data['answer']
#         m_ask = md5sum(ask)
#         m_answer = md5sum(answer)
#         fileMd5(ask=ask, answer=answer, ask_md5=m_ask, answer_md5=m_answer).save()
#         return render_to_response('home_application/123.html',m_ask,m_answer)
#     else:
#         form = AddForm()
#         return render_to_response('home_application/123.html',{'form': form})
#
#
#
# import hashlib
# def md5sum(text):
#     m = hashlib.md5()
#     m.update(text)
#     return m.hexdigest()
#
#
# from django.http import HttpResponse
# from models import fileMd5
#
#
# def returnMd5(request):
#     ask = request.GET['ask']
#     answer = request.GET['answer']
#
#     fileMd5(ask=ask, answer=answer, ask_md5=m_ask, answer_md5=m_answer).save()

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home_application/index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))






