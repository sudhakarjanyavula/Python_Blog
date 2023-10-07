from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import *

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
#         serializer.save()
#         user = User.objects.get(username=serializer.data['username'])
#         token_obj, _ = Token.objects.get_or_create(user=user)
#         return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj), 'message': 'Your details are saved'})