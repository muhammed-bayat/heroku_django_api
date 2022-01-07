from django.shortcuts import render,HttpResponse

from .models import Article, Experiment, Category
from .serializers import ArticleSerializer, ExperimentSerializer, CategorySerializer, ExperimentDetailSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class ArticleViewsets(viewsets.ViewSet):
    
    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    
    def create(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        queryset = Article.objects.all()
        article=get_object_or_404(queryset,pk=pk) 
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
        

class ArticleList (generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
    
    def delete(self,request):
        return self.destroy(request)
"""
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
class ArticleDetails (generics.GenericAPIView,mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
    
    def get(self,request,pk):
        return self.retrieve(request,pk=pk)

    def put(self, request, pk):
        return self.update(request,pk=pk)
    
    def delete(self, request, pk):
        return self.destroy(request,pk=pk)
    


   
"""
@api_view(['GET', 'PUT', 'DELETE'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response()(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response()(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
         
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()(serializer.data)
        return Response()(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response()(status=status.HTTP_204_NO_CONTENT)
"""




class ExperimentListView(generics.ListAPIView):
    serializer_class = ExperimentDetailSerializer

    def get_queryset(self):
        queryset = Experiment.objects.filter(category_id=self.kwargs['pk'])
        return  queryset
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset =  Category.objects.all()

class ExperimentDetailView(generics.RetrieveAPIView):
    serializer_class = ExperimentDetailSerializer
    def get_object(self):
        experiments = get_object_or_404(Experiment, pk=self.kwargs['pk'])
        return experiments
