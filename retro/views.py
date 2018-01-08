from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import *


class IndexView(generic.ListView):
    template_name = 'retro/index.html'
    context_object_name = 'retro_list'

    def get_queryset(self):
        return Retro.objects.all()


class CreateRetro(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Retro
    fields = ['project', 'team', 'category', 'sprint', 'description', 'action_item', 'owner', 'status', 'eta']
    template_name = 'retro/create.html'
    success_url = reverse_lazy('index')
    success_message = "Retro item was created successfully"


class UpdateRetro(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Retro
    fields = ['project', 'team', 'category', 'sprint', 'description', 'action_item', 'owner', 'status', 'eta']
    template_name = 'retro/edit.html'
    success_url = reverse_lazy('index')
    success_message = "Retro item was updated successfully"


class DeleteRetro(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Retro
    template_name = 'retro/retro_confirm_delete.html'
    success_url = reverse_lazy('index')
    success_message = "Retro item was deleted successfully"


class RetroFeedback(SuccessMessageMixin, generic.CreateView):
    model = Feedback
    fields = ['name', 'title', 'description']
    template_name = 'retro/feedback.html'
    success_url = reverse_lazy('index')
    success_message = "Thank you for your valuable feedback!"
