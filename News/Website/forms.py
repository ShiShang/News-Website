from django import forms

class Comment(forms.Form):
    Name=forms.CharField(label='Name',max_length=40,error_messages={
    'required':'Please enter your name!',
    'max_length':' Your name is too long!'
    })
    Email=forms.EmailField(label='Email',error_messages={
    'required':'Please enter your name!',
    'invaild':'Please enter the correct Email address!'
    })
    Comment=forms.CharField(label='Comment',max_length=256,error_messages={
    'required':'Please enter your name!',
    'max_length':' Your name is too long!'
    })


class Login(forms.Form):
    Name=forms.CharField(label='Name',max_length=40,error_messages={
    'required':'Please enter your name!',
    'max_length':' Your name is too long!'
    })
    Password=forms.CharField(label='Password',max_length=40,error_messages={
    'required':'Please enter your name!',
    'max_length':' Your name is too long!'
    })

class RegisterForm(forms.Form):
    Name=forms.CharField(label='Name',max_length=40,error_messages={
    'required':'Please enter your name!',
    'max_length':' Your name is too long!'
    })
    Password=forms.CharField(label='Password',max_length=40,error_messages={
    'required':'Please enter your Password!',
    'max_length':' Your Password is too long!'
    })
    Profile=forms.CharField(label='Profile',max_length=40,error_messages={
    'required':'Please enter your Profile!',
    'max_length':' Your name is too long!'
    })




	
	
	
	
	
	
	
	
	
	
	
	
	