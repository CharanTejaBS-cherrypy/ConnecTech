from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Community, Membership, Message
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Idea
from .forms import PostForm, IdeaForm





@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community_list.html', {'communities': communities})


def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    messages = Message.objects.filter(community=community)
    is_member = request.user.is_authenticated and Membership.objects.filter(
        user=request.user, community=community).exists()
    return render(request, 'community_detail.html', {'community': community, 'messages': messages, 'is_member': is_member})


@login_required
def join_community(request, pk):
    community = get_object_or_404(Community, pk=pk)
    Membership.objects.get_or_create(user=request.user, community=community)
    return redirect('community_detail', pk=pk)


@login_required
def leave_community(request, pk):
    community = get_object_or_404(Community, pk=pk)
    Membership.objects.filter(user=request.user, community=community).delete()
    return redirect('home')


@csrf_exempt
@login_required
def send_message(request, pk):
    if request.method == 'POST':
        community = get_object_or_404(Community, pk=pk)
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                user=request.user, community=community, content=content)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)


def index(request):
    return render(request, 'welcome.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def home(request):
    ideas = Idea.objects.all()
    communities = Community.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IdeaForm()
    return render(request, 'home.html', {'communities': communities, 'posts': posts, 'ideas': ideas, 'form': form})


def idea_detail(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    # if request.method == 'POST':
    #     send_mail(
    #         'Collaboration Request',
    #         f'I am interested to work on {idea.title} project with you.',
    #         'from@example.com',
    #         [idea.email],
    #         fail_silently=False,
    #     )
    #     return redirect('home')
    return render(request, 'idea_detail.html', {'idea': idea})

def contrib(request):
    return redirect('https://charantejabs-cherrypy.github.io/ConnecTech-Contributors/')