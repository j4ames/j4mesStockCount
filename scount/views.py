from django.shortcuts import render, redirect
from .models import stockcount
from .models import stockuserrequest
from .models import stocklog
from .models import stockpreviousrequest
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

today_date = datetime.datetime.now()
date_format = today_date.strftime("%d/%m/%y")

def stock_home(request):
    stock_request_table=stockuserrequest.objects.all()
    stock_previous_request=stockpreviousrequest.objects.all()

    labels = []
    data = []

    queryset = stockcount.objects.all()
    for x in queryset:
        labels.append(x.stock_item)
        data.append(x.stock_item_quantity)

    return render(request, 'home.html', {
        'labels': labels,
        'data': data,
        'stock_request_table':stock_request_table,
        'stock_previous_request':stock_previous_request
    })

def stock_request(request):

    stock_request_table=stockuserrequest.objects.all()
    stock_count_table=stockcount.objects.all()

    stockRequestError = ""

    if request.method == 'POST':
        stock_count_instance=stockuserrequest()
        stock_count_instance.request_date = date_format
        stock_count_instance.request_requestor= "text1"
        stock_count_instance.request_item= request.POST.get('request_item')
        getQuantitiy = request.POST.get('request_quantity')
        convertQuantity = int(getQuantitiy)
        if convertQuantity >=1:
            stock_count_instance.request_quantity= getQuantitiy
            stock_count_instance.save()
        else:
            stockRequestError = "Please enter a number 1 or more"
    else:
        stock_count_instance=stockuserrequest()
        stock_count_instance.request_date = date_format
        stock_count_instance.request_requestor= "text1"
        stock_count_instance.request_item = request.POST.get('service_type')
        getQuantitiy = request.POST.get('request_quantity')
        convertQuantity = int(getQuantitiy)
        if convertQuantity >=1:
            stock_count_instance.request_quantity= getQuantitiy
            stock_count_instance.save()
        else:
            stockRequestError = "Please enter a number 1 or more"

        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'request.html',{'stock_request_table':stock_request_table, 'stock_count_table':stock_count_table, 'stockRequestError':stockRequestError})

def stock_main(request):

    stock_count_table=stockcount.objects.all()
    stock_request_table=stockuserrequest.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('stock_item'):
            stock_count_instance=stockcount()
            stock_count_instance.stock_item= request.POST.get('stock_item')
            stock_count_instance.stock_item_quantity= 1
            stock_count_instance.save()

            return redirect(request.META['HTTP_REFERER'])
    
    return render(request,'stock.html', {'stock_count_table':stock_count_table, 'stock_request_table':stock_request_table})
    
def delete(request,id):
  
  stock_count_instance = stockcount.objects.get(id=id)
  stock_count_instance.delete()

  return HttpResponseRedirect(reverse('stock'))

def updatestockname(request,id):

    stock_item = request.POST['stock_item']
    stock_count_instance = stockcount.objects.get(id=id)
    stock_count_instance.stock_item = stock_item
    stock_count_instance.save()
    return HttpResponseRedirect(reverse('stock'))

def updatequantity(request,id):

    stock_item_quantity = request.POST['stock_item_quantity']
    stock_count_instance = stockcount.objects.get(id=id)
    stock_count_instance.stock_item_quantity = stock_item_quantity
    stock_count_instance.save()

    return HttpResponseRedirect(reverse('stock'))

def approve(request,id):

    stock_count_deliver_item = "Approved, ordering and awaiting delivery"
    stock_count_instance = stockuserrequest.objects.get(id=id)
    stock_count_instance.request_status = stock_count_deliver_item
    stock_count_instance.request_status_home = stock_count_deliver_item
    stock_count_instance.save()

    return HttpResponseRedirect(reverse('stock'))

def approveinstock(request,id):

    stock_count_instock_item = "Approved, give to user"
    stock_count_instock_item_home = "Approved, IT will give to you soon"
    stock_count_instance = stockuserrequest.objects.get(id=id)
    stock_count_instance.request_status = stock_count_instock_item
    stock_count_instance.request_status_home = stock_count_instock_item_home
    stock_count_instance.save()

    return HttpResponseRedirect(reverse('stock'))

