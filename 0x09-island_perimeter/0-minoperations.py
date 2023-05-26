#!/usr/bin/python3
'''Island Perimeter Interview'''


def island_perimeter(grid):
    '''Calculates the perimeter of the Island described and returns it.'''
    countholder = 0
    maximumgrid = len(grid) - 1
    lastmax = len(grid[0]) - 1

    for lastindex, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # the left side and right side 
                if land_idx == 0:
                    
                    countholder += 1

                    if lst[land_idx + 1] == 0:
                        countholder += 1
                elif land_idx == lastmax:
                    # left side
                    if lst[land_idx - 1] == 0:
                        countholder += 1

                    # right side
                    countholder += 1
                else:
                    # left side
                    if lst[land_idx - 1] == 0:
                        countholder += 1

                    # right side
                    if lst[land_idx + 1] == 0:
                        countholder += 1

                # top and down
                if lastindex == 0:
                    # top side
                    countholder += 1

                    # bottom side
                    if grid[lastindex + 1][land_idx] == 0:
                        countholder += 1
                elif lastindex == maximumgrid:
                    # top side
                    if grid[lastindex - 1][land_idx] == 0:
                        countholder += 1

                    # bottom side
                    countholder += 1
                else:
                    # top side
                    if grid[lastindex - 1][land_idx] == 0:
                        countholder += 1

                    # bottom side
                    if grid[lastindex + 1][land_idx] == 0:
                        countholder += 1

    return countholder
