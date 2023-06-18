from django.shortcuts import render

# Create your views here.

# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from django.conf import settings
import jwt


class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    def complete_login(self, request, app, token, response, **kwargs):
        print("GAA")
        print(response)
        try:
            identity_data = jwt.decode(
                response["id_token"], #another nested id_token was returned
                options={
                    "verify_signature": False,
                    "verify_iss": True,
                    "verify_aud": True,
                    "verify_exp": True,
                },
                issuer=self.id_token_issuer,
                audience=app.client_id,
            )
        except jwt.PyJWTError as e:
            raise OAuth2Error("Invalid id_token") from e
        login = self.get_provider().sociallogin_from_response(request, identity_data)
        return login

class GoogleLoginView(SocialLoginView):
  # authentication_classes = [] # disable authentication, make sure to override `allowed origins` in settings.py in production!
  adapter_class = CustomGoogleOAuth2Adapter
  # callback_url = "https://test-dk4c.vercel.app/"  # frontend application url
  # callback_url = "http://127.0.0.1:8000/accounts/google/login/callback/"
  # callback_url = "http://localhost:3000/api/auth/callback/google"
  callback_url = "http://localhost:3000/"
  client_class = OAuth2Client
 
