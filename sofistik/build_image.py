from pathlib import Path
from typing import List

import sofistik.sof.sofistik_daten as sof_struct
from sofistik.settings import SOFISTIK_YEAR
from sofistik.sofistik_discover import Sofistik
from sofistik.utils import read_data_from_file, create_image, logger, write_to_file


def quad_dict_from_db(sofistik_year: int, filepath: Path) -> dict:
    sof = Sofistik(sofistik_year=sofistik_year, filename=filepath)

    quads = sof.get_data(database_object=getattr(sof_struct, 'cgar_elnr'), obj_db_index=32,
                         obj_db_index_sub_number=2, args=['m_nr',
                                                          ])
    quads_numbers = range(int(quads[0][0][0]), -(quads[0][0][1]) + 1)
    logger.info(quads_numbers)

    quad_data = sof.get_data(database_object=getattr(sof_struct, 'cquad'), obj_db_index=200, obj_db_index_sub_number=00,
                             args=['m_nr',
                                   'm_node[0]',
                                   'm_node[1]',
                                   'm_node[2]',
                                   'm_node[3]',
                                   ])
    # logger.info(quad_data)

    cnode_data = sof.get_data(database_object=getattr(sof_struct, 'cnode'), obj_db_index=20, obj_db_index_sub_number=0,
                              args=['m_nr',
                                    'm_xyz[0]',
                                    'm_xyz[1]',
                                    ])

    # Create dict with node number and it coords
    cnodes_dict = dict()
    for node_item in cnode_data:
        cnode_number = node_item[0]
        coords = [round(node_item[i], 3) * 500 for i in range(1, len(node_item))]
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
        # logger.info(f'{quad_number}: {tuple_nodes_coords}')

    return quad_dict


def from_db(filepath: Path, save_to_file: bool = False) -> None:
    quad_dict = quad_dict_from_db(sofistik_year=SOFISTIK_YEAR, filepath=filepath)
    if save_to_file:
        write_to_file(data=quad_dict, filename='result/rectangles.txt')
    create_image(quad_dict=quad_dict, image_name='result/test_image_from_python.bmp')  # Draw rectangles!!!!


def from_txt(filepath: Path) -> None:
    quad_dict = read_data_from_file(filepath)
    create_image(quad_dict=quad_dict, image_name='result/test_image_from_python.bmp')  # Draw rectangles!!!!


if __name__ == '__main__':
    try:
        from_txt(Path('result/rectangles.txt'))
        # from_db(Path('../db/Test.cdb'))
    except Exception as e:
        logger.error(e)
        raise(e)
