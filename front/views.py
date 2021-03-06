from django.shortcuts import render
from django.http import HttpResponse
#from management.models import Fm as fb
import os
# Create your views here.
def index(request):
	return render(request,'index.html')
	'''
	if request.method == 'GET':
		data = fb.objects.all()
		#下表获取
		d_descipt = data[1].descipt
		#传输字典
		context = {
			'cs' : 'wanan',
			'lists' : data 
		}

		return render(request,'index.html',context)
		
	else:
		title = request.POST['title']
		descipt = request.POST['descipt']
		img = request.FILES['img']
		ffb = fb(title=title,descipt=descipt,img=img.name)
		ffb.save()
		#保存图片
		imgdir = os.path.join('statics',img.name)
		with open(imgdir,'wb+') as f:
			f.write(img.read())
		return HttpResponse(imgdir)



'''
