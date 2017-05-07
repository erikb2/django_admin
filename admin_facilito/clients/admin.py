from django.contrib import admin
from .models import Client, SocialNetwork

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# El modelo Client es agregado dentro del Admin de django
# pero se quita el atributo user, para que no se asocie a otro usuario.
# Y unicamente se modifiquen los campos necesarios.


class ClientAdmin(admin.ModelAdmin):
    exclude = ('user',)


class ClientInLine(admin.StackedInline):
    model = Client
    can_delete = False


class SocialInLine(admin.StackedInline):
    model = SocialNetwork
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [ClientInLine, SocialInLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
