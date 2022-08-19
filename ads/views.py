import logging
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from ads.models import Ad
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
    # template_name = "ads/ads_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Ad model to the Ad form
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad
