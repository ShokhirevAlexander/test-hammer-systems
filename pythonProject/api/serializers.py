from rest_framework import serializers
from referral.models import ReferralUser


class ReferralSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='i_invited.phone_number')

    class Meta:
        model = ReferralUser
        fields = ('phone_number',)
