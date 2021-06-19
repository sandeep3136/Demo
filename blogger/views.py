from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def index(request):
    return render(request, "blogger/viewpost.html")

class NewPostForm(forms.Form):
    post_title = forms.CharField(label='newpost')
    post_author = forms.CharField(label='authon')
    post_image = forms.ImageField()
    post_content = forms.CharField(widget=forms.Textarea)

def addPosts(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["newpost"]
            
        else:
            return render(request, "blogger/addpost.html", {"form": NewPostForm()})
    return render(request, "blogger/addpost.html", {"form": NewPostForm()})
    
def visitpost(request):
    return render(request, "blogger/visitpost.html")

