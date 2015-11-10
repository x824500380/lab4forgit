# -*- coding: utf-8 -*-
from django.shortcuts import render
from library.models import Author
from library.models import Book
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def index(request):
	return render_to_response('index.html')

def library(request):
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	is_click = False
	return render_to_response('library.html',{'AuthorList':lis,'BookList':lis2,"is_click":is_click})

def booklist(request):
	booklist = Book.objects.all()
	return render_to_response('booklist.html',{'booklist':booklist})	
    

def addbook0(request):
	return render_to_response('addbook.html')
def addbook(request):
	title = request.POST['book_name']
	#ISBN = request.POST['book_ISBN']
	authorID = request.POST['book_authorID']
	publisher = request.POST['book_publisher']
	publishdate = request.POST['book_date']
	price = request.POST['book_price']
	try:
		author = Author.objects.get(AuthorID=authorID)
		BOOK = Book()
		BOOK.ISBN = request.POST['book_ISBN']
		BOOK.Title = title
		BOOK.AuthorID = author
		BOOK.Publisher =  publisher
		BOOK.Publishdate = publishdate
		BOOK.Price = float(price)
		BOOK.save()
		return render_to_response('bookinformation.html',{'booktest':BOOK})
	except Author.DoesNotExist:
		return render_to_response('addwriter.html')   

def addwriter0(request):
    return render_to_response('addwriter.html')
def addwriter(request):
	AUTHOR = Author()
	AUTHOR.AuthorID = request.POST['author_ID']
	AUTHOR.Age = request.POST['author_age']
	AUTHOR.Country = request.POST['author_country']
	AUTHOR.Name = request.POST['author_name']
	AUTHOR.save()
	AuthorList = Author.objects.all()
	return render_to_response('addbook.html') 


def serchbook0(request):
	return render_to_response('serchbook.html')
def serchbook(request):
	word = request.POST['bookname']
	try:
		BookAim = Book.objects.get(Title = word)
	except Book.DoesNotExist:
		return render_to_response('addbook.html')
	else:
		return render_to_response('bookinformation.html',{'booktest':BookAim})


def serchwriter0(request):
    return render_to_response('serchwriter.html')

def serchwriter(request):
	word = request.POST['authorname']
	try:
		AuthorAim = Author.objects.get(Name = word)
		AuthorBooks = AuthorAim.book_set.all()	
		return render_to_response('library.html',{'Authors':AuthorAim,'AuthorBooks':AuthorBooks})  
	except Author.DoesNotExist:
		return render_to_response('addwriter.html') 


def DelBook(request,key):
	Aim = Book.objects.get(ISBN=key)
	Aim.delete()
	return  HttpResponseRedirect("/booklist")

def UpdateBook(request):
	Aim = Book.objects.get(ISBN=request.POST['update'])
	BookAuthor = Author.objects.get(AulthorID=Aim.AulthorID_id)
	return render_to_response('addbook.html',{'book':Aim,'author':BookAuthor})

def UpdateBook2(request):
	publisher = request.POST['book_publisher']
	date = request.POST['book_date']
	price = request.POST['book_price']
	Aim = Book.objects.get(ISBN=request.POST['book_ISBN'])
	Aim.Publisher =  publisher
	Aim.PublishDate = date
	Aim.Price = float(price)
	Aim.save()
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	return render_to_response('library.html',{'AuthorList':lis,'BookList':lis2})

def information(request):
	is_click = True
	AuthorAim = Author.objects.get(AuthorID = request.POST['author_ID'])
	AuthorBooks = AuthorAim.book_set.all()
	return render_to_response("library.html",{"is_click":is_click,"book1":Book.objects.get(ISBN=request.POST['book_ISBN']),'Authors':AuthorAim,'AuthorBooks':AuthorBooks})