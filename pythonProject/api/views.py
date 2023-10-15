import random

from django.contrib.auth import login

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from accounts.models import CustomeUser
from api.serializers import ReferralSerializer


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_all(request):
    if request.method == 'GET':
        user = CustomeUser.objects.get(id=request.user.id)
        qs = user.referrer.select_related('i_invited').filter(he_invited_me=request.user).order_by('id')
        serializer = ReferralSerializer(qs, many=True)
        return Response(serializer.data)
