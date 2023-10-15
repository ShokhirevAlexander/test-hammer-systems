from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserProfileForm
from referral.forms import CodeForm
from django.contrib import auth
from .models import CustomeUser
from referral.models import ReferralUser


def index(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    else:
        return render(request, 'accounts/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        user_register = CustomeUser.objects.filter(phone_number=request.POST.get('phone_number'))

        if user_register.exists():
            user = authenticate(request, phone_number=request.POST.get('phone_number'))
            request.session['pk'] = user.pk
            return redirect('accounts:verified')

        if form.is_valid():
            form.save()
            user = authenticate(request, phone_number=form.cleaned_data['phone_number'])
            request.session['pk'] = user.pk
            return redirect('accounts:verified')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def verified_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomeUser.objects.get(id=pk)

        if request.method == 'POST':

            password = request.POST.get('password_phone')

            if str(password) == user.password_phone:
                login(request, user, backend='accounts.backends.UserModelBackend')
                return redirect('accounts:profile')
            else:
                return redirect('accounts:index')
    return render(request, 'accounts/verified.html', {'form': form})


@login_required
def profile_view(request):
    form = UserProfileForm(request.POST or None)
    user = CustomeUser.objects.get(phone_number=request.user)

    referred = user.referred.select_related('he_invited_me').first()

    referrer = user.referrer.select_related('i_invited').filter(he_invited_me=request.user).order_by('id')

    paginator = Paginator(referrer, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'form': form,
               'referrer': referrer,
               'he_invited_me': referred,
               'referral': page_obj}

    return render(request, 'accounts/profile.html', context)


@login_required
def invite_referral(request):
    """ Активация реферальной ссылки в профиле """

    form = UserProfileForm(request.POST)
    if form.is_valid():
        invite_code = form.cleaned_data['invite_code']

        referrer_user = CustomeUser.objects.get(invite_code=invite_code)
        my_referrer = CustomeUser.objects.get(phone_number=request.user)

    if referrer_user != my_referrer:
        ReferralUser.objects.get_or_create(
            i_invited=my_referrer,
            he_invited_me=referrer_user,
        )

    return redirect('accounts:profile')


def logout(request):
    auth.logout(request)
    return redirect('accounts:index')
