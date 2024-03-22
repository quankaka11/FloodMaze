from pyMaze import maze,agent


m = maze(19,19)
m.CreateMaze(loopPercent=50)
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path},delay=100)

m.run()