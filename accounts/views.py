from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            # Check if the user exists
            user = User.objects.filter(username=username).first()
            if user is not None:
                # User exists, authenticate and login
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    token, _ = Token.objects.get_or_create(user=authenticated_user)
                    # Return token with success message
                    return Response(
                        {"token": token.key, "message": "Login successful"}, status=200
                    )
                else:
                    # Invalid credentials, handle the error...
                    return Response({"error": "Invalid credentials"}, status=400)
            else:
                # User does not exist, create and give token
                new_user = User.objects.create_user(
                    username=username, password=password
                )
                token, _ = Token.objects.get_or_create(user=new_user)
                # Return token with success message
                return Response(
                    {"token": token.key, "message": "User created and logged in"},
                    status=201,
                )

        # Missing username or password, handle the error...
        return Response({"error": "Missing username or password"}, status=400)
