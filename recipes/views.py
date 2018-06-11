from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Recipe, Comment
from .forms import UserForm
from django import forms


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'

    def get_queryset(self):
        return Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'time', 'difficulty', 'ingridients', 'description', 'photo']

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return response

class CommentCreate(CreateView):
    model = Comment

    def get_initial(self):
        initial = super().get_initial()
        initial["recipe"] = self.request.GET.get("recipe", None)
        return initial

    fields = ['recipe', 'content']

    def get_form(self, form_class):
        form = super().get_form(form_class)
        form.fields['recipe'].widget = forms.HiddenInput()
        return form

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return response

    def get_success_url(self):
        return reverse_lazy('recipes:index')

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'time', 'difficulty', 'ingridients', 'description', 'photo']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'recipes/registration.html'

    # pusty formularz
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # wysłany formularz
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # jakies ogarniete dane
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)     #ustawienie hasla
            user.save()     #zapisywanie do bazy danych

            user = authenticate(username=username, password=password)   #sprawdza czy user istnieje

            if user is not None:
                if user.is_active:
                    login(request, user)    #zalogowanie
                    return redirect('recipes:index')

        return render(request, self.template_name, {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                recipes = Recipe.objects.filter(user=request.user)
                return render(request, 'recipes/index.html', {'recipes': recipes})
            else:
                return render(request, 'recipes/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'recipes/login.html', {'error_message': 'Invalid login'})
    return render(request, 'recipes/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'recipes/login.html', context)

