from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from datetime import date
import os
import json
from web3 import Web3, HTTPProvider
import os
import pickle

global username
global contract, web3, product_name
global usersList, productList, usertype

#function to call contract
def getContract():
    global contract, web3
    blockchain_address = 'http://127.0.0.1:9545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Drug.json' #Drug contract file
    deployed_contract_address = '0x7C200D1954596c3c4A26A53541D696BdE647741f' #contract address
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
getContract()

def getUsersList():
    global usersList, contract
    usersList = []
    count = contract.functions.getUserCount().call()
    for i in range(0, count):
        user = contract.functions.getUsername(i).call()
        password = contract.functions.getPassword(i).call()
        utype = contract.functions.getUserType(i).call()
        usersList.append([user, password, utype])

def getProductList():
    global productList, contract
    productList = []
    count = contract.functions.getProductCount().call()
    for i in range(0, count):
        owner = contract.functions.getOwner(i).call()
        pid = contract.functions.getProductid(i).call()
        pname = contract.functions.getProductname(i).call()
        desc = contract.functions.getDesc(i).call()
        img = contract.functions.getImage(i).call()
        dd = contract.functions.getDate(i).call()
        ttype = contract.functions.getTracing(i).call()
        status = contract.functions.getStatus(i).call()
        location = contract.functions.getLocation(i).call()
        productList.append([owner, pid, pname, desc, img, dd, ttype, location, status])
getUsersList()
getProductList()

def ViewStake(request):
    if request.method == 'GET':
        global usersList
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Username</font></th>'
        output+='<th><font size=3 color=black>Password</font></th>'
        output+='<th><font size=3 color=black>User Type</font></th></tr>'
        for i in range(len(usersList)):
            ulist = usersList[i]
            output+='<tr><td><font size=3 color=black>'+ulist[0]+'</font></td>'
            output+='<td><font size=3 color=black>'+ulist[1]+'</font></td>'
            output+='<td><font size=3 color=black>'+str(ulist[2])+'</font></td></tr>'                    
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)

def AdminLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        status = "AdminLogin.html"
        output = 'Invalid login details'
        if username == 'admin' and password == 'admin':
            context = {'data':"Welcome "+username}
            status = "AdminScreen.html"
            output = 'Welcome '+username             
        context= {'data':output}
        return render(request, status, context)
    
def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})    

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})
    
def AddStake(request):
    if request.method == 'GET':
       return render(request, 'AddStake.html', {})

def GenerateOrders(request):
    if request.method == 'GET':
       return render(request, 'GenerateOrders.html', {})

def ConsumerTracing(request):
    if request.method == 'GET':
        return render(request, 'ConsumerTracing.html', {})

def UserMap(request):
    if request.method == 'GET':
        name = request.GET.get('t1', False)
        output = '<iframe width="625" height="650" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q='+name+'&amp;ie=UTF8&amp;&amp;output=embed"></iframe><br/>'
        context= {'data':output}
        return render(request, 'ViewOutput.html', context)    
    
    
def ConsumerTracingAction(request):
    if request.method == 'POST':
        global productList
        pid = request.POST.get('t1', False)
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Owner Name</font></th>'
        output+='<th><font size=3 color=black>Product Id</font></th>'
        output+='<th><font size=3 color=black>Product Name</font></th>'
        output+='<th><font size=3 color=black>Description</font></th>'
        output+='<th><font size=3 color=black>Update Date</font></th>'
        output+='<th><font size=3 color=black>Tracing Type</font></th>'
        output+='<th><font size=3 color=black>Location</font></th>'
        output+='<th><font size=3 color=black>Tracing Status</font></th>'
        output+='<th><font size=3 color=black>Image</font></th>'
        output+='<th><font size=3 color=black>View on Map</font></th></tr>'
        for i in range(len(productList)):
            plist = productList[i]
            if plist[1] == pid:
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'UserMap?t1='+str(plist[7])+'\'><font size=3 color=black>View on Map</font></a></td></tr>'
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'ViewOutput.html', context)

