from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    """
    Extends UserCreationForm to include an email field (required).
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    """
    Form for editing profile info (bio and profile image).
    """
    class Meta:
        model = Profile
        fields = ("bio", "profile_image")



class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Add tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        

        widgets = {
            'tags': TagWidget(),
         }


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # handle tags
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [name.strip() for name in tags_str.split(',') if name.strip()]
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            instance.tags.add(tag)
        return instance