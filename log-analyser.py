import sys
def analyze_log(file_path):
   error=0
   info=0
   warning=0
   try:
      with open(file_path,'r') as file:
         for line in file:
            line = line.strip()
            if '[ERROR]' in line:
               error += 1
            elif '[WARNING]' in line:
               warning += 1
            elif '[INFO]' in line:
               info += 1
   except FileNotFoundError:
        print("File not found.")
        return
   except PermissionError:
        print("Permission denied. Cannot read the file.")
        return
   total=error+info+warning
   if total==0:
            print("SYSTEM EMPTY")
            return
   rate=(error/total)*100
   if rate==0:
      print("SYSTEM STABLE")
   elif rate<=20:
      print("SYSTEM DEGRADED")
   else:
      print("SYSTEM CRITICAL")    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <logfile>")
    else:
        analyze_log(sys.argv[1])      

       
      




