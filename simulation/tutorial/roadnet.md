Roadnet File Format
===================
The simulation(cityflow) use this json file to build the road map on wich the vehicle drive. 
The file compose of 2 main 'objects' wich determined it behaviour: `intersections` , `roads`.

### intersections 
object|description
------|-------------------------
`id` |uniq string.
`point`| the intersection centered coordinate `x` , `y`
`width`| the height or length of the intersection
`roads`| id's of roads connected to the intersection(max.6)
`roadLinks`| list of possible route from one road to another trhow the intersection Object <br> `type`: "turn_left" \ "turn_right" \ "go_straight", <br>`startRoad`: from road-id ,<br>`endRoad`: to road-id <br> `laneLinks`: array of lane movment inside the intersection
`trafficLight` | include `lightphases` wich determined the phase (period,and wich lanes).
`virtual` | true if it's a peripheral intersection (if it only connects to one road).
                
### roads
object|description
------|-------------------------
`id` | uniq string
`startIntersection` | id of the intersection we start from
`endIntersection` | id of the intersection we end in
`points`| array of start of the road and end point in `x`,`y` axis
`lanes` | array of lane {`width`: 4, `maxSpeed`: 16.67}

### example:
![Screenshot](https://i.ibb.co/XSb6ymR/Screenshot-from-2021-09-28-12-36-29.png)
```js
{
    "intersections": [
        {
            "id": "intersection_0_0",
            "point": {
                "x": 0,
                "y": 0
            },
            "width": 10,
            "roads": [
                "road_0_0_0",
                "road_0_0_1",
                "road_1_0_0",
                "road_1_0_1"
            ],
            "roadLinks": [
                {
                    "type": "go_straight",
                    "startRoad": "road_0_0_0",
                    "endRoad": "road_1_0_1",
                    "laneLinks": [
                        {
                            "startLaneIndex": 0,
                            "endLaneIndex": 0,
                            "points": [
                                {
                                    "x": 2,
                                    "y": -5
                                },
                                {
                                    "x": 2,
                                    "y": 5
                                }
                            ]
                        }
                    ]
                }
            ],
            "trafficLight": {
                "lightphases": [
                    {
                        "time": 30,
                        "availableRoadLinks": [
                            0
                        ]
                    },
                    {
                        "time": 5,
                        "availableRoadLinks": [
                            
                        ]
                    }
                ]
            },
            "virtual": false
        },
        {
            "id": "intersection_1_0",
            "point": {
                "x": 0,
                "y": -300
            },
            "width": 0,
            "roads": [
                "road_0_0_0",
                "road_0_0_1"
            ],
            "roadLinks": [],
            "virtual": true
        },
        {
            "id": "intersection_1_1",
            "point": {
                "x": 0,
                "y": 300
            },
            "width": 0,
            "roads": [
                "road_1_0_0",
                "road_1_0_1"
            ],
            "roadLinks": [],
            "virtual": true
        }
    ],
    "roads": [
        {
            "id": "road_0_0_0",
            "points": [
                {
                    "x": 0,
                    "y": -300
                },
                {
                    "x": 0,
                    "y": 0
                }
            ],
            "lanes": [
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                }
            ],
            "startIntersection": "intersection_1_0",
            "endIntersection": "intersection_0_0"
        },
        {
            "id": "road_0_0_1",
            "points": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 0,
                    "y": -300
                }
            ],
            "lanes": [
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                }
            ],
            "startIntersection": "intersection_0_0",
            "endIntersection": "intersection_1_0"
        },
        {
            "id": "road_1_0_0",
            "points": [
                {
                    "x": 0,
                    "y": 300
                },
                {
                    "x": 0,
                    "y": 0
                }
            ],
            "lanes": [
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                }
            ],
            "startIntersection": "intersection_1_1",
            "endIntersection": "intersection_0_0"
        },
        {
            "id": "road_1_0_1",
            "points": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 0,
                    "y": 300
                }
            ],
            "lanes": [
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                },
                {
                    "width": 4,
                    "maxSpeed": 16.67
                }
            ],
            "startIntersection": "intersection_0_0",
            "endIntersection": "intersection_1_1"
        }
    ]
}

```
