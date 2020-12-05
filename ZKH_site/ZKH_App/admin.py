from django.contrib import admin

# Register your models here.

from .models import Flat, Contract, Charge, Payment, Saldo
from .models import PaymentForm, ChargeForm

@admin.register(Flat)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'house_number', 'flat_number')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'created_at', 'updated_at', 'bill_number', 'address')


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('charge_number', 'created_at', 'updated_at', 'month', 'year', 'value', 'value_with_saldo', 'is_paid', 'contract')
    form = ChargeForm

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'value', 'charge')

@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'value', 'charge')