# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+

import os               # for the environment variable necessary, this is a great tool
import platform         # checks the python platform
import string
from ctypes import *    # read the functions from the cdb

# This example has been tested with Python 3.7 (64-bit)
# print("The path variable=", os.environ["PATH"])

# Check the python platform (32bit or 64bit)
print("Python architecture=", platform.architecture())
sofPlatform = str(platform.architecture())

# Get the DLLs (32bit or 64bit DLL)
if sofPlatform.find("32Bit") < 0:
    # Set environment variable for the dll files
    print("Hint: 64bit DLLs are used")

# Set DLL dir path - new in PY 3.8 for ctypes
# See: https://docs.python.org/3/whatsnew/3.8.html#ctypes
# os.add_dll_directory('dlls')
# os.add_dll_directory(r"C:\sofistik_installation\2020\SOFiSTiK 2020")

# Get the DLL functions
myDLL = cdll.LoadLibrary("dlls/sof_cdb_w-70.dll")
py_sof_cdb_get = cdll.LoadLibrary("sof_cdb_w-70.dll").sof_cdb_get
py_sof_cdb_get.restype = c_int

py_sof_cdb_kenq = cdll.LoadLibrary("sof_cdb_w-70.dll").sof_cdb_kenq_ex
# else:
#     # Set environment variable for the DLL files
#     print("Hint: 32bit DLLs are used")
#
#     # Set DLL dir path - new in PY 3.8 for ctypes
#     # See: https://docs.python.org/3/whatsnew/3.8.html#ctypes
#     os.add_dll_directory(r"C:\sofistik_installation\2020\SOFiSTiK 2020\interfaces\32bit")
#     os.add_dll_directory(r"C:\sofistik_installation\2020\SOFiSTiK 2020")
#
#     # Get the DLL functions
#     myDLL = cdll.LoadLibrary("cdb_w31.dll")
#     py_sof_cdb_get = cdll.LoadLibrary("cdb_w31.dll").sof_cdb_get
#     py_sof_cdb_get.restype = c_int
#
#     py_sof_cdb_kenq = cdll.LoadLibrary("cdb_w31.dll").sof_cdb_kenq_ex

# Connect to CDB
Index = c_int()
cdbIndex = 99

# input the cdb path here
fileName = r"db/CG-Plate.cdb"

# important: Unicode call!
Index.value = myDLL.sof_cdb_init(fileName.encode('utf8'), cdbIndex)

# get the CDB status
cdbStat = c_int()
cdbStat.value = myDLL.sof_cdb_status(Index.value)

# Print the Status of the CDB
print ("CDB Status:", cdbStat.value)

# Close the CDB, 0 - will close all the files
myDLL.sof_cdb_close(0)

# Print again the status of the CDB, if status = 0 -> CDB Closed successfully
cdbStat.value = myDLL.sof_cdb_status(Index.value)
if cdbStat.value == 0:
    print ("CDB closed successfully, status = 0")