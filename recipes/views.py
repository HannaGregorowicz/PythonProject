from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .models import Recipe
from .forms import UserForm
from django.http import JsonResponse

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