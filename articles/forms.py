from django import forms
from django.contrib.auth.forms import AuthenticationForm

# AuthenticationForm의 username과 password 기본 양식을 따옴. -> custom
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=(""),     # 표시되는 문자를 지움
        widget=forms.TextInput(
            attrs={
                # "autofocus": True,
                "class" : "gray-border login-box",  # CSS를 정의(String 내에 띄워쓰기로 구분)
                "placeholder" : "아이디"            # 내부 표시되는 텍스트 정의
                })
                )
    
    password = forms.CharField(
        label=(""),     # 표시되는 문자를 지움
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                # "autocomplete": "current-password",
                "class" : "gray-border login-box",
                "placeholder" : "비밀번호"
                }),
    )