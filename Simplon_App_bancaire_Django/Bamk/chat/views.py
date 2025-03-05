from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import get_object_or_404

class ChatRoomView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "chat/chat_room.html"
    context_object_name = "messages"

    def get_queryset(self):
        """Récupère uniquement les messages entre l'utilisateur et son conseiller"""
        user = self.request.user

        if hasattr(user, "profile") and user.profile.advisor:
            chat_partner = user.profile.advisor  # Client vers conseiller
        else:
            chat_partner = User.objects.filter(profile__advisor=user).first()  # Conseiller vers client

        if chat_partner:
            return Message.objects.filter(
                sender__in=[user, chat_partner],
                receiver__in=[user, chat_partner]
            ).order_by("timestamp")
        return Message.objects.none()

    def get_context_data(self, **kwargs):
        """Ajoute le conseiller ou client en tant que partenaire de chat"""
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if hasattr(user, "profile") and user.profile.advisor:
            chat_partner = user.profile.advisor
        else:
            chat_partner = User.objects.filter(profile__advisor=user).first()

        context["chat_partner"] = chat_partner
        return context

class ClientChatView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "chat/client_chat.html"
    context_object_name = "messages"

    def get_queryset(self):
        """Récupère les messages entre le conseiller et le client sélectionné."""
        user = self.request.user
        client = get_object_or_404(User, pk=self.kwargs["client_id"])

        return Message.objects.filter(
            sender__in=[user, client],
            receiver__in=[user, client]
        ).order_by("timestamp")

    def get_context_data(self, **kwargs):
        """Ajoute le client au contexte pour l'afficher dans le template."""
        context = super().get_context_data(**kwargs)
        context["client"] = get_object_or_404(User, pk=self.kwargs["client_id"])
        return context
    
    def mark_messages_as_read(self):
        """Marque tous les messages comme lus"""
        messages = Message.objects.filter(receiver=self.request.user, sender=self.kwargs["client_id"], is_read=False)
        messages.update(is_read=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client"] = get_object_or_404(User, pk=self.kwargs["client_id"])

        # 🔴 Marquer les messages comme lus
        self.mark_messages_as_read()

        return context
