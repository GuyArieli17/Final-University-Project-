
TRAFFIC_ROAD_ID = [0,1,2,3] 
NUMBER_OF_LANE = [3] * len(TRAFFIC_ROAD_ID)
ROAD_LENGTH= [300] * len(TRAFFIC_ROAD_ID)

NUMBER_OF_ROAD = 3
DIVISION = [0,50,150]
DIVISION_CATEGORY =  [10,10,3] 


class ClusterMannager:

    def __init__(self,traffic_road_id=TRAFFIC_ROAD_ID, number_of_lane=NUMBER_OF_LANE, road_length=ROAD_LENGTH
                        ,division=DIVISION,division_category=DIVISION_CATEGORY) -> None:
        # save info
        self.traffic_road_id = TRAFFIC_ROAD_ID
        self.number_of_lane = number_of_lane
        self.road_length = road_length
        self.division = division
        self.division_category = division_category
        # create category list
        self.road = []
        for road_idx in self.traffic_road_id:
            category = []
            self.road.append(category)
            # create cluster for each category
            for category_index in range(len(DIVISION)):
                clusters = []
                # create info list for each clustter in category
                for _ in range(0,self.division[category_index],self.division_category[category_index]):
                    clusters.append(list()) # info for each cluster
                self.category.append(clusters)
        

    def get_car_cluster_info(self,distance: float,lane_index: int):
        if distance < DIVISION[1]:#0
            category_index = 0
        elif distance < DIVISION[2]: #50
            category_index = 1
        else:
            category_index = 2 # 150
        cluster_length = DIVISION[category_index]
        cluster_num = DIVISION_CATEGORY[category_index]
        cluster_index = ((distance - cluster_length)//cluster_num)
        return self.category[category_index][cluster_index]



            



    @classmethod
    def create_clusters(cls) ->:
