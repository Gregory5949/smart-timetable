import logging
from prettytable import PrettyTable
from pathlib import Path
from timetable_builder import *

logging.basicConfig(level=logging.INFO)


def main():
    # Read data
    # data = Database()
    # data.load_from_dir(Path("modeus-data"))
    # genetic_algorithm = GeneticAlgorithm(data)
    # next = genetic_algorithm.run(data)
    # # # for i in range(len(next)):
    # # #     print(len(next[i].timetable))
    # best = sorted(next, reverse=True, key=lambda x: x.fitness)[0]
    # print(best.fitness, best.timetable)
    # best_so_far1 = [EventRealization(event_id='7d27a180-9116-4dad-a61d-e4b34638b2f8', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 7)), EventRealization(event_id='9b992ddd-1450-4211-970a-0133325bab64', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b958349f-2764-4d36-bb96-dfdfc595c884', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='b7c48b95-e628-4627-ad47-44ba3bbc1eb0', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='1a6a6fac-09ac-4202-996c-e1e1620db133', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='734b1bc3-4c18-46c8-b2ec-0d0a8e8a9377', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='6ff51783-7f2c-4537-a5a7-f6f3aa2c8139', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 9)), EventRealization(event_id='9ec311b7-56dd-4eb7-9c46-8849ae2e8f03', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 9)), EventRealization(event_id='2aadf171-63d1-4042-9e08-07d184a0b683', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 9)), EventRealization(event_id='db93dbf4-d6d4-4baf-8a3f-7ef9cd3b0f38', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 9)), EventRealization(event_id='fe08df4f-4d32-4153-9d15-141ac9c06c5a', room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 10)), EventRealization(event_id='079fcd54-9793-412b-b35b-a97d175692c4', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 10)), EventRealization(event_id='63457700-c6c5-402b-89a6-6c7949cddd24', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 10)), EventRealization(event_id='95cab579-6c09-4201-8f8b-a0c36ed806b8', room_id='a5be3cfe-6d27-4f25-9030-a81a94590190', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 10)), EventRealization(event_id='7e72abc4-1d4d-45cc-b06a-dbad25b668e1', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 11)), EventRealization(event_id='1fae969b-e834-442f-afea-f4719526f704', room_id='8dcbd51f-71c6-4f97-8ef5-5f258dbca1f5', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='162ee721-344c-4404-94b8-2d41dc922a65', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 11))]
    # for i in  best_so_far1:
    #     print(i.event_id, i.room_id, i.grid_slot_id, i.date)
