from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from frontend_app.models import Blog,BlogSerializer
@api_view()
def main_api(request):
    data = {
        "List_blog":"blog_list",
        "Detail_blog":"blog-detail/<id>",
        "Create-blog":"blog-create",
        "Delete_blog":"blog-delete/<id>",
        "Update_blog":"blog-update/<id>",
    }
    return Response({"api":data})

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    bls = BlogSerializer(blogs,many=True)
    return Response(bls.data)

@api_view(['GET'])
def blog_detail(request,id):
    blogs = Blog.objects.get(id=id)
    blogser = BlogSerializer(blogs,many=False)
    return Response(blogser.data)

@api_view(['POST'])
def blog_create(request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['POST'])
def blog_update(request,id):
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(instance=blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['DELETE'])
def blog_delete(request,id):
        blog = Blog.objects.get(id=id)
        blog.delete()
        return Response({"message":"Object deleted"})
