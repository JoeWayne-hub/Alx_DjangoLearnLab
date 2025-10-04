from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def register_view(request):
    """
    Handle user registration. On POST with valid form create user and log them in.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {"form": form})


@login_required
def profile_view(request):
    """
    Display profile details; allow POST to edit profile.
    """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {"form": form, "profile": profile})

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # templates/blog/post_list.html
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10  # optional

# Detail view (public)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # templates/blog/post_detail.html
    context_object_name = "post"

# Create (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"  # templates/blog/post_form.html

    def form_valid(self, form):
        # set the logged-in user as author
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update (only the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

# Delete (only the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
