from django import forms
from users.models import User

class PessoaJuridicaForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(PessoaJuridicaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ['username', 'email', 'nome_completo', 'cnpj', 'razao_social', 'imagemperfil', 'email_extra', 'telefone_contato', 'telefone_contato_extra', 
        'cep','cidade' ,'bairro', 'rua', 'numero', 'complemento', 'paginadoperfil', 'linkdoperfil','password']

class PessoaFisicaForm(forms.ModelForm):

    def save(self, commit=True):
        user = super(PessoaFisicaForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'email', 'imagemperfil', 'password']