from ctypes import cast
import logging
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from cats.forms import MakeForm
from cats.models import Breed, Cat

log = logging.getLogger(__name__)


def autoview(request):
    log.debug('autoview() is working.')
    response: HttpResponse = HttpResponse("You're in the Cats CRUD app!")
    return response


class MainCatsView(LoginRequiredMixin, View):

    def get(self, request):
        log.debug('MainCatsView: get() is working.')

        # search for breeds and cats
        breeds_count = Breed.objects.all().count()
        cats = Cat.objects.all()
        log.debug(f'Found #{breeds_count} breed(s) and #{cats.count()} cat(s).')

        # put objects into the 'context' and render+return the request
        ctx = {'breeds_count': breeds_count, 'cats_list': cats}
        return render(request, 'cats/cat_list.html', ctx)


# class MakeView(LoginRequiredMixin, View):
#     def get(self, request):
#         ml = Make.objects.all()
#         ctx = {'make_list': ml}
#         return render(request, 'autos/make_list.html', ctx)


# # We use reverse_lazy() because we are in "constructor attribute" code
# # that is run before urls.py is completely loaded
# class MakeCreate(LoginRequiredMixin, View):
#     template = 'autos/make_form.html'
#     success_url = reverse_lazy('autos:all')

#     def get(self, request):
#         form = MakeForm()
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request):
#         form = MakeForm(request.POST)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         make = form.save()
#         return redirect(self.success_url)


# # MakeUpdate has code to implement the get/post/validate/store flow
# # AutoUpdate (below) is doing the same thing with no code
# # and no form by extending UpdateView
# class MakeUpdate(LoginRequiredMixin, View):
#     model = Make
#     success_url = reverse_lazy('autos:all')
#     template = 'autos/make_form.html'

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(request.POST, instance=make)
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         form.save()
#         return redirect(self.success_url)


# class MakeDelete(LoginRequiredMixin, View):
#     model = Make
#     success_url = reverse_lazy('autos:all')
#     template = 'autos/make_confirm_delete.html'

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'make': make}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(self.success_url)


# # Take the easy way out on the main table
# # These views do not need a form because CreateView, etc.
# # Build a form object dynamically based on the fields
# # value in the constructor attributes
# class AutoCreate(LoginRequiredMixin, CreateView):
#     model = Auto
#     fields = '__all__'
#     success_url = reverse_lazy('autos:all')


# class AutoUpdate(LoginRequiredMixin, UpdateView):
#     model = Auto
#     fields = '__all__'
#     success_url = reverse_lazy('autos:all')


# class AutoDelete(LoginRequiredMixin, DeleteView):
#     model = Auto
#     fields = '__all__'
#     success_url = reverse_lazy('autos:all')

# # We use reverse_lazy rather than reverse in the class attributes
# # because views.py is loaded by urls.py and in urls.py as_view() causes
# # the constructor for the view class to run before urls.py has been
# # completely loaded and urlpatterns has been processed.

# # References

# # https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview