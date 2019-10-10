def showAllView(data, mazeSizes):

   for idx, d in enumerate(mazeSizes):
      print("Maze size: %d" %d)
      print("Average time: %f" %data[idx][0])
      print("Avegage visited: %d" %data[idx][1])

   
   

def startView():
   print('Maze')
   print('Start/End y/n')

def endView():
   print('Goodbye!')
