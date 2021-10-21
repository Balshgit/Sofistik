# +============================================================================+
# | Company:   SOFiSTiK AG                                                     |
# | Version:   SOFiSTIK 2020                                                   |
# +============================================================================+
import os               # for the environment variable necessary, this is a great tool
import sys
import logging
import re

from sofistik_daten import *
from ctypes import *    # read the functions from the cdb
from utils import write_to_file, read_data_from_file, create_image, text_coordinates

console_logger = logging.getLogger(__name__)
formatter = logging.Formatter(datefmt="%Y.%m.%d %H:%M:%S", fmt='%(asctime)s | func name: %(funcName)s |'
                                                               ' message: %(message)s')
                              # fmt='%(asctime)s | %(levelname)s | process: %(process)d | module name: %(name)s | '
                              #     'func name: %(funcName)s | line number: %(lineno)s | message: %(message)s',)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
console_logger.setLevel(logging.INFO)
console_logger.addHandler(handler)


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
        console_logger.info(f'CDB Status: {cdb_stat.value}')
        return cdb_stat.value

    def _close_connect_to_db(self) -> None:
        # Close the CDB, 0 - will close all the files
        self._myDLL.sof_cdb_close(0)

        # Print again the status of the CDB, if status = 0 -> CDB Closed successfully
        status = self._get_cdb_status()
        if status == 0:
            console_logger.info("CDB closed successfully, status = 0")

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
            # console_logger.info(f'({all_objects})')

            RecLen = c_int(sizeof(database_object))

        self._close_connect_to_db()  # Close connection to DB
        return result


# sof = Sofistik(sofistik_year=2020, filename=r'C:\Users\Balsh\PycharmProjects\sofistik\db\Test.cdb')
#
# quad_data = sof.get_data(database_object=cquad, obj_db_index=200, obj_db_index_sub_number=0, args=['m_nr',
#                                                                                                    'm_node[0]',
#                                                                                                    'm_node[1]',
#                                                                                                    'm_node[2]',
#                                                                                                    'm_node[3]',
#                                                                                                    ])
#
#
# cnode_data = sof.get_data(database_object=cnode, obj_db_index=20, obj_db_index_sub_number=0, args=['m_nr',
#                                                                                                    'm_xyz[0]',
#                                                                                                    'm_xyz[1]',
#                                                                                                    ])
# # Create dict with node number and it coords
# cnodes_dict = dict()
# for node_item in cnode_data:
#     cnode_number = node_item[0]
#     coords = [round(node_item[i], 3) * 500 for i in range(1, len(node_item))]
#     cnodes_dict[cnode_number] = coords
#
#
# # Get list of nodes coordinates from list of nodes
# def node_coords(nodes: list) -> list:
#     nodes_coords = []
#     for node in nodes:
#         nodes_coords.append(tuple(cnodes_dict[node]))
#     return nodes_coords
#
#
# # Create dict with quad number and list of it nodes
# quad_dict = dict()
# for quad_item in quad_data:
#     quad_number = quad_item[0]
#     nodes = [quad_item[i] for i in range(1, len(quad_item))]
#     quad_dict[quad_number] = nodes
#
# # Recreate quad dict to quad number and list of it dots coordinates
# for quad_number, list_nodes in quad_dict.items():
#     nodes_list = node_coords(list_nodes)
#     quad_dict[quad_number] = nodes_list
#     console_logger.info(f'{quad_number}: {nodes_list}')


# # ------ Write to a file and extract it back --------
# write_to_file(data=quad_dict, filename='./rectangles.txt')
quad_dict = read_data_from_file('./rectangles.txt')

#  Draw rectangles!!!!
for quad_number, coords in quad_dict.items():
    rectangle = list()
    for coord in coords:
        rectangle.append(tuple(coord))
    quad_dict[quad_number] = tuple(rectangle)


#rectangles = list(quad_dict.values())

create_image(quad=quad_dict, image_name='test_image_from_python.png')


