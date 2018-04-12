from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import *


class IndexView(generic.ListView):
    template_name = 'retro/index.html'
    context_object_name = 'retro_list'
    queryset = Retro.objects.order_by('-status', '-updated_on')


class CreateRetro(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Retro
    fields = ['project', 'team', 'category', 'sprint', 'description', 'action_item', 'retro_type', 'owner', 'status', 'eta']
    template_name = 'retro/create.html'
    success_url = reverse_lazy('index')
    success_message = "Retro item was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateRetro, self).form_valid(form)


class UpdateRetro(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Retro
    fields = ['project', 'team', 'category', 'sprint', 'description', 'action_item', 'retro_type', 'owner', 'status', 'eta']
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
