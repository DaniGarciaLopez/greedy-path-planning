#! /usr/bin/env python
import random
import os
import time

DISPLAY_TIME=0.05

while True:
    try:
        selection=int(input("Select a map (1-11): "))
    except: #Avoid int conversion error when a letter is typped
        selection=0
        print("Invalid number")

    while selection<1 or selection>11:
        try:
            selection=int(input("Select a number between 1 and 11: "))
        except:
            selection=0
            print("Invalid number")
    
    iterations=0
    FILE_NAME = "map"+str(selection)+".csv"
    mapPoints={
        1: {
            'start': {
                'x' : 3,
                'y' : 3
            }, 
            'end': {
                'x' : 8,
                'y' : 3
            }, 
        },
        2: {
            'start': {
                'x' : 3,
                'y' : 3
            }, 
            'end': {
                'x' : 11,
                'y' : 8
            }, 
        },
        3: {
            'start': {
                'x' : 5,
                'y' : 11
            }, 
            'end': {
                'x' : 5,
                'y' : 15
            }, 
        },
        4: {
            'start': {
                'x' : 5,
                'y' : 15
            }, 
            'end': {
                'x' : 5,
                'y' : 11
            }, 
        },
        5: {
            'start': {
                'x' : 4,
                'y' : 16
            }, 
            'end': {
                'x' : 4,
                'y' : 10
            }, 
        },
        6: {
            'start': {
                'x' : 3,
                'y' : 3
            }, 
            'end': {
                'x' : 11,
                'y' : 18
            }, 
        },
        7: {
            'start': {
                'x' : 4,
                'y' : 10
            }, 
            'end': {
                'x' : 4,
                'y' : 16
            }, 
        },
        8: {
            'start': {
                'x' : 3,
                'y' : 3
            }, 
            'end': {
                'x' : 11,
                'y' : 18
            }, 
        },
        9: {
            'start': {
                'x' : 4,
                'y' : 10
            }, 
            'end': {
                'x' : 4,
                'y' : 16
            }, 
        },
        10: {
            'start': {
                'x' : 4,
                'y' : 10
            }, 
            'end': {
                'x' : 4,
                'y' : 16
            }, 
        },
        11: {
            'start': {
                'x' : 4,
                'y' : 16
            }, 
            'end': {
                'x' : 4,
                'y' : 10
            }, 
        }
    }    

    class Node:
        def __init__(self, x, y, myId, parentId):
            self.x = x
            self.y = y
            self.myId = myId
            self.parentId = parentId
        def dump(self):
            print("---------- x "+str(self.x)+\
                            " | y "+str(self.y)+\
                            " | id "+str(self.myId)+\
                            " | parentId "+str(self.parentId))
        def checkSurroundings(self): #Return the direction of a free tile or 0 if not found
            if charMap[self.x-1][self.y] == '0':
                return 1
            elif charMap[self.x][self.y+1] == '0':
                return 2
                
            elif charMap[self.x+1][self.y] == '0':
                return 3
                
            elif charMap[self.x][self.y-1] == '0':
                return 4
            else:
                return 0


    nodes = []
    

    init = Node(mapPoints[selection]["start"]["x"], mapPoints[selection]["start"]["y"], 0, -2)

    nodes.append(init)

    charMap = []

    def dumpMap(map):
        os.system('cls' if os.name == 'nt' else 'clear') #Clear screen: "cls" in windows and "clear" in linux

        for line in map:
            for tile in line:
                if tile=='0': #Free
                    print("  ", end= '')
                elif tile=='1': #Obstacle
                    print("██", end= '')
                elif tile=='2': #Visited
                    print("░░", end= '')
                elif tile=='3': #Start
                    print("[]", end= '') 
                elif tile=='4': #Goal
                    print("<>", end= '')
                elif tile=='5': #Path
                    print("▒▒", end= '')
            print("") 


    with open(FILE_NAME) as f:
        line = f.readline()
        while line:
            charLine = line.strip().split(',')
            charMap.append(charLine)
            line = f.readline()

    charMap[mapPoints[selection]["start"]["x"]][mapPoints[selection]["start"]["y"]] = '3'
    charMap[mapPoints[selection]["end"]["x"]][mapPoints[selection]["end"]["y"]] = '4'

    done = False
    goalParentId = -1

    try:
        algorithm=int(input("Select search algorithm: \n1)Breadth \n2)Greedy\n"))
    except: #Avoid int conversion error when a letter is typped
        algorithmn=0
        print("Invalid number")

    while algorithm<1 or algorithm>2:
        try:
            algorithm=int(input("Select a number between 1 and 2: "))
        except:
            algorithm=0
            print("Invalid number")

    startTime=time.time()

    if algorithm==1: #BFS
        while not done:
            for node in nodes:
                dumpMap(charMap)
                iterations+=1 #Increase iteration to compute total computing time

                # up
                tmpX = node.x - 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    print("up: GOALLLL!!!")
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    print("up: mark visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # down
                tmpX = node.x + 1
                tmpY = node.y
                if( charMap[tmpX][tmpY] == '4' ):
                    print("down: GOALLLL!!!")
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    print("down: mark visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # right
                tmpX = node.x
                tmpY = node.y + 1
                if( charMap[tmpX][tmpY] == '4' ):
                    print("right: GOALLLL!!!")
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    print("right: mark visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                # left
                tmpX = node.x
                tmpY = node.y - 1
                if( charMap[tmpX][tmpY] == '4' ):
                    print("left: GOALLLL!!!")
                    goalParentId = node.myId
                    done = True
                    break
                elif ( charMap[tmpX][tmpY] == '0' ):
                    print("left: mark visited")
                    newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)

                time.sleep(DISPLAY_TIME) #Sleep to visualize map

    elif algorithm==2: #Greedy
        #direction=0 : not defined
        #direction=1 : up
        #direction=2 : right
        #direction=3 : down
        #direction=4 : left
        direction=0 
        directionVerbose = ["not defined","up", "right", "down", "left"]
        index=-1


        while not done:
            dumpMap(charMap)
            iterations+=1 #Increase iteration to compute total computing time

            print("Number of nodes: "+str(len(nodes)))
            if not direction: #If direction is not defined, pick it random
                direction=random.randint(1,4)

            print("Direction: "+str(directionVerbose[direction]))
            
            #nodes[-1] picks the last node in the list

            if direction==1: #up
                tmpX = nodes[index].x - 1
                tmpY = nodes[index].y
                
            elif direction==2: #right
                tmpX = nodes[index].x
                tmpY = nodes[index].y + 1

            elif direction==3: #down
                tmpX = nodes[index].x + 1
                tmpY = nodes[index].y

            elif direction==4: #left
                tmpX = nodes[index].x
                tmpY = nodes[index].y - 1

            if( charMap[tmpX][tmpY] == '4' ):
                    goalParentId = nodes[index].myId
                    done = True
                    break
            elif ( charMap[tmpX][tmpY] == '0' ):
                    print(str(directionVerbose[direction])+": mark visited")
                    newNode = Node(tmpX, tmpY, len(nodes), nodes[index].myId)
                    charMap[tmpX][tmpY] = '2'
                    nodes.append(newNode)
                    index=-1 #Reset to last node
            
            elif ( charMap[tmpX][tmpY] == '2' ): #Node already visited. Checking other nodes with free tiles in surroundings
                free=False
                while not free: #Find node with a free tile in its surroundings
                    direction=nodes[index].checkSurroundings() #
                    if not direction: #If free direction does not exist, then check parent 
                        index=nodes[index].parentId
                    else:
                        free=True

            elif ( charMap[tmpX][tmpY] == '1' or charMap[tmpX][tmpY] == '3'):
                    direction=0  #Reset direction if obstacle or start detected

            
            time.sleep(DISPLAY_TIME) #Sleep 10ms to visualize map
                

    resultMap=charMap
    ok = False
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                #node.dump()
                if node.myId > 0: #Avoid changing color from starting tile
                    resultMap[node.x][node.y]='5' #Changing tiles color to visualize path to goal
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True

    dumpMap(resultMap)
    print("============ GOAL REACHED ============")
    currentTime=time.time()
    computingTime=(currentTime-startTime)-iterations*DISPLAY_TIME
    print("Iterations: " +str(iterations))
    print("Computing time: "+str(round(computingTime,4))+"s\n")