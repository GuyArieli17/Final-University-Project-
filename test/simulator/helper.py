import numpy as np
TRAFFIC_ROAD_ID = [0,1,2,3] 
NUMBER_OF_LANE = [3] * len(TRAFFIC_ROAD_ID)
ROAD_LENGTH= [300] * len(TRAFFIC_ROAD_ID)

NUMBER_OF_ROAD = 3
DIVISION = [0,50,150,300]
DIVISION_LENGTH =  [5,10,50] 


class ClusterMannager:

    def _build_first_category_clusters(self,category_index = 1):
        lanes = []
        # create info list for each clustter in category
        for lane_idx in range(self.number_of_lane[0]):
            clusters = []
            # create info list for each clustter in category
            form_dist = self.division[category_index-1]
            to = self.division[category_index]
            step = self.division_length[category_index-1]
            for _ in range(form_dist,to,step):
                clusters.append([np.zeros(2)]) # info for each cluster
            lanes.append(np.array(clusters))
        return np.array(lanes)

    def _build_category_clusters(self,category_index):
        clusters = []
        # create info list for each clustter in category
        form_dist = self.division[category_index-1]
        to = self.division[category_index]
        step = self.division_length[category_index-1]
        for _ in range(form_dist,to,step):
            clusters.append([0,0]) # info for each cluster
        return np.array(clusters)
    
    def _build_mapper(self):
        for road_idx in self.traffic_road_id:
            category = list()
            # create cluster for each category
            for category_index in range(1,len(self.division)):
                # if category_index == 1:
                #     clusters = self._build_first_category_clusters()
                # else:
                clusters = self._build_category_clusters(category_index)
                category.append(clusters)
            self.mapper[road_idx] = np.array(category,dtype=object)
            # category.append(clusters)
        


    def __init__(self,traffic_road_id=TRAFFIC_ROAD_ID, number_of_lane=NUMBER_OF_LANE, road_length=ROAD_LENGTH
                        ,division=DIVISION,division_length=DIVISION_LENGTH) -> None:
        # save info
        self.traffic_road_id = TRAFFIC_ROAD_ID
        self.number_of_lane = number_of_lane
        self.road_length = road_length
        self.division = division
        self.division_length = division_length
        # create category list
        self.mapper = dict()
        self._build_mapper()
        

    def push_car_to_cluster_info(self,distance: float,lane_idx: int,road_idx: int,value: float):
        is_first = distance < self.division[1]
        if is_first:
            category_index = 0
        elif distance < self.division[2]: #50
            category_index = 1
        else:
            category_index = 2 # 150
        category_length = self.division[category_index+1]
        cluster_length = self.division_length[category_index+1]
        cluster_index = (abs((distance - category_length))//cluster_length)
        add_to = self.mapper[road_idx][category_index]
        # if is_first:
        #     add_to = self.mapper[road_idx][category_index][lane_idx]
        # print(cluster_index)
        add_to[cluster_index,0] += value
        add_to[cluster_index,1] += 1

    # def _calc_cluster_mean(self,list):



    def calc_cluster_mean(self):
        output = []
        for road_id in self.traffic_road_id:
            for category in self.mapper[road_id]:
                for clusster in category:
                    if clusster[1]:
                        output.append(clusster[0] / clusster[1])
        return output
