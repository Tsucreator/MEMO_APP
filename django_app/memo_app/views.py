from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import PostForm, RecordNumberForm, SortForm
from .models import *
from django.core.paginator import Paginator

def index(request, now_page=1):

    #レコードの件数
    if 'record_number' in request.session:
        record_number = request.session['record_number']
    else: 
        record_number = 10
    
    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    #ソートのold,new
    if 'order_option' in request.session:
        order_option = request.session['order_option']
    else:
        order_option = 'new'
    
    order_option_form = SortForm()
    order_option_form.initial ={'order_option': str(order_option)}

    #変数と格納
    if order_option == 'new':
        memos = Memo.objects.all().order_by('update_datetime').reverse()
    else:
        memos = Memo.objects.all().order_by('update_datetime')
    page = Paginator(memos, record_number)
    params = {
        'page': page.get_page(now_page),
        'form': PostForm(),
        'record_number_form': record_number_form,
        'order_option_form': order_option_form,
}
    return render(request, 'index.html', params)

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/')

#セッションに格納
#表示件数
def set_record_number(request):
    request.session['record_number'] = request.POST['record_number']
    return redirect(to='/')

#ソート
def set_order_option(request):
    request.session['order_option'] = request.POST['order_option']
    return redirect(to='/')

#Create your views here.
