from django.db import models
from accounts.models import CustomeUser


class ReferralUser(models.Model):
    i_invited = models.ForeignKey(CustomeUser,
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  verbose_name='меня пригласил',
                                  related_name='referred') #человек который меня пригласил
    he_invited_me = models.ForeignKey(CustomeUser,
                                      on_delete=models.CASCADE,
                                      blank=True,
                                      verbose_name='я пригласил',
                                      related_name='referrer') #человек которых я пригласил

    def __str__(self):
        return f'{self.i_invited}'

    class Meta:
        verbose_name_plural = 'реферальная ссылка'
