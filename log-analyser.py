with open('sample.log','r') as file:
   error=0
   info=0
   warning=0
   for line in file:
      if 'ERROR' in line:
         error+=1
      if 'INFO' in line:
         info+=1
      if 'WARNING' in line:
         warning+=1
   total=error+info+warning
   if total==0:
       print("SYSTEM EMPTY")
   elif total!=0:
      rate=int((error/total)*100)
      if rate==0:
            print("SYSTEM STABLE")
      elif rate<=20:
         print("SYSTEM DEGRADED")
      else:
          print("SYSTEM CRITICAL")    



        
      




