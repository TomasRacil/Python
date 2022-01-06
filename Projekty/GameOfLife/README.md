# Conway's Game of Life

made with shapely library to create unique behaviour determined by geometry

run from cmd with args to control the game

made by sk3rda
inspired by Game of Life from Electronut Labs: https://github.com/electronut/pp/blob/master/conway/conway.py

generatePolygon function from: https://newbedev.com/algorithm-to-generate-random-2d-polygon

Known issues:

- angle of ellipse is set bc generating_point_in_polygon was crashing sometimes bc there were more than 1 min and max coords.
- sometimes there is graphical issue (mostly with vertices in hundreds) that we get out of displayed grid.
- more geometries can be applied at once but it will just rewrite itself the way it is coded rn.
- when grid size is increased above ~150 with geometry, its getting really slow.

## TODO

- rozdělit do modulů kvůli přehlednosti
- proměnná ani není využívána pouze naplněna
- při pokusu o spuštění následující chyba: *"FileNotFoundError: Could not find module 'geos.dll' (or one of its dependencies). Try using the full path with constructor syntax."*
