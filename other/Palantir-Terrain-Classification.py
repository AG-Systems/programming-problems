#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findTerrainTypes' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY elevations
#  2. 2D_CHARACTER_ARRAY features
#

def findTerrainTypes(elevations, features):
    import math
    # Write your code here
    if elevations == [] or features == []:
        return []

    def detect_river(elevations, features):
        # rivers move 
        # rivers are connected to bigger pools of water

        # rivers have elevation descending downwards
        pass
    def detect_highland(elevations, features):
        # highlands have a very high elevation without any "drops"
        row = 0
        col = 0
        intial_height = elevations[row][col]
        while row < len(elevations) - 1:
            while col < len(elevations[row]) - 1:
                if features[row][col] != "W" and features[row][col] != "T":
                    if abs(intial_height - elevations[row][col + 1]) <= 3:
                        if features[row][col + 1] != "W" and features[row][col + 1] != "T":
                            return True
                    if abs(intial_height - elevations[row + 1][col + 1]) <= 3:
                        if features[row + 1][col + 1] != "W" and features[row + 1][col + 1] != "T":
                            return True
                    if abs(intial_height - elevations[row + 1][col]) <= 3:
                        if features[row + 1][col] != "W" and features[row + 1][col] != "T":
                            return True                
                    col += 1
            row += 1
        return False
    def detect_waterfall(elevations, features):
        # waterfalls are just like rivers, they have a sudden steep drop
        pass
    def detect_cliff(elevations, features):
        # cliffs are just like highlands however they have a sudden steep drop
        # highlands have a very high elevation without any "drops"
        row = 0
        col = 0
        intial_height = elevations[row][col]
        while row < len(elevations) - 1:
            while col < len(elevations[row]) - 1:
                #if features[row][col] != "W" and features[row][col] != "T":
                if abs(intial_height - elevations[row][col + 1]) <= 10:
                    #if features[row][col + 1] != "W" and features[row][col + 1] != "T":
                    return True
                if abs(intial_height - elevations[row + 1][col + 1]) <= 10:
                    #if features[row + 1][col + 1] != "W" and features[row + 1][col + 1] != "T":
                    return True
                if abs(intial_height - elevations[row + 1][col]) <= 10:
                    #if features[row + 1][col] != "W" and features[row + 1][col + 1] != "T":
                    return True                
                col += 1
            row += 1
        return False

    def detect_lake(elevations, features):
        # lake has a very similar elevation throughout 
        pass
    def detect_beach(elevations, features):
        # beach has sand and water
        pass
    def detect_forest(elevations, features):
        # forest just has a bunch trees
        pass
    
    terrain_types = []
    if detect_river(elevations, features):
        terrain_types.append("river")
    if detect_highland(elevations, features):
        terrain_types.append("highland")
    if detect_cliff(elevations, features):
        terrain_types.append("cliff")
    if detect_lake(elevations, features):
        terrain_types.append("lake")
    if detect_beach(elevations, features):
        terrain_types.append("beach")
    if detect_forest(elevations, features):
        terrain_types.append("forest")
    return terrain_types

if __name__ == '__main__':
