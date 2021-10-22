import json
class JsonHandler:
    @staticmethod
    def read(path):
        with  open(f'{path}.json') as file:
            return json.load(file)
    
    @staticmethod                                                                                                                                                                                                                                                   
    def create(path,json_dict): 
        with open(f'{path}.json','w') as json_file:
            json.dump(json_dict,json_file)
           
    @staticmethod
    def append(path,json_dict):
        with open(f'{path}.json','r')as file1:
            file_as_json = json.load(file1)
            file_as_json.update(json_dict)
            with  open(f'{path}.json','w')as file2:
                json.dump([file_as_json],file2)
                                   
    @staticmethod
    def append_in(path,placement,value):
        with open(f'{path}.json','r')as file1:
            file_as_json = json.load(file1)
            regular_keys = placement[:-1]
            prime_key = placement[-1]
            prev_dict = file_as_json
            for key in regular_keys:
                prev_dict = prev_dict[key]
            prev_dict[prime_key].update(value)
            with  open(f'{path}.json','w')as file2:
                json.dump([file_as_json],file2)
                
                
    @staticmethod
    def append_to_intersection(path,intersection_id,options):
        with open(f'{path}.json','r')as file1:
            file_as_json = json.load(file1)[0]
            #print(file_as_json)
            lst = file_as_json['intersections']
            index = 0
            while index < len(lst) and lst[index]["id"] != intersection_id:
                index+=1
            if index == len(lst):
                return
            for opt in options:
               lst[index]["trafficLight"]["lightphases"].append({"time": opt[0],"availableRoadLinks":opt[1]})
            with  open(f'{path}.json','w')as file2:
                json.dump([file_as_json],file2)