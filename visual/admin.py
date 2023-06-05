from django.contrib import admin
from visual.models import CreditApplication, Contract, Producer, Position

admin.site.register(Contract)
admin.site.register(Producer)
admin.site.register(Position)
admin.site.register(CreditApplication)