def reject(request,id):
        
    stock_count_id= stockuserrequest.objects.get(id=id)
    stock_count_transfer_date= stockuserrequest.objects.get(id=id).request_date
    stock_count_transfer_requestor= stockuserrequest.objects.get(id=id).request_requestor
    stock_count_transfer_item= stockuserrequest.objects.get(id=id).request_item
    stock_count_transfer_quantity= stockuserrequest.objects.get(id=id).request_quantity
    stock_count_transfer_status= "Rejected"
    stock_count_transfer_approvedby= stockuserrequest.objects.get(id=id).request_item

    stock_count_instance=stocklog()
    stock_count_instance.request_date = stock_count_transfer_date
    stock_count_instance.request_requestor = stock_count_transfer_requestor
    stock_count_instance.request_item = stock_count_transfer_item
    stock_count_instance.request_quantity = stock_count_transfer_quantity
    stock_count_instance.request_status = stock_count_transfer_status
    stock_count_instance.request_approvedby = stock_count_transfer_approvedby
    stock_item_ajfawih = request.POST['stock_reject_input']
    stock_count_instance.request_rejected = stock_item_ajfawih
    stock_count_instance.save()

    stock_count_instance2=stockpreviousrequest()
    stock_count_instance2.request_date = stock_count_transfer_date
    stock_count_instance2.request_item = stock_count_transfer_item
    stock_count_instance2.request_quantity = stock_count_transfer_quantity
    stock_count_instance2.request_status = stock_count_transfer_status
    stock_count_instance2.request_rejected = stock_item_ajfawih
    stock_count_instance2.save()

    stock_count_id.delete()

    return HttpResponseRedirect(reverse('stock'))

def delivered(request,id):

    stock_count_deliver_item = "Delivered"
    stock_count_deliver_item_home = "Item has been delivered, IT will give to you soon"
    stock_count_instance = stockuserrequest.objects.get(id=id)
    stock_count_instance.request_status = stock_count_deliver_item
    stock_count_instance.request_status_home = stock_count_deliver_item_home
    stock_count_instance.save()

    return HttpResponseRedirect(reverse('stock'))

def complete(request,id):

    stock_count_id= stockuserrequest.objects.get(id=id)
    stock_count_transfer_date= stockuserrequest.objects.get(id=id).request_date
    stock_count_transfer_requestor= stockuserrequest.objects.get(id=id).request_requestor
    stock_count_transfer_item= stockuserrequest.objects.get(id=id).request_item
    stock_count_transfer_quantity= stockuserrequest.objects.get(id=id).request_quantity
    stock_count_transfer_status= "Given to user"
    stock_count_transfer_approvedby= stockuserrequest.objects.get(id=id).request_item
    stock_count_given_item_home = "IT have given you the item"
    stock_count_id.request_status_home = stock_count_given_item_home

    stock_count_instance=stocklog()
    stock_count_instance.request_date = stock_count_transfer_date
    stock_count_instance.request_requestor = stock_count_transfer_requestor
    stock_count_instance.request_item = stock_count_transfer_item
    stock_count_instance.request_quantity = stock_count_transfer_quantity
    stock_count_instance.request_status = stock_count_transfer_status
    stock_count_instance.request_approvedby = stock_count_transfer_approvedby
    stock_count_instance.save()

    stock_count_instance2=stockpreviousrequest()
    stock_count_instance2.request_date = stock_count_transfer_date
    stock_count_instance2.request_item = stock_count_transfer_item
    stock_count_instance2.request_quantity = stock_count_transfer_quantity
    stock_count_instance2.request_status = stock_count_given_item_home
    stock_count_instance2.save()

    stock_count_id.delete()

    return HttpResponseRedirect(reverse('stock'))

def stock_log(request):

    stock_request_table_log=stocklog.objects.all()

    return render(request, 'log.html',{'stock_request_table_log':stock_request_table_log})

def signin(request):

  return render(request,'signin.html')

def stock_tools(request):
    if request.method == 'POST':
        if request.POST.get('stock_item'):
            stock_count_instance=stockcount()
            stock_count_instance.stock_item= request.POST.get('stock_item')
            stock_count_instance.stock_item_quantity= 1
            stock_count_instance.save()

            return redirect(request.META['HTTP_REFERER'])
    
    return render(request,'tools.html')


#MOVE FROM 1 DB TABLE TO ANOTHER

# def approve(request,id):

#     stock_count_id= stockuserrequest.objects.get(id=id)
#     stock_count_transfer_item= stockuserrequest.objects.get(id=id).request_item
#     stock_count_transfer_quantity= stockuserrequest.objects.get(id=id).request_quantity

#     stock_count_instance=stockcount()
#     stock_count_instance.stock_item= stock_count_transfer_item
#     stock_count_instance.stock_item_quantity= stock_count_transfer_quantity
#     stock_count_instance.save()

#     stock_count_id.delete()

#     return HttpResponseRedirect(reverse('stock'))