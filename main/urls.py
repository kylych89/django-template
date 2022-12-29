from django.urls import path
from .views import (indexView,
                    leninView,
                    oktyabrView,
                    pervomayView,
                    sverdlovView,
                    chuiView,
                    talasView,
                    yssykkolView,
                    narynView,
                    oshView,
                    jalalabadView,
                    batkenView,
                    enterView,
                    registerView)

app_name = 'main'

urlpatterns = [
    path('index/', indexView, name='index'),
    path('sverdlov/', sverdlovView, name='sverdlov'),
    path('lenin/', leninView, name='lenin'),
    path('oktyabr/', oktyabrView, name='oktyabr'),
    path('pervomay/', pervomayView, name='pervomay'),
    path('chui/', chuiView, name='chui'),
    path('talas/', talasView, name='talas'),
    path('yssykkol/', yssykkolView, name='yssykkol'),
    path('naryn/', narynView, name='naryn'),
    path('osh/', oshView, name='osh'),
    path('jalalabad/', jalalabadView, name='jalalabad'),
    path('batken/', batkenView, name='batken'),
    path('enter/', enterView, name='enter'),
    path('register/', registerView, name='register'),
]


