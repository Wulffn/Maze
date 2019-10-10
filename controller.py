import model
import view
import time

def solveMaze(size):
    grid = model.convert(model.DFS(model.make_empty_maze(size,size)))
    start = time.time()
    model.search(1, 1, grid)
    end = time.time()

    #print(grid)

    count = 0
    flattened_list = [y for x in grid for y in x]

    for n in flattened_list:
        if n == 3 or n == 2:
            count += 1
    t = end - start

    lis = [t, count]

    return lis

def startMaze():
    overallData = []
    mazeSizes = [5,10,15,20,25,30]
    
    for mazeSize in mazeSizes : 
        time = []
        count = 0
        averageTime = 0
        averageSteps = 0        
        while(count < 10):
            time.append(solveMaze(mazeSize))
            count += 1
        
        for a in time:
            averageTime += a[0]

        for a in time:
            averageSteps += a[1]

        averageTime = averageTime / len(time)
        averageSteps = averageSteps / len(time)

        overallData.append([averageTime, averageSteps])
        


    #return overallData?
    return view.showAllView(overallData, mazeSizes)




def start():
    view.startView()
    inp = input()
    if inp == 'y':
        startMaze()
    else:
        view.endView()

if __name__ == "__main__":
   #running controller function
   start()