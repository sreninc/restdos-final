from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    mobile = forms.CharField(max_length=20, label='Mobile')
    signup_plan = forms.CharField(max_length=30, label='Signup Plan')
    signup_monthly = forms.IntegerField(label='Monthly Fee')



    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.mobile = self.cleaned_data['mobile']
        user.signup_plan = self.cleaned_data['signup_plan']
        user.signup_monthly = self.cleaned_data['signup_monthly']
        user.save()