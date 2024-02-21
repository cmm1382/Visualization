# Rendering a Robot Arm with Light Source in OpenGL

The goal of the project is to model a simple animatronic with realistic materials and lighting in C++ OpenGL.

##Source code:\
-illumination.cpp\
Attached dependencies:\
-robotMaterials.vs (main vertex shader)\
-robotMaterials.fs (main fragment shader)\
-robotLight.vs (vertex shader for rendering lamp)\
-robotLight.fs (fragment shader for rendering lamp)\
-camera.h\
-shader.h\
##Output:\
The robot arm is rendered in a black background with a point light source represented by a
white cube (the lamp mentioned above). Arm can extend and retract upper and lower arm, rotate
around Y axis, open and close fingers. Material for arm is chrome, material for fingers is red plastic.
Material specs from http://devernay.free.fr/cours/opengl/materials.html. Header and shader files
adapted from ones provided at https://learnopengl.com. 
