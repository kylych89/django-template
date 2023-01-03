from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth import login, authenticate

from .models import User, Regions


def indexView(request):
    info = 'Главная страница'

    context = {
        'info': info,
    }
    return render(request, 'main/index.html', context)


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form": form})


def registerView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create(username=username, password=password, email=email, ).save()
        return redirect('main:index')

    else:
        form = ContactForm()

        context = {
            'form': form
        }
    return render(request, 'main/register.html', context)


def sverdlovView(request):
    sverdlov = Regions.objects.get(id=1)
    name = sverdlov.name
    info = sverdlov.info

    context = {
        'name': name,
        'info': info,
    }

    return render(request, 'main/sverdlov.html', context)


def leninView(request):
    lenin = Regions.objects.get(id=2)
    name = lenin.name
    info = lenin.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/lenin.html', context)


def oktyabrView(request):
    oktyabr = Regions.objects.get(id=3)
    name = oktyabr.name
    info = oktyabr.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/oktyabr.html', context)


def pervomayView(request):
    pervomay = Regions.objects.get(id=4)
    name = pervomay.name
    info = pervomay.info

    context = {
        'name': name,
        'info': info,
    }
    return render(request, 'main/pervomay.html', context)


def chuiView(request):
    info = 'Чу́йская о́бласть (кирг. Чүй облусу) находится в северной части Киргизии, образована как \
    Фрунзенская область 21 ноября 1939 года Указом Президиума Верховного Совета СССР, упразднена в 1959 году. \
    Была восстановлена из районов республиканского подчинения в 1990 году под современным названием.'

    context = {
        'info': info,
    }
    return render(request, 'main/chui.html', context)


def talasView(request):
    info = 'Таласская область (кирг. Талас облусу) — самая маленькая область Киргизии, находится в северо-западной \
    части страны.Занимает Таласскую долину и склоны гор Киргизского Ала-Тоо. Граничит на севере и западе \
    с Казахстаном (Жамбылская область), на юге — с Джалал-Абадской, на востоке — с Чуйской областями Киргизии.'

    context = {
        'info': info,
    }
    return render(request, 'main/talas.html', context)


def yssykkolView(request):
    info = 'Иссык-Ку́льская о́бласть (кирг. Ысык-Көл облусу) — самый восточный регион Киргизии. Административный \
    центр — город Каракол. Образована Указом Президиума Верховного Совета СССР от 21 ноября 1939 года с центром \
    в городе Пржевальск (в область был преобразован Иссык-Кульский округ). 27 января 1959 года упразднена[1]. \
    Вновь создана 11 декабря 1970 года; в июле 1989—1991 году областной центр находился в городе Иссык-Куль, \
    в 1991 году вернулся в Пржевальск (в 1991 переименован в Каракол).'

    context = {
        'info': info,
    }
    return render(request, 'main/yssykkol.html', context)


def narynView(request):
    info = 'Нары́нская область (кирг. Нарын облусу) находится в центральной части Киргизии. Занимает долины и склоны \
    гор Внутреннего Тянь-Шаня и является самым крупным регионом в стране.Образована Указом Президиума Верховного \
    Совета СССР от 21 ноября 1939 года как Тянь-Шанская область с центром в городе Нарын. Первоначально \
    включала 6 районов (Ак-Талинский, Ат-Башинский, Джумгальский, Кочкорский, Нарынский и Тогуз-Тороузский) \
    и город областного подчинения Нарын. В 1944 году были образованы Куланакский и Чолпонский районы \
    (упразднены в 1958 и 1956 годах соответственно).'

    context = {
        'info': info,
    }
    return render(request, 'main/naryn.html', context)


def oshView(request):
    info = 'Ошская область (кирг. Ош облусу) — административная единица Киргизской Республики. \
    Образована Указом Президиума Верховного Совета СССР от 21 ноября 1939 года. Административный \
    центр — город Ош (в состав области не входит).Ошская область образована 21 ноября 1939 года. \
    Позже из неё были выделены Джалал-Абадская (1990) и Баткенская (1999) области. \
    В начале XXI века неоднократно была очагом антиправительственных выступлений (Тюльпановая революция).'

    context = {
        'info': info,
    }
    return render(request, 'main/osh.html', context)


def jalalabadView(request):
    info = 'Джала́л-Аба́дская о́бласть (также Жалалабатская, Жалал-Абадская) — одна из административно-территориальных \
    единиц Кыргызской Республики, расположенная на юго-западе страны. Образована Указом Президиума Верховного \
    Совета СССР от 21 ноября 1939 года. Административный центр области — город Джалал-Абад. В 2002 году \
    переименован в Жалалабат согласно принятой Жогорку Кенешем Киргизии «Новой редакции орфографии киргизского \
    языка» от 28 июня 2002 года за № 830-11. В июне 2008 года переименован обратно в Джалал-Абад согласно \
    постановлению Жогорку Кенеша Кыргызстана о восстановлении написания населённых пунктов страны через дефис.'

    context = {
        'info': info,
    }
    return render(request, 'main/jalalabad.html', context)


def batkenView(request):
    info = 'Батке́нская о́бласть (кирг. Баткен облусу) — область Киргизии. Административный центр области \
    — Баткен. На востоке она граничит с Ошской областью, на юге, западе и севере — с Таджикистаном, \
    а на северо-востоке — с Узбекистаном. Северная часть области является частью плоской, сельскохозяйственной \
    Ферганской долины. Земля поднимается к югу до гор на южной границе: Алайские горы на востоке и Туркестанский \
    хребет на западе.'

    context = {
        'info': info,
    }
    return render(request, 'main/batken.html', context)
