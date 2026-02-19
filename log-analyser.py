error=0
info=0
warning=0
with open('sample.log','r') as file:
   for line in file:
        line = line.strip()
        print(line)
        if line.startswith('[ERROR]'):
            error += 1
        elif line.startswith('[WARNING]'):
            warning += 1
        elif line.startswith('[INFO]'):
            info += 1
   total=error+info+warning
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

       
      




