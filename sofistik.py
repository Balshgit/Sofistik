# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+

from sofistik_daten import *
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

# ---- 64 bit ---------

os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020\interfaces\64bit")
os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020")

# Get the DLL functions
myDLL = cdll.LoadLibrary("sof_cdb_w-70.dll")
py_sof_cdb_get = cdll.LoadLibrary("sof_cdb_w-70.dll").sof_cdb_get
py_sof_cdb_get.restype = c_int

py_sof_cdb_kenq = cdll.LoadLibrary("sof_cdb_w-70.dll").sof_cdb_kenq_ex
py_sof_cdb_kexist = cdll.LoadLibrary("sof_cdb_w-70.dll").sof_cdb_kexist

# ------------- 32 bit-----------------------------

# os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020\interfaces\32bit")
# os.add_dll_directory(r"C:\Program Files\SOFiSTiK\2020\SOFiSTiK 2020")
#
# # Get the DLL functions
# myDLL = cdll.LoadLibrary("cdb_w31.dll")
# py_sof_cdb_get = cdll.LoadLibrary("cdb_w31.dll").sof_cdb_get
# py_sof_cdb_get.restype = c_int
#
# py_sof_cdb_kenq = cdll.LoadLibrary("cdb_w31.dll").sof_cdb_kenq_ex

# ----------------------------------------------

# Connect to CDB
Index = c_int()
cdbIndex = 99


# input the cdb path here
# fileName = r"C:\Users\Balsh\PycharmProjects\sofistik\db\CG-Plate.cdb"
fileName = r"C:\Users\Balsh\PycharmProjects\sofistik\db\Test.cdb"

# important: Unicode call!
Index.value = myDLL.sof_cdb_init(fileName.encode('utf8'), cdbIndex)

# get the CDB status
cdbStat = c_int()
cdbStat.value = myDLL.sof_cdb_status(Index.value)


# Print the Status of the CDB
print("CDB Status:", cdbStat.value)

pos = c_int(0)
datalen = c_int(0)

a = c_int()
ie = c_int(0)
datalen.value = sizeof(cquad)

RecLen = c_int(sizeof(cquad))

"""
do while ie == 0, see cdbase.chm, Returnvalue.
    = 0 -> No error
    = 1 -> Item is longer than Data
    = 2 -> End of file reached
    = 3 -> Key does not exist
"""
# -------------
# print('IEVALUE', ie.value)
# ie.value = py_sof_cdb_get(Index, 20, 0, byref(cnode), byref(RecLen), 1)
# print('CQUAD', dir(cquad))

# print('elementnumber materialnumber material Reinf')
while ie.value < 2:
    ie.value = py_sof_cdb_get(Index, 200, 0, byref(cquad), byref(RecLen), 1)

    print("{:10d}       |     {:10d}       |  |     {}       {}     |   {:10.2f}".format(
        cquad.m_nr,      # elementnumber#
        cquad.m_node[0], cquad.m_node[1], cquad.m_node[2], cquad.m_node[3],
        # cquad.m_mat,     # materialnumber
        # cquad.m_mrf,    # material Reinf
        # cquad.m_thick[0],
    )
    )

    # Always read the length of record before sof_cdb_get is called
    RecLen = c_int(sizeof(cquad))
# -------------

# while ie.value < 2:
#     ie.value = py_sof_cdb_get(Index, 20, 0, byref(cnode), byref(RecLen), 1)
#     print("{:10d}{:10d}{:10d}{:10d}{:10.2f}{:10.2f}{:10.2f}".format(
#         cnode.m_nr,      # node-number
#         cnode.m_inr,     # internal node-number
#         cnode.m_kfix,    # degree of freedoms
#         cnode.m_ncod,    # additional bit code
#         cnode.m_xyz[0],  # x coordinates
#         cnode.m_xyz[1],  # y coordinates
#         cnode.m_xyz[2])  # z coordinates
#     )
#     RecLen = c_int(sizeof(cnode))  # Always read the length of record before sof_cdb_get is called





# Close the CDB, 0 - will close all the files
myDLL.sof_cdb_close(0)

# Print again the status of the CDB, if status = 0 -> CDB Closed successfully
cdbStat.value = myDLL.sof_cdb_status(Index.value)
if cdbStat.value == 0:
    print("CDB closed successfully, status = 0")