def AdminMap(request):
    if request.method == 'GET':
        name = request.GET.get('t1', False)
        output = '<iframe width="625" height="650" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?q='+name+'&amp;ie=UTF8&amp;&amp;output=embed"></iframe><br/>'
        context= {'data':output}
        return render(request, 'AdminMap.html', context)    

def ViewAdminTracingAction(request):
    if request.method == 'POST':
        global productList
        pid = request.POST.get('t1', False)
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Owner Name</font></th>'
        output+='<th><font size=3 color=black>Product Id</font></th>'
        output+='<th><font size=3 color=black>Product Name</font></th>'
        output+='<th><font size=3 color=black>Description</font></th>'
        output+='<th><font size=3 color=black>Update Date</font></th>'
        output+='<th><font size=3 color=black>Tracing Type</font></th>'
        output+='<th><font size=3 color=black>Location</font></th>'
        output+='<th><font size=3 color=black>Tracing Status</font></th>'
        output+='<th><font size=3 color=black>Image</font></th>'
        output+='<th><font size=3 color=black>View Map</font></th></tr>'
        for i in range(len(productList)):
            plist = productList[i]
            if plist[1] == pid:
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'AdminMap?t1='+str(plist[7])+'\'><font size=3 color=black>View on Map</font></a></td></tr>'       
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)    

def AdminTracing(request):
    if request.method == 'GET':
        global productList
        output = '<tr><td><font size="" color="black">Product&nbsp;ID</font></td>'
        output +='<td><select name="t1">'
        for i in range(len(productList)):
            plist = productList[i]
            output += '<option value="'+plist[1]+'">'+plist[1]+'</option>'
        output += '</select></td></tr>'
        context= {'data':output}
        return render(request, 'AdminTracing.html', context)        

def getProductId():
    global productList
    pname = []
    for i in range(len(productList)):
        plist = productList[i]
        if plist[2] not in pname:
            pname.append(plist[2])
    return len(pname) + 1

def UpdateTracingAction(request):
    if request.method == 'GET':
        global product_name, username, usertype
        product_name = request.GET['pname']
        tracing = request.GET['tracing']                   
        output = '<tr><td><font size="" color="black">Product&nbsp;Name</font></td>'
        output += '<td><input type="text" name="t1" style="font-family: Comic Sans MS" size="30" value='+product_name+' readonly/></td></tr>'
        output += '<tr><td><font size="" color="black">Next&nbsp;Tracing</font></td>'
        output += '<td><input type="text" name="t2" style="font-family: Comic Sans MS" size="30" value='+tracing+' readonly/></td></tr>'
        context= {'data':output}
        return render(request, 'AddTracing.html', context)    

def getCounter(pid):
    global productList
    count = 0
    for i in range(len(productList)):
        plist = productList[i]
        if plist[1] == pid:
            count += 1
    return count

def AddTracingAction(request):
    if request.method == 'POST':
        product_id = request.POST.get('t1', False)
        tracing_type = request.POST.get('t2', False)
        location = request.POST.get('t3', False)
        today = str(date.today())
        temp = None
        today = str(date.today())
        for i in range(len(productList)):
            plist = productList[i]
            if plist[1] == product_id:
                temp = plist
                break
        msg = contract.functions.createProduct(temp[0], product_id, temp[2], temp[3], temp[4], today, tracing_type, location, tracing_type).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
        productList.append([temp[0], product_id, temp[2], temp[3], temp[4], today, tracing_type, location, tracing_type])
        context= {'data':"Tracing details updated"}
        return render(request, 'StakeScreen.html', context)

