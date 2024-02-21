#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkSphere
from vtkmodules.vtkFiltersCore import vtkContourFilter
from vtkmodules.vtkImagingHybrid import vtkSampleFunction
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
from vtkmodules.vtkFiltersCore import vtkMarchingCubes


def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor("BkgColor", [51, 77, 102, 255])

    sphere = vtkSphere()
    sample_resolution = get_program_parameters()

    # Sample the function
    sample = vtkSampleFunction()
    sample.SetSampleDimensions(sample_resolution, sample_resolution, sample_resolution)
    sample.SetImplicitFunction(sphere)
    value = 1.0
    xmin = -value
    xmax = value
    ymin = -value
    ymax = value
    zmin = -value
    zmax = value
    sample.SetModelBounds(xmin, xmax, ymin, ymax, zmin, zmax)

    # Create the 0 isosurface
    iso_surface = vtkMarchingCubes()
    iso_surface.SetInputConnection(sample.GetOutputPort())

    # Map the contours to graphical primitives
    iso_surface_mapper = vtkPolyDataMapper()
    iso_surface_mapper.SetInputConnection(iso_surface.GetOutputPort())
    iso_surface_mapper.ScalarVisibilityOff()

   # Create an actor for the contours
    isoActor = vtkActor()
    isoActor.SetMapper(iso_surface_mapper)
    isoActor.GetProperty().SetColor(colors.GetColor3d('Bisque'))

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetWindowName('Implicit Sphere Marching Cubes')

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    renderer.AddActor(isoActor)
    renderer.SetBackground(colors.GetColor3d("BkgColor"))

    renderWindow.Render()
    interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Maps the isosurface described by the implicit sphere equation using the marching cubes algorithm.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-r', '--resolution', type=int, default=101,
                        help='The sample resolution of the sphere. Default is 101, min is 5')
    args = parser.parse_args()
    return args.resolution


if __name__ == '__main__':
    main()
