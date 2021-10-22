# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+
import os               # for the environment variable necessary, this is a great tool
import re
from ctypes import *    # read the functions from the cdb
from .utils import logger


class Sofistik:

    def __init__(self, sofistik_year: int, filename: str) -> None:

        os.add_dll_directory(fr'C:\Program Files\SOFiSTiK\{sofistik_year}\SOFiSTiK {sofistik_year}\interfaces\64bit')
        os.add_dll_directory(fr'C:\Program Files\SOFiSTiK\{sofistik_year}\SOFiSTiK {sofistik_year}')

        # Get the DLL functions
        self._myDLL = cdll.LoadLibrary('sof_cdb_w-70.dll')
        self._py_sof_cdb_get = cdll.LoadLibrary('sof_cdb_w-70.dll').sof_cdb_get
        self._py_sof_cdb_get.restype = c_int
        self._py_sof_cdb_kenq = cdll.LoadLibrary('sof_cdb_w-70.dll').sof_cdb_kenq_ex
        self._py_sof_cdb_kexist = cdll.LoadLibrary('sof_cdb_w-70.dll').sof_cdb_kexist

        # Load Database file
        self._filename = fr'{filename}'  # "C:\Users\Balsh\PycharmProjects\sofistik\db\Test.cdb"

        self._Index = c_int()

    def _connect_to_db(self) -> None:

        # Connect to CDB
        cdb_index = 99
        self._Index.value = self._myDLL.sof_cdb_init(self._filename.encode('utf8'), cdb_index)
        self._get_cdb_status()

    def _get_cdb_status(self) -> int:
        # get the CDB status
        cdb_stat = c_int()
        cdb_stat.value = self._myDLL.sof_cdb_status(self._Index.value)

        # Print the Status of the CDB
        logger.info(f'CDB Status: {cdb_stat.value}')
        return cdb_stat.value

    def _close_connect_to_db(self) -> None:
        # Close the CDB, 0 - will close all the files
        self._myDLL.sof_cdb_close(0)

        # Print again the status of the CDB, if status = 0 -> CDB Closed successfully
        status = self._get_cdb_status()
        if status == 0:
            logger.info("CDB closed successfully, status = 0")

    def get_data(self, database_object, obj_db_index: int, obj_db_index_sub_number: int, args: list) -> list:

        self._connect_to_db()  # Connect to CDB

        pos = c_int(0)
        a = c_int()
        result = list()

        ie = c_int(0)
        datalen = c_int(0)
        datalen.value = sizeof(database_object)
        RecLen = c_int(sizeof(database_object))

        """
        do while ie == 0, see cdbase.chm, Returnvalue.
            = 0 -> No error
            = 1 -> Item is longer than Data
            = 2 -> End of file reached
            = 3 -> Key does not exist
        """
        while ie.value < 2:
            ie.value = self._py_sof_cdb_get(self._Index, obj_db_index, obj_db_index_sub_number,
                                            byref(database_object), byref(RecLen), 1)

            temp = list()
            for argument in args:
                ind = re.findall(r'\[\d{1}\]', argument)
                if ind and ind is not None:
                    db_item = getattr(database_object, str(argument).replace(str(ind[0]), ''))
                    ind = int(str(ind[0]).strip('[]'))
                    temp.append(db_item[ind])
                else:
                    db_item = getattr(database_object, argument)
                    temp.append(db_item)
            result.append(temp)

            # # Logger for debug TODO: delete this lines
            # all_objects = ', '.join([str(item) for item in temp])
            # logger.info(f'({all_objects})')

            RecLen = c_int(sizeof(database_object))

        self._close_connect_to_db()  # Close connection to DB
        return result
