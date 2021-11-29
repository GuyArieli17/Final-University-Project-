class Action:
    """
    Each action is a dictionary which contains 4 lists: 
    North, South, East, West.
    Each list has 3 values: [Move left, Move right, Go straight]
    """
    actions = {
            # left east and west
            0: { 
                'WEST' : [1,0,0],
                'SOUTH' : [0,0,0],
                'EAST' : [1,0,0],
                'NORTH' : [0,0,0]     
            },
            # left, right and straight west
            1: { 
                'WEST' : [1,1,1],
                'SOUTH' : [0,0,0],
                'EAST' : [0,0,0],
                'NORTH' : [0,0,0] 
            },
            # right and straight east and west
            2: { 
                'WEST' : [0,1,1],
                'SOUTH' : [0,0,0],
                'EAST' : [0,1,1],
                'NORTH' : [0,0,0]
            },
            # left, right and straight east
            3: { 
                'WEST' : [0,0,0],
                'SOUTH' : [0,0,0],
                'EAST' : [1,1,1],
                'NORTH' : [0,0,0]
            },
            # left south and north
            4: { 
                'WEST' : [0,0,0],
                'SOUTH' : [1,0,0],
                'EAST' : [0,0,0], 
                'NORTH' : [1,0,0]
            },
            # left, right and straight south
            5: { 
                'WEST' : [0,0,0],
                'SOUTH' : [1,1,1],
                'EAST' : [0,0,0], 
                'NORTH' : [0,0,0]
            },
            # right and straight south, north
            6: { 
                'WEST' : [0,0,0],
                'SOUTH' : [0,1,1],
                'EAST' : [0,0,0],
                'NORTH' : [0,1,1]
            }, 
            # leftright and straight south, north
            7: { 
                'WEST' : [0,0,0],
                'SOUTH' : [0,0,0],
                'EAST' : [0,0,0], 
                'NORTH' : [1,1,1]
            },
    }
    
    
