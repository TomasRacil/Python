# Conway's Game of Life

made with shapely library to create unique random behaviour determined by geometry

made by sk3rda
inspired by Game of Life from Electronut Labs: <https://github.com/electronut/pp/blob/master/conway/conway.py>
generatePolygon function from: <https://newbedev.com/algorithm-to-generate-random-2d-polygon>

numpy, matplotlib and shapely needed - there can be problem with instalation of shapely with pip - it wont install all its dependencies (e.g. geos.dll) and the game wont run

to proper install and manage all your libraries install Anaconda to create custom enviroments: <https://www.anaconda.com/products/individual>
conda guide: <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>

- To create an environment: conda create --name myenv
- To activate an env: conda activate myenv
- To install needed libraries: conda install -c conda-forge shapely matplotlib numpy

to run the game from conda, activate ur enviroment, set it to game dir and run with command: python main.py (with args to control the game, args in -h)

Known issues:

- angle of ellipse is set bc generating_point_in_polygon was crashing sometimes bc there were more than 1 min and max coords.
- sometimes there is graphical issue (mostly with vertices in hundreds) that we get out of displayed grid bc img is set to be grid size and verts arent -> img = ax.imshow(grid)
- when grid size is increased above ~150 with geometry, its getting really slow, bad optimalization in update function

Possible future extensions:

- polygons determined by user coords (get input with nargs, paste it into shapely.Polygon, done)
- more polygons determined by shape - square,.. - polygons with predetermined location on grid (only playing with numbers in shapely.Polygon)
- make more shapes viable at the same time (make more lists so that shapes dont rewrite themselves and change Update to use intersection or union for them)
- make it faster = scrap the Update algorithm and compute only the area within polygon
- combine it with game of life by Chaloupka,Kovar
