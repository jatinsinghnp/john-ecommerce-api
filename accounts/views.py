from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            # Check if the user exists
            user = User.objects.filter(username=username).first()
            if user is not None:
                # User exists, authenticate the user
                authenticated_user = User.objects.filter(username=username).first()
                if (
                    authenticated_user is not None
                    and authenticated_user.check_password(password)
                ):
                    # Generate tokens for the user
                    refresh = RefreshToken.for_user(authenticated_user)
                    access_token = str(refresh.access_token)

                    # Return tokens with success message
                    return Response(
                        {"access_token": access_token, "message": "Login successful"},
                        status=200,
                    )
                else:
                    # Invalid credentials, handle the error...
                    return Response({"error": "Invalid credentials"}, status=400)
            else:
                # User does not exist, create and give tokens
                new_user = User.objects.create_user(
                    username=username, password=password
                )
                refresh = RefreshToken.for_user(new_user)
                access_token = str(refresh.access_token)

                # Return tokens with success message
                return Response(
                    {
                        "access_token": access_token,
                        "message": "User created and logged in",
                    },
                    status=201,
                )

        # Missing username or password, handle the error...
        return Response({"error": "Missing username or password"}, status=400)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Get the user associated with the request (since we are using IsAuthenticated permission)
        user = request.user

        # Delete the user's token
        try:
            token = Token.objects.get(user=user)
            token.delete()
        except Token.DoesNotExist:
            pass  # If the token does not exist, no need to raise an error

        return Response(
            {"message": "Logged out successfully"}, status=status.HTTP_200_OK
        )
