# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from website import models as wm
from projeto_redacao import models as prm
from politicas_afirmativas import models as pam
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PerfilDeAluno(Perfil):
    aluno = models.ForeignKey(wm.Aluno, on_delete=models.CASCADE, verbose_name=u'Aluno')

    def __unicode__(self):
        return self.aluno.get_nome()

    class Meta:
        managed = True
        verbose_name = u'Perfil de Aluno'
        verbose_name_plural = u'Perfis de Aluno'


class PerfilDeVoluntario(Perfil):
    voluntario = models.ForeignKey(wm.Voluntario, on_delete=models.CASCADE, verbose_name=u'Voluntário')

    def __unicode__(self):
        return self.voluntario

    class Meta:
        managed = True
        verbose_name = u'Perfil de Voluntário'
        verbose_name_plural = u'Perfis de Voluntário'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilDeAluno.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    profile = PerfilDeAluno.objects.get(user=instance)
    profile.save()
