from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from rest_framework import viewsets

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AutorView(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        autors=[]
        for autor in self.queryset:
            articles=Article.objects.filter(autor=autor.id)
            art=[]
            for a in articles:
                article ={
                    'name':a.name
                }
                art.append(article)
            d={
                'id':autor.id,
                'level':autor.level,
                'faculty':autor.faculty,
                'cafedra':autor.cafedra,
                'image':autor.imageURL,
                'reg_time':autor.reg_time,
                'user':autor.user.username,
                'articles':art
            }
            autors.append(d)
        return Response({'autors':autors})

        # for autor in serializer.data:
        #     articles=Article.objects.filter(autor=autor['id'])
        #     art=[]
        #     for a in articles:
        #         article ={
        #             'name':a.name
        #         }
        #         art.append(article)
        #     d={
        #         'id':autor['id'],
        #         'level':autor['level'],
        #         'faculty':autor['faculty'],
        #         'cafedra':autor['cafedra'],
        #         'image':autor['image'],
        #         'reg_time':autor['reg_time'],
        #         'user':autor['user'],
        #         'articles':art
        #     }
        #     autors.append(d)
        # return Response({'autors':autors})


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        datas=[]
        for i in serializer.data:
            files=LinkedFiles.objects.filter(article=i['id'])
            f=[]
            for file in files:
                ff={
                    'url': file.fileURL
                }
            f.append(ff)
            d={
                'id':i['id'],
                'name':i['name'],
                'text': i['text'],
                'tags':i['tags'],
                'autor':i['autor'],
                'files':f

            }
            datas.append(d)

        return Response({'datas':datas})
        # return Response(serializer.data)
        # return Response({'data': 'bori shu.....'})  # serializer.data)
class ArticleByTagView(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer
    def retrieve(self, request, *args, **kwargs):
        tag=kwargs['pk']
        print(tag)
        articles=self.queryset.filter(tags__contains=tag)
        print(articles)
        data =[]
        for article in articles:
            d={
                'id':article.id,
                'name':article.name,
                'text':article.text,
                'tags':article.tags,
                'autor':article.autor.id
            }
            data.append(d)
        return Response({'data':data})


class FileView(viewsets.ModelViewSet):
    queryset = LinkedFiles.objects.all()
    serializer_class = FilesSerializer

