from django.contrib.auth.backends import ModelBackend
from accounts.models import CustomeUser


class UserModelBackend(ModelBackend):

    def authenticate(self, request, phone_number=None, **kwargs):
        try:
            user = CustomeUser.objects.get(phone_number=phone_number)
            return user
        except CustomeUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = CustomeUser.objects.get(pk=user_id)
            return user
        except CustomeUser.DoesnotExist:
            return None

        return user if self.user_can_authenticate(user) else None
