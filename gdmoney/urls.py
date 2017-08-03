# This two if you want to enable the Django Admin: (recommended)                                       
from django.contrib import admin                                                                       
admin.autodiscover()                                                                                   
                                                                                                       
from django.conf.urls import include, url                                                              
from gdmoney.views import GdMoneyView                                                                                    
                                                                                                       
urlpatterns = [                                                                                        
#    url(r'^$', views.index, name='index'),                                                             
    url(r'^money/', GdMoneyView.as_view(), name='moneyview'),                                        
] 