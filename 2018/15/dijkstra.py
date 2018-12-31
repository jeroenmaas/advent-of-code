from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 5.093030303030303, 5.32, 5.336633663366337, 5.352941176470588, 5.368932038834951, 0.0],
  [0.0, 5.585858585858586, 5.6, 5.6138613861386135, 0.0, 5.640776699029126, 0.0],
  [0.0, 5.8686868686868685, 0.0, 0.0, 0.0, 0.0, 0.0],
  [0.0, 6.151515151515151, 6.16, 6.1683168316831685, 0.0, 6.184466019417476, 0.0],
  [0.0, 6.434343434343434, 6.4399999999999995, 6.445544554455445, 6.450980392156863, 6.456310679611651, 0.0],
  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]


grid = Grid(matrix=matrix)

start = grid.node(3, 1)
end = grid.node(5, 4)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print(path)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))