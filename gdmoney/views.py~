# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from gdmoney.models import GdMoney

class GdMoneyView(TemplateView):
    def get(self, request):
        data_dict = {}
        gdmoney = []
        database_object = GdMoney.objects.all()
        for data in database_object:
            data_dict['name'] = data.name
            data_dict['fine'] = data.fine
            data_dict['money_earned'] = data.money_earned
            data_dict['total'] = data.money_earned - data.fine
            data_dict['balance'] = data_dict['total'] + data.paid
            gdmoney.append(data_dict.copy())
            print(data_dict)
        return render(request, 'gdmoney/money.html', context={'students': gdmoney})
