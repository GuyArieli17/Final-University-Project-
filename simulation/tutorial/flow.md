Flow File Format
===================
The simulation(cityflow) use this json file to build vehicle and thier movment. 
The file compose of array of 'objects' wich determined each vehicle behaviour.

properties|description
------|-------------------------
`vehicle` | exclamation ahead 
`route` | exclamation ahead 
`interval` | how many step to finish the route
`startTime` | on wich step it beggin
`endTime` | witch step hw stops



### vehicle
properties|description
------|-------------------------
`length` | vehicle length
`width` | width of the vehicle
`maxPosAcc` | max fowrad acceleration
`maxNegAcc`| max backward acceleration
`usualPosAcc` | regular foward acceleration
`usualNegAcc` | regular backward acceleration
`minGap` | minimum gap from the next vehicle
`maxSpeed` | vehicle speed limit 
`headwayTime` | idk

### route:
properties|description
------|-------------------------
`route` | array of road route to go throw



```js
[
    {
        "vehicle": {
            "length": 5.0,
            "width": 2.0,
            "maxPosAcc": 2.0,
            "maxNegAcc": 4.5,
            "usualPosAcc": 2.0,
            "usualNegAcc": 4.5,
            "minGap": 2.5,
            "maxSpeed": 16.67,
            "headwayTime": 1.5
        },
        "route": [
            "road_0_0_0",
            "road_1_0_1"
        ],
        "interval": 10.0,
        "startTime": 0,
        "endTime": -1
    }
]
```
