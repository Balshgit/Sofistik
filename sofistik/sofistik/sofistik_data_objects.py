from typing import List

import sofistik.sof.sofistik_daten as sof_struct
from sofistik.utils import logger

from .sofistik_discover import Sofistik


def get_plate_group(sofistik: Sofistik, area: int) -> int:
    """
    Get plate group for selected area

    :param sofistik: Sofistik main data getter
    :param area: area number is chosen by user

    :return: Plate number is used just for check data is correct
    """
    cgar_data = sofistik.get_data(database_object=getattr(sof_struct, 'cgar'), obj_db_index=32,
                                  obj_db_index_sub_number=area, args=['m_nog',
                                                                      'm_nom',
                                                                      'm_nor',
                                                                      ])
    logger.info(f'Plate group is {cgar_data[0][0]}')
    return cgar_data[0][0]


def quad_dict_from_db(sofistik: Sofistik, area: int) -> dict:
    """
    Get quads from database for selected area

    :param sofistik: Sofistik main data getter
    :param area: area number is chosen by user

    :return: Plate number is used just for check data is correct
    """
    # Get start and end numbers of quads and create range quads to check
    quads = sofistik.get_data(database_object=getattr(sof_struct, 'cgar_elnr'), obj_db_index=32,
                              obj_db_index_sub_number=area, args=['m_nr'])
    quads_in_this_area = range(int(quads[0][0][0]), -(quads[0][0][1]) + 1)  # get list of quads belong to this area

    # Get all quads from database
    quad_data = sofistik.get_data(database_object=getattr(sof_struct, 'cquad'), obj_db_index=200,
                                  obj_db_index_sub_number=0, args=['m_nr',
                                                                   'm_node[0]',
                                                                   'm_node[1]',
                                                                   'm_node[2]',
                                                                   'm_node[3]',
                                                                   ])
    # Get all nodes from database
    cnode_data = sofistik.get_data(database_object=getattr(sof_struct, 'cnode'), obj_db_index=20,
                                   obj_db_index_sub_number=0, args=['m_nr',
                                                                    'm_xyz[0]',
                                                                    'm_xyz[1]',
                                                                    ])
    scale = 450  # Scale of quad mash image

    # Create dict with node number and it coords
    cnodes_dict = dict()
    for node_item in cnode_data:
        cnode_number = node_item[0]
        coords = [round(node_item[i], 1) * scale for i in range(1, len(node_item))]
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
        quad_number = quad_item[0]
        nodes = [quad_item[i] for i in range(1, len(quad_item))]
        tuple_nodes_coords = node_coords_to_tuple(nodes)
        quad_dict[quad_number] = tuple_nodes_coords

        # Filter quads only for this area
        if quad_number not in quads_in_this_area:
            quad_dict.pop(quad_number)
            # logger.info(f'{quad_number}: {tuple_nodes_coords}')
    return quad_dict
