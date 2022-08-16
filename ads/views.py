import logging
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

log = logging.getLogger(__name__)


def autoview(request):
    log.debug('autoview() is working.')
    log.debug(f'HTTP request: {request}')
    response: HttpResponse = HttpResponse("You're in the ADS app!")
    return response
