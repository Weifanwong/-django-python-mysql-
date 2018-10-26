from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post,Category,Tag
from django.db.models.aggregates import Count
from pure_pagination import PageNotAnInteger,Paginator

def index(request):
	return HttpResponse('hello')

def index2(request):
	post_list = Post.objects.all().order_by('created_time')
	category_list = Category.objects.annotate(num_posts=Count('post'))
	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1
	p = Paginator(post_list, 4, request=request)  #5为每页展示的博客数目
	post_list = p.page(page)

	return render(request,'index.html',{'post_list':post_list,'category_list':category_list})

def detail(request,pk):
 post = get_object_or_404(Post,pk=pk)
 return render(request,'detail.html',{'post':post})

def biology(request):
	return render(request,'biology.html')

def get(request, category_name):
	list_blog = Post.objects.filter(category=category_name).all()
	
	return render(request, 'category-detail.html', {
            'list_blog': list_blog,
        })