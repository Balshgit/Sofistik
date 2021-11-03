from typing import List

import sofistik.sof.sofistik_daten as sof_struct
from .sofistik_discover import Sofistik
from sofistik.utils import read_data_from_txt, create_image, logger


def get_plate_group(sofistik: Sofistik, db_index: int) -> str:
    cgar_data = sofistik.get_data(database_object=getattr(sof_struct, 'cgar'), obj_db_index=32,
                                  obj_db_index_sub_number=db_index, args=['m_nog',
                                                                          'm_nom',
                                                                          'm_nor',
                                                                          ])
    logger.info(f'Plate group is {cgar_data[0][0]}')
    return cgar_data[0][0]


def quad_dict_from_db(sofistik: Sofistik, db_index: int) -> dict:
    quads = sofistik.get_data(database_object=getattr(sof_struct, 'cgar_elnr'), obj_db_index=32,
                              obj_db_index_sub_number=db_index, args=['m_nr',
                                                                      ])
    quads_numbers = range(int(quads[0][0][0]), -(quads[0][0][1]) + 1)  # get list of quads belong to this db_index area

    quad_data = sofistik.get_data(database_object=getattr(sof_struct, 'cquad'), obj_db_index=200,
                                  obj_db_index_sub_number=0, args=['m_nr',
                                                                   'm_node[0]',
                                                                   'm_node[1]',
                                                                   'm_node[2]',
                                                                   'm_node[3]',
                                                                   ])

    cnode_data = sofistik.get_data(database_object=getattr(sof_struct, 'cnode'), obj_db_index=20,
                                   obj_db_index_sub_number=0, args=['m_nr',
                                                                    'm_xyz[0]',
                                                                    'm_xyz[1]',
                                                                    ])

    cgar_data = sofistik.get_data(database_object=getattr(sof_struct, 'cgar'), obj_db_index=32,
                                  obj_db_index_sub_number=2, args=['m_nog'])
    logger.info(cgar_data[0])

    # Create dict with node number and it coords
    cnodes_dict = dict()
    for node_item in cnode_data:
        cnode_number = node_item[0]
        coords = [round(node_item[i], 3) * 300 for i in range(1, len(node_item))]
        cnodes_dict[cnode_number] = coords

    # Get list of nodes coordinates from list of nodes
    def node_coords_to_tuple(nodes: list) -> List[tuple]:
        nodes_coords = []
        for node in nodes:
            nodes_coords.append(tuple(cnodes_dict[node]))
        return nodes_coords

    # Create dict with quad number and list of it nodes
    quad_dict = dict()
    for quad_item in quad_data:
        if quad_item[0] in quads_numbers:  # if quad number in quads in this area add quad
            quad_number = quad_item[0]

            nodes = [quad_item[i] for i in range(1, len(quad_item))]
            tuple_nodes_coords = node_coords_to_tuple(nodes)

            quad_dict[quad_number] = tuple_nodes_coords
            logger.info(f'{quad_number}: {tuple_nodes_coords}')

    create_image(quad=quad_dict, image_name='result/test_image_from_python.bmp')
    return quad_dict



