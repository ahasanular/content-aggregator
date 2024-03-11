import jwt
from datetime import datetime
from django.conf import settings


def is_access_token_valid(access_token):
    try:
        # Decode the access token
        decoded_token = jwt.decode(
            access_token,
            settings.SECRET_KEY, algorithms=['HS256']
        )

        # Check expiration time
        expiration_time = datetime.utcfromtimestamp(decoded_token['exp'])
        if expiration_time < datetime.utcnow():
            return False

        return True
    except jwt.ExpiredSignatureError:
        # Token has expired
        return False
    except jwt.InvalidTokenError:
        # Invalid token
        return False