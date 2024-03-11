from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from podcasts.serializers import EpisodeSerializer
from content_aggregator.utils.token_checker import is_access_token_valid
from django.http import JsonResponse
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from podcasts.models import Episode
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, redirect


User = get_user_model()


@ensure_csrf_cookie
def favorites_template(request):
    access_token = request.COOKIES.get('access_token')  # Assuming the token is stored in cookies

    if not access_token or not is_access_token_valid(access_token):
        # If access token is not present or not valid, redirect to login page
        return redirect('/authentication/login')

    return render(request, 'favorites.html')


class FavoriteAPIView(ListAPIView):
    serializer_class = EpisodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Episode.objects.filter(user=user)
        else:
            return Episode.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AddToFavoritesView(UpdateAPIView):
    queryset = Episode.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            episode = Episode.objects.get(pk=kwargs.get('pk'))
            episode.user.add(request.user)
            episode.save()
            return JsonResponse({'message': 'Episode added to favorites '
                                            'successfully.'}, status=200)
        except Episode.DoesNotExist:
            return JsonResponse({'error': 'Episode not found.'}, status=404)

