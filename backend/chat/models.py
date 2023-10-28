from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

def upload_image_profile(instance, filename):
    return f"profile/{instance}/{filename}"

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="nombre de usuario", max_length=100, null=False, blank=False, unique=True)
    slug = models.SlugField(verbose_name="nombre de busqueda", editable=False, null=True, blank=True)
    picture = models.ImageField(verbose_name="foto de perfil", upload_to=upload_image_profile, blank=True, null=True)
    friends = models.ManyToManyField('FriendModel', related_name="friends_profiles")
    
    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        ordering = ["slug"]
        

    def save(self, *args, **kwargs):
        name = slugify(self.name)
        self.slug = name
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.name}"


class FriendModel(models.Model):
    friend_porfile = models.OneToOneField(ProfileModel, verbose_name="amigo", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "amigo"
        verbose_name_plural = "amigos"
    
    def __str__(self) -> str:
        return self.friend_porfile.name