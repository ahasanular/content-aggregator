from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render


@ensure_csrf_cookie
def login_page(request):
    return render(request, 'login.html')


@ensure_csrf_cookie
def register_page(request):
    return render(request, 'register.html')


from django.contrib.auth.views import LogoutView
from django.http import JsonResponse
from django.urls import reverse_lazy


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('explore')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        # Remove access and refresh tokens from local storage
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return JsonResponse({'message': 'Logout successful'}, status=200)


from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View


User = get_user_model()


class CustomRegisterView(View):
    def post(self, request, *args, **kwargs):
        # Extract data from request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate data
        if not username or not password:
            return JsonResponse(
                {'error': 'Username and password are required'},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {'error': 'Username is already taken'},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response_data = {
            'access': access_token,
            'refresh': str(refresh),
        }

        # return Response(data=response_data, status=201)
        return JsonResponse(data=response_data, status=201)
