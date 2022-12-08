#Ce projet a été réalisé par:
# - NDOUR Ndeye Aida
# - DJAKOPO Abiola David
# - BALDE Mamadou Saliou
# - BISSOMBOLO Siega
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from bibliotheque.models import Book
from bibliotheque.serializers import BookSerializer
from rest_framework.decorators import api_view
# Create your views here.
from django.http import HttpResponse

@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':  
        bibliotheque = Book.objects.all()
        
        titre = request.GET.get('titre', None)
        if titre is not None:
            bibliotheque = bibliotheque.filter(title__icontains=titre)
        
        book_serializer = BookSerializer(bibliotheque, many=True)
        return JsonResponse(book_serializer.data, safe=False)

    #POST Book
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete
    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} Book were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    # ... tutorial = Tutorial.objects.get(pk=pk)
    # ...
    try: 
        book = Book.objects.get(pk=pk) 
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        book_data = JSONParser().parse(request) 
        book_serializer = BookSerializer(book, data=book_data) 
        if book_serializer.is_valid(): 
            book_serializer.save() 
            return JsonResponse(book_serializer.data) 
    


# @api_view(['GET', 'PUT', 'DELETE','POST'])
# def book_detail(request,pk):
#     # GET book
#     if request.method == 'GET':       
#         book_serializer = BookSerializer(Book)
#         return JsonResponse(book_serializer.data)
#         # 'safe=False' for objects serialization
#     #put book
#     elif request.method == 'PUT': 
#         book_data = JSONParser().parse(request) 
#         book_serializer = BookSerializer(Book, data=book_data) 
#         if book_serializer.is_valid(): 
#             book_serializer.save() 
#             return JsonResponse(book_serializer.data) 
#         return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     #DELETE book
#     elif request.method == 'DELETE': 
#         Book.delete() 
#         return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
# #post book
# @api_view(['POST'])
# def book_list(request):
#     #POST Book
#     if request.method == 'POST':
#         book_data = JSONParser().parse(request)
#         book_serializer = BookSerializer(data=book_data)
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def home(request):
#     return HttpResponse("Hello, Django!")
