from django.shortcuts import render,redirect, HttpResponseRedirect
from PIL import Image
import stepic
import io 
from django.views import View
from app.models import Customer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.

def index(request):
    return render(request,'index.html')

def hide_text_in_image(image,text):
    data=text.encode('utf-8')
    return stepic.encode(image,data)

def encryption(request):
    message=""
    if request.method == "POST":
        text=request.POST['text']
        image_file=request.FILES['image']
        image = Image.open(image_file) 
		
        # if image.format != 'PNG': convert(image_file)

        new_image = hide_text_in_image(image,text)
        image_path='encrypted_images/'+ 'new_' + image_file.name
        new_image.save(image_path)
        message="Text has been encrypted in the image"
    return render(request,'encrypt.html',locals())

def decryption(request):
    text=""
    if request.method == 'POST':
        image_file=request.FILES['image']
        image = Image.open(image_file)

        text = extract_text_from_image(image)
    return render(request,'decrypt.html',locals())

def extract_text_from_image(image):
    data = stepic.decode(image)
    if isinstance(data,bytes):
        return data.decode('utf-8')
    return data 



class Login(View):
	return_url = None

	def post(self,request):
		userData = request.POST
		image_file=request.FILES['password']
		image = Image.open(image_file)
		text = extract_text_from_image(image)
		customerEmail = Customer.emailExits(userData["email"])
		if customerEmail:
			if check_password(text,customerEmail.password):
				request.session["customer"] = customerEmail.id
				if Login.return_url:
					return HttpResponseRedirect(Login.return_url)
				else:
					Login.return_url = None
					return redirect('/encryption')
			else:
				return render(request,'index.html',{"userData":userData,"error":"Email or password doesn't match"})
		else:
			return render(request,'index.html',{"userData":userData,"error":"Email or password doesn't match"})



class Signup(View):

	def get(self,request):
		return render(request,'index.html')
			
	def post(self,request):
		userData = request.POST
		password=""
		# validate
		error = self.validateData(userData)
		if error :
			return render(request,'index.html',{"error":error,"userData":userData})
		else:
			if Customer.emailExits(userData['email']):
				error["emailExits_error"] = "Email Already Exits"
				return render(request,'index.html',{"error":error,"userData":userData})
			else:
				customer = Customer(
					name=userData['name'],
					email=userData['email'],
					phone=userData['phone'],
					password=make_password(userData['password']),
				)
					
				customer.save()
	
				text=request.POST.get('password')
				image_file=request.FILES['image']
				image = Image.open(image_file)
				new_image = hide_text_in_image(image,text)
				image_path='encrypted_images/'+ 'new_' + image_file.name
				new_image.save(image_path)	
		return redirect('index')


	# Validate form method
	def validateData(self,userData):
		error = {}
		if not userData['name'] or not userData['email']  or not userData['phone']  or not userData['password'] or not userData['confirm_password']:
			error["field_error"] = "All field must be required"
		if len(userData['password'])<8 and len(userData['confirm_password'])<8 :
			error['minPass_error'] = "Password must be 8 char"
		elif len(userData['name']) > 25 or len(userData['name']) < 3 :
			error["name_error"] = "Name must be 3-25 charecter"
		elif len(userData['phone']) != 10:
			error["phoneNumber_error"] = "Phone number must be 11 charecter."
		elif userData['password'] != userData['confirm_password']:
			error["notMatch_error"] = "Password doesn't match"	

		return error
	

    
def logout(request):
	request.session.clear()
	return redirect('/')

# def convert(image_file):
# 	file ='encrypted_images/'+image_file.name
# 	with open(file, 'rb') as jpg_file:
# 		jpg_data = jpg_file.read()
# 	jpg_image = Image.open(io.BytesIO(jpg_data))
# 	png_data = io.BytesIO()
# 	jpg_image.save(png_data, format='PNG')
# 	# png_bytes = png_data.getvalue()
# 	# image = Image.open(io.BytesIO(png_bytes))
# 	return image