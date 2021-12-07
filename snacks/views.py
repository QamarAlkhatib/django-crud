# from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snacks
from django.urls import reverse_lazy


class ListSnackView(ListView):
    template_name = 'snack_list.html'
    model = Snacks

class DetailSnackView(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks

class CreateSnackView(CreateView):
    template_name = 'snack_create.html'
    model = Snacks
    fields = ['title', 'purchaser', 'description']

class UpdateSnackView(UpdateView):
    template_name = 'snack_update.html'
    model = Snacks
    fields = ['title', 'purchaser', 'description']


class DeleteSnackView(DeleteView):
    template_name = 'snack_confirm_delete.html'
    model = Snacks
    success_url = reverse_lazy('snack_list')

    