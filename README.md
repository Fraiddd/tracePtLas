# tracePtLas

tracePtLas is 2 smalls programs, tracePtLas2D (z=0) and tracePtLas3D, in Python 3.11 which traces in Autocad the points of the .las files.

When you receive a large amount of point clouds from a Lidar, being able to batch process .las files is a must.

The clouds containing less than 1000 points are ignored.

Insert a block containing points.

Save each drawing under the name of the .las.

Point resolution is reduced. 1/12 for 3D, 1/32 for 2D
 
## Installation

   - No installation for .exe
   - for .py you have to install pyautocad and laspy

```
pip install pyautocad
pip install laspy
```

## Requirements

  Only for Windows

  Autocad must be installed

## Usage

  - Start Autocad and open the destination drawing.

  - Otherwise Autocad will start with drawing1.dwg.

  - Start tracePtLas2D or tracePtLas3D

  - Choose .las files

  - Wait a few minutes (9 minutes for 6 million points with a Intel Xeon CPU E3-1245 V2 @ 3.40GHz)


## License

  No license
