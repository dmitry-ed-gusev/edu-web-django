import logging
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from ads.models import Ad
from ads.forms import CreateForm
from ads.owner import OwnerListView, OwnerDetailView, OwnerDeleteView, OwnerUpdateView, OwnerCreateView

log = logging.getLogger(__name__)


def autoview(request):
    log.debug('autoview() is working.')
    log.debug(f'HTTP request: {request}')
    response: HttpResponse = HttpResponse("You're in the ADS app!")
    return response


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class old_AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Ad model to the Ad form
    fields = ['title', 'price', 'text']


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class old_AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request, pk):
    """View for show picture in full size on the screen."""

    log.debug(f'stream_file(): showing picture for Ad with the id={pk}')
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
