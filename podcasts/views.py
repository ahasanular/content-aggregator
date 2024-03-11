from django.views.generic import ListView
from django.contrib.auth.models import AnonymousUser
from .models import Episode
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EpisodeSerializer
from content_aggregator.utils.token_checker import is_access_token_valid


@ensure_csrf_cookie
def explore_page(request):
    access_token = request.COOKIES.get('access_token')  # Assuming the token is stored in cookies

    if not access_token or not is_access_token_valid(access_token):
        # If access token is not present or not valid, redirect to login page
        return redirect('/authentication/login')

    return render(request, 'explore.html')


# class ExploreView(ListView):
#     template_name = "explore.html"
#     model = Episode
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         episodes = Episode.objects.filter().order_by("-pub_date")[
#                    :10]
#
#         for ep in episodes:
#             ep.is_favorite = False
#
#         if not isinstance(self.request.user, AnonymousUser):
#             episoded = self.request.user.user_episodes.all().values('id')
#             for ep in episodes:
#                 users = ep.user.all().values('id')
#                 if ep.user.filter(id=self.request.user.id).exists():
#                     ep.is_favorite = True
#         context['episodes'] = episodes
#         return context


class ExploreAPIView(ListAPIView):
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        episodes = Episode.objects.filter().order_by("-pub_date")[:10]

        for episode in episodes:
            episode.is_favorite = False

        if not isinstance(self.request.user, AnonymousUser):
            favorite_episode_ids = self.request.user.user_episodes.values_list('id', flat=True)
            for episode in episodes:
                if episode.id in favorite_episode_ids:
                    episode.is_favorite = True
        return episodes

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
