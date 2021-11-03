from typing import List
import sofistik.sof.sofistik_daten as sof_struct
from sofistik.utils import write_to_file, read_data_from_txt, create_image, logger
from sofistik.sofistik_discover import Sofistik
from sofistik.settings import SOFISTIK_YEAR


def quad_dict_from_db(sofistik_year: int, db_path: str) -> dict:
    sof = Sofistik(sofistik_year=sofistik_year, filename=fr'{db_path}')

    quads = sof.get_data(database_object=getattr(sof_struct, 'cgar_elnr'), obj_db_index=32,
                                  obj_db_index_sub_number=1, args=['m_nr',
                                                                   ])
    for quad in quads:
        for item in quad:
            logger.info(list(item))
    quad_data = sof.get_data(database_object=getattr(sof_struct, 'cquad'), obj_db_index=200, obj_db_index_sub_number=00,
                             args=['m_nr',
                                   'm_node[0]',
                                   'm_node[1]',
                                   'm_node[2]',
                                   'm_node[3]',
                                   ])
    #logger.info(quad_data)

    cnode_data = sof.get_data(database_object=getattr(sof_struct, 'cnode'), obj_db_index=20, obj_db_index_sub_number=0,
                              args=['m_nr',
                                    'm_xyz[0]',
                                    'm_xyz[1]',
                                    ])

    cgar_data = sof.get_data(database_object=getattr(sof_struct, 'cgar'), obj_db_index=32, obj_db_index_sub_number=2,
                             args=['m_nog'])
    logger.info(cgar_data[0])

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
        #logger.info(f'{quad_number}: {tuple_nodes_coords}')

    return quad_dict


# # ------ Write data to a file and extract it back --------
# write_to_file(data=quad_dict, filename='result/rectangles.txt')


def quad_dict_from_file(filename: str) -> dict:
    quad_dict = read_data_from_txt(filename)
    return quad_dict


def main(filepath: str) -> None:

    # Read data
    # 'C:\Users\Balsh\PycharmProjects\sofistik\db\Test.cdb')
    quad_dict = quad_dict_from_db(sofistik_year=SOFISTIK_YEAR, db_path=filepath)
    # quad_dict = quad_dict_from_txt(filepath)#filename='result/rectangles.txt')

    # Draw rectangles!!!!
    create_image(quad=quad_dict, image_name='result/test_image_from_python.bmp')


if __name__ == '__main__':
    main(r'C:\Users\Balsh\PycharmProjects\Sofistik_project\db\Test.cdb')
