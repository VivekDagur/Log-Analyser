with open('sample.log','r') as file:
  error=0
  info=0
  warning=0
  for line in file:
     if 'ERROR' in line:
        error+=1
     elif 'INFO' in line:
        info+=1
     elif 'WARNING' in line:
        warning+=1
  print("Error: ",error)      
  print("Info: ", info)      
  print("Warning: ",warning)      
        
      
