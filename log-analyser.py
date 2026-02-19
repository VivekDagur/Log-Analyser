with open('sample.log','r') as file:
   error=0
   info=0
   warning=0
   for line in file:
      if 'ERROR' in line:
         error+=1
      elif 'WARNING' in line:
         warning+=1
      elif 'INFO' in line:
         info+=1
   total=error+info+warning
   print(error)
   print(info)
   print(warning)
   if total==0:
       print("SYSTEM EMPTY")
   else:
      rate=int((error/total)*100)
      if rate==0:
            print("SYSTEM STABLE")
      elif rate<=20:
         print("SYSTEM DEGRADED")
      else:
          print("SYSTEM CRITICAL")    



        
      




