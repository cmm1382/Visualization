# Rendering an IsoSurface with the Marching Cubes Algorithm

Suppose f(x,y,z) = x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> \
We want to render the Iso-Surface where f(x,y,z) = 0.5 within the unit cube

Using VTK in python, the implicit sphere function can be used to calculate the sphere equation at given sample points. The given equation is the sphere equation, so we just have to sample this function at 1013 uniform points within [-1,1]<sup>3</sup>. The iso-surface of any constant should then be a sphere with a radius proportionate to the constant and the sampling function’s parameters. The attached file marchingcubes.py models the sphere equation centered at (x,y,z) = (0,0,0) and renders the iso-surface of 0.5. The amount of samples for each axis is taken as a positional input, but defaults to 101.

## Source code:
- marchingcubes.py

## Required Packages
- vtk
  - available through pip

## Output:

### Running ‘python marchingcubes.py’
![image](https://github.com/cmm1382/Visualization/assets/148571043/c777d7aa-2954-40bf-9925-3323ba6a610a)

### Press W to view wireframe model. This shows how dense the mesh is.
![image](https://github.com/cmm1382/Visualization/assets/148571043/e0ca3389-2d2f-43c3-9230-2e937204f506)

### Running ‘python marchingcubes.py -r 5’ shows that less sample points leads to a less accurate rendering
![image](https://github.com/cmm1382/Visualization/assets/148571043/63493355-2fc7-46e5-a9d2-c2f9e6c45b4f)

### Running ‘python marchingcubes.py -r 500’ shows that there is not much visual difference as sample points are increased. When increased to ~1000, the program does not run on my machine.
![image](https://github.com/cmm1382/Visualization/assets/148571043/3a7c8727-1b4e-4534-82bf-fe82cfbce10f)

### Press W to view wireframe model. Although the sphere is not noticeably better, the mesh is much more dense.
![image](https://github.com/cmm1382/Visualization/assets/148571043/3d94a9dc-a3e5-4ab0-a36b-a88a1086cd01)
