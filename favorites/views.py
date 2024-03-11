from django.views.generic import ListView
from django.contrib.auth import get_user_model
from podcasts.models import Episode


User = get_user_model()


class FavoritesView(ListView):
    template_name = "base.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["episodes"] = User.objects.filter().order_by(
        #     "-pub_date")[
        #     :10
        # ]
        return context


from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from podcasts.models import Episode


class UpdateFavoriteView(LoginRequiredMixin, View):
    def post(self, request, episode_id, *args, **kwargs):
        episode = get_object_or_404(Episode, id=episode_id)
        episode.user = self.request.user
        episode.save()
        return JsonResponse({'success': True})
