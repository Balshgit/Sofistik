x = 1
result = 1144 #input te KFIX value here
value = "PXPYPZMXMYMZ"

x = 64 & result
if x > 0:
   value = "PXPYPZMXMYMZ"

x = 32 & result
if x > 0:
   value = value.replace("MZ", "")

x = 16 & result
if x > 0:
   value = value.replace("MY", "")

x = 8 & result
if x > 0:
   value = value.replace("MX", "")

x = 4 & result
if x > 0:
   value = value.replace("PZ", "")

x = 2 & result
if x > 0:
   value = value.replace("PY", "")

x = 1 & result
if x > 0:
   value = value.replace("PX", "")

# Replace the text
value = value.replace("PXPYPZ", "PP")
value = value.replace("MXMYMZ", "MM")
value = value.replace("PYPZ", "XP")
value = value.replace("PXPZ", "YP")
value = value.replace("PXPY", "ZP")
value = value.replace("MYMZ", "XM")
value = value.replace("MXMZ", "YM")
value = value.replace("MXMY", "ZM")
value = value.replace("PPMM", "F")

print(value)