def UpdateTracing(request):
    if request.method == 'GET':
        global productList, usertype, username
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Owner Name</font></th>'
        output+='<th><font size=3 color=black>Product Id</font></th>'
        output+='<th><font size=3 color=black>Product Name</font></th>'
        output+='<th><font size=3 color=black>Description</font></th>'
        output+='<th><font size=3 color=black>Update Date</font></th>'
        output+='<th><font size=3 color=black>Tracing Type</font></th>'
        output+='<th><font size=3 color=black>Location</font></th>'
        output+='<th><font size=3 color=black>Tracing Status</font></th>'
        output+='<th><font size=3 color=black>Image</font></th>'
        output+='<th><font size=3 color=black>Update New Tracing Info</font></th></tr>'
        for i in range(len(productList)):
            plist = productList[i]
            counter = getCounter(plist[1])
            if counter == 1 and usertype == 'Raw Material Supplier' and plist[6] == 'Raw Material Supplier':
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'UpdateTracingAction?pname='+plist[1]+'&tracing="Manufacturer"\'><font size=3 color=black>Click Here</font></a></td></tr>'
            if counter == 2 and usertype == 'Manufacturer' and plist[6] == 'Manufacturer':
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'UpdateTracingAction?pname='+plist[1]+'&tracing="Distributor"\'><font size=3 color=black>Click Here</font></a></td></tr>'
            if counter == 3 and usertype == 'Distributor' and plist[6] == 'Distributor':
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'UpdateTracingAction?pname='+plist[1]+'&tracing="Retailer"\'><font size=3 color=black>Click Here</font></a></td></tr>'
            if counter == 4 and usertype == 'Retailer' and plist[6] == 'Retailer':
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[2])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><img src="/static/products/'+plist[4]+'" width="200" height="200"></img></td>'
                output+='<td><a href=\'UpdateTracingAction?pname='+plist[1]+'&tracing="Sold"\'><font size=3 color=black>Click Here</font></a></td></tr>'    
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'StakeScreen.html', context) 
          
def GenerateOrdersAction(request):
    if request.method == 'POST':
        global username, productList
        cname = request.POST.get('t1', False)
        desc = request.POST.get('t4', False)
        image = request.FILES['t5']
        imagename = request.FILES['t5'].name
        location = request.POST.get('t6', False)
        pid = cname+"-"+str(getProductId())
        today = str(date.today())

        fs = FileSystemStorage()
        msg = contract.functions.createProduct(username, str(pid), cname, desc, imagename, today, 'Raw Material Supplier', location, 'Raw Material Supplier').transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
        if os.path.exists('DrugApp/static/products/'+imagename):
            os.remove('DrugApp/static/products/'+imagename)
        filename = fs.save('DrugApp/static/products/'+imagename, image)
        productList.append([username, str(pid), cname, desc, imagename, today, 'Raw Material Supplier', location, 'Raw Material Supplier'])
        context= {'data':"Order details saved in Blockchain<br/><br/>"+str(tx_receipt)}
        return render(request, 'GenerateOrders.html', context)        
   
def AddStakeAction(request):
    if request.method == 'POST':
        global usersList
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        contact = request.POST.get('contact', False)
        utype = request.POST.get('type', False)
        count = contract.functions.getUserCount().call()
        status = "none"
        for i in range(0, count):
            user1 = contract.functions.getUsername(i).call()
            if username == user1:
                status = "exists"
                break
        if status == "none":
            msg = contract.functions.createUser(username, password, contact, utype).transact()
            tx_receipt = web3.eth.waitForTransactionReceipt(msg)
            usersList.append([username, password, utype])
            context= {'data':'New Stakeholder details added<br/>'+str(tx_receipt)}
            return render(request, 'AddStake.html', context)
        else:
            context= {'data':'Given username already exists'}
            return render(request, 'AddStake.html', context)

def StakeLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList, usertype
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        utype = request.POST.get('type', False)
        status = "StakeLogin.html"
        output = 'Invalid login details'
        for i in range(len(usersList)):
            ulist = usersList[i]
            user1 = ulist[0]
            pass1 = ulist[1]
            if user1 == username and pass1 == password and utype == ulist[2]:
                if utype == 'Raw Material Supplier':
                    usertype = utype
                elif utype == 'Manufacturer':
                    usertype = utype
                elif utype == 'Distributor':
                    usertype = utype
                elif utype == 'Retailer':
                    usertype = utype     
                status = "StakeScreen.html"
                output = 'Welcome '+username+"<br/>User Type : "+usertype
                break        
        context= {'data':output}
        return render(request, status, context)

def StakeLogin(request):
    if request.method == 'GET':
       return render(request, 'StakeLogin.html', {})
    

