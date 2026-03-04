import sys
def analyze_log(file_path):
   error=0
   info=0
   warning=0
   with open(file_path,'r') as file:
         for line in file:
            line = line.strip()
            if '[ERROR]' in line:
               error += 1
            elif '[WARNING]' in line:
               warning += 1
            elif '[INFO]' in line:
               info += 1
   total=error+info+warning
   out={
  "errors": error,
  "warnings": warning,
  "info": info,
  "total": total,
  "error_percentage": 0.0,
  "warning_percentage": 0.0,
  "info_percentage": 0.0,
  "status": "None"
}
   if total==0:
            out["status"]="SYSTEM EMPTY"
            return out
   error_percentage = (error / total) * 100
   warning_percentage = (warning / total) * 100
   info_percentage = (info / total) * 100

   out["error_percentage"] = error_percentage
   out["warning_percentage"] = warning_percentage
   out["info_percentage"] = info_percentage
   out["error_percentage"]=error_percentage 
   if error_percentage==0:
      out["status"]="SYSTEM HEALTHY"
   elif error_percentage<=20:
      out["status"]="SYSTEM DEGRADED"
   else:
      out["status"]="SYSTEM CRITICAL"
   return out   
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <logfile>")
    else:
        try:
            result = analyze_log(sys.argv[1])
            print(result)
        except FileNotFoundError:
            print("File Not Found")
        except PermissionError:
            print("Permission Denied. Cannot read the file.")

      




