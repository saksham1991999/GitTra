import os

from django.shortcuts import render, redirect, get_object_or_404

from .forms import RepositoryForm
from .models import Repository
from .utilities.git_commands import git_clone, translate_repo


def home_view(request):
    form = RepositoryForm()
    if request.method == "POST":
        form = RepositoryForm(request.POST, request.FILES)
        if request.POST['url']:
            if form.is_valid():
                new_form = form.save(commit=False)
                url = new_form.url
                url = url.replace(".git", "")
                language = new_form.language
                current_dir = os.getcwd()
                os.chdir(current_dir)
                repo_name, user_path = git_clone(url)
                os.chdir(current_dir)
                zip_path = translate_repo(repo_name, user_path, language=language)
                zip_url = zip_path.replace(current_dir, "")
                repository = Repository.objects.create(url=url, language=language, directory=zip_url)
                # repository.translated.path = zip_url
                repository.save()
                return redirect("core:result", repository.id)
        elif request.POST['file']:
            if form.is_valid():
                form.save()
                file = form.cleaned_data['file']

            file = request.POST['file']
            print("Found a file")

            return redirect('core:result')
    context = {
        "form": form
    }
    return render(request, 'index.html', context)


def result(request, id):
    repository = get_object_or_404(Repository, id=id)
    context = {
        "repository": repository
    }
    return render(request, "result.html", context)


def repo_url_view(request, github_username, repo_name):
    language = "en"
    if "language" in request.GET:
        language = request.GET['language']
    url = "https://github.com/{}/{}".format(github_username, repo_name)
    url = url.replace(".git", "")
    current_dir = os.getcwd()
    os.chdir(current_dir)
    repo_name, user_path = git_clone(url)
    os.chdir(current_dir)
    zip_path = translate_repo(repo_name, user_path, language=language)

    zip_url = zip_path.replace(current_dir, "")
    repository = Repository.objects.create(url = url, language = language, directory = zip_url)
    # repository.translated.path = zip_url
    repository.save()
    return redirect('core:result', repository.id)