#0.5
    # best_so_far = [EventRealization(event_id='01d539b7-979e-49ca-9964-09968c2234e0', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b0794808-9e31-4c7c-9f74-b5d9f93bea9a', room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b92039f2-de51-4d2f-80b2-7dfbab47e150', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='5e6bae83-f4fb-4f92-a760-a79c33d2c075', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='aa5522e5-d850-4719-9a2f-7d36b65bfc2b', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 8)), EventRealization(event_id='c7787f52-841a-4c1a-82c2-c70dd9e5e0db', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='5ae35dd1-dfea-4ea3-975c-ad441757fc02', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='a72d6dbf-352a-4f75-80a3-350c672024a0', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 9)), EventRealization(event_id='9536095d-b2c0-479a-848e-d79e1da129d6', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 9)), EventRealization(event_id='27975c54-e8fb-4a5d-bf7c-cfb3bfb7e988', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 9)), EventRealization(event_id='5c9dadaf-53f5-425c-88ac-e0016ae1f6e9', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 10)), EventRealization(event_id='5f5fcca1-6382-441c-9f08-14d984913dfd', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 10)), EventRealization(event_id='2ba3543c-2e38-4982-813f-1b694fb5f513', room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='0a05fb8a-a840-44a8-8b11-ed63d9ab349b', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 10)), EventRealization(event_id='d882780f-bb8f-4ee8-8daa-42b4f1f1483a', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='a85bd769-10d3-49b6-a1af-f104e6c815c1', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 11)), EventRealization(event_id='20cde08a-decf-4885-8b3e-5e9f8d5c1c66', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10)), EventRealization(event_id='f4416ac8-c057-47ea-84f8-f1623246a95c', room_id='8dcbd51f-71c6-4f97-8ef5-5f258dbca1f5', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='1055d99a-d111-4807-8a86-7caa93318bfd', room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 11))]


    # best = [EventRealization(event_id='db624e1a-1d8e-48ed-926f-d4528256b48f', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 7)), EventRealization(event_id='7aeebaed-0a01-4604-a0cc-a3b2f5dca1a0', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 7)), EventRealization(event_id='78ab5d7c-a535-47f8-9b7d-ff072a372b29', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 7)), EventRealization(event_id='bf9d2645-c314-404f-a765-4c9edc8b8c7a', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 7)), EventRealization(event_id='1c789707-d367-40bb-9a0d-7b49deabcc95', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='12957139-f0ba-4325-8e19-b02975ce0ec1', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='4f44d7cb-5c6f-4b5c-b7cc-1bec7b0fa199', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 8)), EventRealization(event_id='45f07ad1-3a4c-4fe3-91c2-a1a8b9c34273', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='1d0d4d98-26ce-47b0-ba42-a4840b39a880', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='ca0912ad-4216-4fdf-9b49-941bf1d8df6c', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 9)), EventRealization(event_id='7a6c2a13-d8d5-4bc5-820e-ce9b333a2cf1', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 9)), EventRealization(event_id='27248ada-d041-4515-a881-1367a0ed12d5', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='4797648f-58f2-48e0-9e5b-59d3dceff683', room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 10)), EventRealization(event_id='3bf2fcad-6a26-4521-bb46-cfb74f169dcb', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10)), EventRealization(event_id='ee9d9d50-8a3b-440c-9cb8-4d8e92591fe5', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 10))]

    # best1 = [EventRealization(event_id='c93ec520-7be5-4d7d-8eab-242c5d599fc6', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='0c71c02c-c033-4ebc-a19f-0b847e563fa8', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 7)), EventRealization(event_id='2ee9e07e-ad34-4582-84fe-dbb601719554', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b94dada7-1cdd-4041-bc29-250263fce40a', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='e7654be3-50e7-4fab-91b6-e5d752c634eb', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 8)), EventRealization(event_id='c708913a-f01d-4efb-bc54-3c617e14f590', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='8e73cdab-16d5-40c1-aa00-11b705577cb4', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ba29718f-6f9a-4acb-88e3-99da63b12766', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ad7c0e40-f88a-4bd4-9dc0-fc9d8d413251', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='f7e125d2-e5be-4944-aec1-e8d10eb6abb2', room_id='e40dff05-196e-4eca-9d1e-ce1d866311a1', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 9)), EventRealization(event_id='6a016a05-fde4-40e1-9da9-2e5181a7de4a', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='00946251-b123-419a-b5e7-ded276da00ea', room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='da9ac66d-5849-4ed3-958b-504e9b53c7e8', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 10)), EventRealization(event_id='e0b06908-1000-403b-8a6f-17f8b8880733', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10)), EventRealization(event_id='0f69b345-87a3-4e06-a198-a3c66590fe70', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 10)), EventRealization(event_id='8bef4153-0648-4a06-925e-03993a1a3b9a', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10)), EventRealization(event_id='d1ba21fd-6bbd-4efa-899a-e3eec08dcddd', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 11))]
    # best2 = [EventRealization(event_id='39ca2f26-5483-42bf-98fb-73f264848969', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 7)), EventRealization(event_id='91171841-4f64-49e8-8f5e-c6a0c473f0e6', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='6783695f-bf28-4265-bfe7-0872ca97473f', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 7)), EventRealization(event_id='83722290-a6a2-4351-a879-d5e44fae599b', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 7)), EventRealization(event_id='055ac618-acd9-45b3-afdc-c38b4434fdae', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='7101203d-2dff-421f-b9ee-2ca4e13b609b', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='84f39f09-b2d8-4234-b54a-3e11a48a9c9d', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='a1853fcd-e05a-46a5-8c58-fb869626c87d', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='16d4b92f-d1bd-421b-9a24-9f3c3bf71734', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='2b890594-7888-48d7-a7a8-3f736e8ccc7e', room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 9)), EventRealization(event_id='81931977-d61a-4071-b489-bb68f39b9081', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 9)), EventRealization(event_id='1639b54c-dc20-4914-8bfc-90138a335270', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='92a71c56-dd5c-429e-b3e3-52ca66ab87c5', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 10)), EventRealization(event_id='a537717f-35d3-4295-b589-af439548970b', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='23639c41-ba18-419d-9e6e-88502cc7a042', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 11)), EventRealization(event_id='011b7470-b324-44ef-b1c0-de490a1e9eaf', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='ab10f10f-bf3f-4916-a702-5146d26add67', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12))]
    # best3 = [EventRealization(event_id='11ece1d5-2bda-4275-b741-728f2bd8344c', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 7)), EventRealization(event_id='32697337-a442-4828-939d-d616bafed93f', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 7)), EventRealization(event_id='be08403d-cabc-4074-8c66-74f47efb9273', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 7)), EventRealization(event_id='d016cb02-7eba-4487-8e61-25006e9b61d3', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='605a73eb-d8c2-434b-86ef-5b1ecfc3335e', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 7)), EventRealization(event_id='d4c8f733-991b-4d00-8cd5-79f07e725118', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ebe47ccd-0f6a-4984-ada6-d8d235b6ba9f', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 8)), EventRealization(event_id='54bd8442-eb41-4d60-9096-fbc1d380d02a', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='2fafe7de-9801-4abd-8523-ab4d9ccfdb92', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='4ebf686b-acc2-409c-af7b-ec15ee9781c5', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 8)), EventRealization(event_id='a27cbfa2-7d59-4a72-87a6-58a29b0c6a38', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 9)), EventRealization(event_id='9707d994-4431-4028-9a6b-42d5652d6e5e', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='16564f98-ca06-464e-8be2-19e32b77b930', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 9)), EventRealization(event_id='32750e72-5421-4f75-ab30-cd422d91ef8f', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 10)), EventRealization(event_id='ac6f79e8-f9c3-4ceb-971a-f5fd98ecc6dd', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 10)), EventRealization(event_id='dd9407c8-a2ea-46cf-9ce6-06f7816adccf', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10)), EventRealization(event_id='c4539758-c16e-4894-866d-31e8a0abd0dd', room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 10))]
    # best4 = [EventRealization(event_id='c93ec520-7be5-4d7d-8eab-242c5d599fc6', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 7)), EventRealization(event_id='0c71c02c-c033-4ebc-a19f-0b847e563fa8', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='2ee9e07e-ad34-4582-84fe-dbb601719554', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b94dada7-1cdd-4041-bc29-250263fce40a', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 7)), EventRealization(event_id='e7654be3-50e7-4fab-91b6-e5d752c634eb', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='c708913a-f01d-4efb-bc54-3c617e14f590', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='8e73cdab-16d5-40c1-aa00-11b705577cb4', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ba29718f-6f9a-4acb-88e3-99da63b12766', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ad7c0e40-f88a-4bd4-9dc0-fc9d8d413251', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='f7e125d2-e5be-4944-aec1-e8d10eb6abb2', room_id='e40dff05-196e-4eca-9d1e-ce1d866311a1', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 9)), EventRealization(event_id='6a016a05-fde4-40e1-9da9-2e5181a7de4a', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 9)), EventRealization(event_id='00946251-b123-419a-b5e7-ded276da00ea', room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='da9ac66d-5849-4ed3-958b-504e9b53c7e8', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 10)), EventRealization(event_id='e0b06908-1000-403b-8a6f-17f8b8880733', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='0f69b345-87a3-4e06-a198-a3c66590fe70', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 11)), EventRealization(event_id='8bef4153-0648-4a06-925e-03993a1a3b9a', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='d1ba21fd-6bbd-4efa-899a-e3eec08dcddd', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12))]
    # best5 = [EventRealization(event_id='ba29718f-6f9a-4acb-88e3-99da63b12766', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 8)), EventRealization(event_id='ad7c0e40-f88a-4bd4-9dc0-fc9d8d413251', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 9)), EventRealization(event_id='f7e125d2-e5be-4944-aec1-e8d10eb6abb2', room_id='e40dff05-196e-4eca-9d1e-ce1d866311a1', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 9)), EventRealization(event_id='6a016a05-fde4-40e1-9da9-2e5181a7de4a', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 9)), EventRealization(event_id='00946251-b123-419a-b5e7-ded276da00ea', room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 10)), EventRealization(event_id='da9ac66d-5849-4ed3-958b-504e9b53c7e8', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 10)), EventRealization(event_id='e0b06908-1000-403b-8a6f-17f8b8880733', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='0f69b345-87a3-4e06-a198-a3c66590fe70', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 11)), EventRealization(event_id='8bef4153-0648-4a06-925e-03993a1a3b9a', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='d1ba21fd-6bbd-4efa-899a-e3eec08dcddd', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12))]
    # best 5 --- самаое лучшее
    # best = [best1,best2,best3,best4,best5]
    # for i in best:
    #     for j in i:
    #         print(j.event_id, j.room_id, j.grid_slot_id, j.date)
    #     print(calculate_fitness(data, i))

    #искалось 1 час 1 минуту кол-во эпох: 1, размер популяции: 10000 фитнес: 0,05, что нормально для расписаний больше, чем на 7 дней.
    best_14days = [EventRealization(event_id='0e6e5454-23da-4b38-a6f4-cf03c2a68261', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 7)), EventRealization(event_id='7e1d1836-add2-49d2-ab69-305fb01b2978', room_id='e40dff05-196e-4eca-9d1e-ce1d866311a1', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 7)), EventRealization(event_id='b87db879-4b59-4732-a380-805d47a0790e', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 7)), EventRealization(event_id='09a2dc4e-7b12-4ade-9663-37d54ea83cd5', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 7)), EventRealization(event_id='1b911012-3003-44ea-ae50-fbaaf91a7852', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 7)), EventRealization(event_id='88188133-9e68-4b20-8b96-a44697219c1f', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 8)), EventRealization(event_id='29bbf1e2-3116-405d-a209-a9fb16e7925f', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 8)), EventRealization(event_id='c3fbb218-f675-458b-8928-a227193acb38', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 8)), EventRealization(event_id='b0283e91-deb3-43cb-bd14-32a8fc368529', room_id='8dcbd51f-71c6-4f97-8ef5-5f258dbca1f5', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 8)), EventRealization(event_id='d1d79337-b133-418d-b985-44cc8b6cd18e', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 9)), EventRealization(event_id='49ccd436-64c8-4fe8-a990-9fc8a10944f6', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 9)), EventRealization(event_id='3cdfe882-45e7-435c-b074-e1b961977838', room_id='1bf7559f-f5d0-4f81-9bd0-a5fa9e889b0e', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 10)), EventRealization(event_id='2b2676a8-e2a4-46c7-ace6-3f407e4febbb', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 10)), EventRealization(event_id='874b473b-d99f-4e89-8744-0b5f7527e401', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 10)), EventRealization(event_id='04c2d147-9205-4605-8674-ffd1860106d9', room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 10)), EventRealization(event_id='9a9fb428-928b-415c-856f-9fb54a37da93', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 11)), EventRealization(event_id='35791dd9-772c-48e8-bfc7-3a9af4de6ddd', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.04', date=datetime.date(2022, 2, 11)), EventRealization(event_id='17170c90-24dd-4a57-8134-f7dc65de26a5', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 11)), EventRealization(event_id='73797808-4418-493f-830f-9cff665c6bf5', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 11)), EventRealization(event_id='62de17f6-a1fd-4447-a6d1-6b7d331e0cc2', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 12)), EventRealization(event_id='f59bd5e4-71f6-431b-bd56-ad6a190faf23', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 12)), EventRealization(event_id='9113b64f-17b5-45e7-adaf-2d714ebc2574', room_id='1645c9e5-eafe-4c3a-a12a-7f5a62792ab8', grid_slot_id='Grid.05.01', date=datetime.date(2022, 2, 14)), EventRealization(event_id='c28d169a-c39f-4d03-b3f8-5d0566de10b4', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 14)), EventRealization(event_id='82022d97-d7e9-43b3-be1e-884afa376231', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 14)), EventRealization(event_id='a0267d83-d7b9-454a-8f73-b2f0175a3ed7', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 15)), EventRealization(event_id='db7f827c-7979-47e2-83be-cba2506bdc3d', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 15)), EventRealization(event_id='bc78eebc-f804-4a1a-8b59-74ba6dc7ecbd', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 15)), EventRealization(event_id='7dc6a914-1a41-4d9c-bbeb-0e58a334ab8b', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 16)), EventRealization(event_id='fdb9a9f6-e1bf-4c70-8551-40ec667f4146', room_id='5d1b3245-b89a-4e38-97f9-9840b9604842', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 16)), EventRealization(event_id='48e9d9ad-b788-4477-8676-b2d72984d64b', room_id='e17b77cf-c3cc-485f-b05f-cc3194caa915', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 17)), EventRealization(event_id='f5bb0107-8d85-418d-ae6d-8ab9dc484321', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 17)), EventRealization(event_id='557b9243-a56e-45b1-bf4d-1ce2aac0c43d', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 18)), EventRealization(event_id='ca1cf131-68ca-472b-ba3d-09fb7362d187', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 18)), EventRealization(event_id='47357718-e642-4ae8-81e7-51ff06f87160', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 18)), EventRealization(event_id='6e5703c3-603d-4755-8cdc-a205ce374291', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 18)), EventRealization(event_id='b18542cc-efb6-4efc-9d5b-50d1acd79a31', room_id='c4e90356-74fc-44ef-bcf5-0fe8e0477d56', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 19)), EventRealization(event_id='68d53df5-9be6-4f6b-811a-5ef70590d9dc', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.03', date=datetime.date(2022, 2, 19)), EventRealization(event_id='6c282d2a-c0da-41c5-86f6-23d45e693871', room_id='8cf16536-8a8d-4a92-97a6-39626504a927', grid_slot_id='Grid.05.08', date=datetime.date(2022, 2, 21)), EventRealization(event_id='8e3c988a-7aa5-4d90-8bea-30430f83d0cc', room_id='4e6f7517-3a39-4351-9e61-966c2f35e5fe', grid_slot_id='Grid.05.06', date=datetime.date(2022, 2, 21)), EventRealization(event_id='379ff0cb-7f12-4a64-aa44-b8d5dc8512b0', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 21)), EventRealization(event_id='ae87f70d-1ed8-43e1-8898-5319c078e974', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.07', date=datetime.date(2022, 2, 21)), EventRealization(event_id='f82a4939-22fd-44de-8f9d-9984716b892f', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.05', date=datetime.date(2022, 2, 21)), EventRealization(event_id='65720ad9-08d5-445c-a18b-88f8b0faacb3', room_id='327f1e29-3951-4d5e-b503-1a8aa5cb1d21', grid_slot_id='Grid.05.02', date=datetime.date(2022, 2, 22))]

    for i in best_14days:
        print(i.event_id, i.room_id, i.grid_slot_id, i.date)
if __name__ == "__main__":
    main()
