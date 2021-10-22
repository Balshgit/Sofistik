from typing import List
from sofistik.sofistik_daten import *
from sofistik.utils import write_to_file, read_data_from_file, create_image, logger
from sofistik.sofistik_discover import Sofistik


if __name__ == '__main__':
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
    # def node_coords_to_tuple(nodes: list) -> List[tuple]:
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
    #
    #     nodes = [quad_item[i] for i in range(1, len(quad_item))]
    #     tuple_nodes_coords = node_coords_to_tuple(nodes)
    #
    #     quad_dict[quad_number] = tuple_nodes_coords
    #     logger.info(f'{quad_number}: {tuple_nodes_coords}')

    # # ------ Write data to a file and extract it back --------
    # write_to_file(data=quad_dict, filename='result/rectangles.txt')
    quad_dict = read_data_from_file('result/rectangles.txt')

    #  Draw rectangles!!!!

    create_image(quad=quad_dict, image_name='result/test_image_from_python.png')