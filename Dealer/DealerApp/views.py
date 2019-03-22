from django.shortcuts import render
from DealerApp.models import PostEnquiry,BikeSale,BikePurchase
from DealerApp import forms
# Create your views here.
def index_view(request):
    return render(request,'DealerApp/index.html')


def Engquiry_view(request):
    form=forms.PostForm()
    if request.method == 'POST':
        form=forms.PostForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'DealerApp/thanks.html')
    my_dic={'form':form}
    return render(request,'DealerApp/sell.html',context=my_dic)



def Service_view(request):
    return render(request,'DealerApp/services.html')
