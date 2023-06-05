from fastapi import FastAPI
import math
from pages.router import router

app = FastAPI(title='VolumeСalculator')
app.include_router(router)


@app.get('/')
def index():
    return {'res': 'res'}


@app.get('/parallelepiped/{side_length}')
def calculation_parallelepiped_volume(height_parallelepiped: float, area_parallelepiped: float):
    if height_parallelepiped and area_parallelepiped > 0:
        result = height_parallelepiped * area_parallelepiped
        result = round(result, 3)
        return {
            'ParallelepipedVolume': result,
            'status': 'ok'
        }
    else:
        return {
            'status': 'Parameters cannot be less than or equal to zero'
        }


@app.get('/cube/{side_length}')
def calculation_cube_volume(side_length: float):
    if side_length > 0:
        result = side_length ** 3
        result = round(result, 3)
        return {
            'CubeVolume': result,
            'status': 'ok'
        }
    else:
        return {
            'status': 'Parameters cannot be less than or equal to zero'
        }


@app.get('/pyramid/{height_pyramid}')
def calculation_pyramid_volume(height_pyramid: float, area_pyramid: float = None, radius: float = None):
    if height_pyramid > 0:
        if area_pyramid > 0:
            result = (area_pyramid * height_pyramid) / 3
            result = round(result, 3)
            return {
                'PyramidVolume': result,
                'area_pyramid': area_pyramid,
                'height_pyramid': height_pyramid,
                'status': 'ok'
            }
        if radius > 0:
            result = (math.pi * radius ** 2 * height_pyramid) / 3
            result = round(result, 3)
            return {
                'PyramidVolume': result,
                'radius': radius,
                'height_pyramid': height_pyramid,
                'status': 'ok'
            }
        else:
            return {
                'status': 'Please enter some data (radius or area of pyramid)'
            }
    else:
        return {
            'status': 'The height of the pyramid cannot be less than or equal to 0'
        }


@app.get('/sphere/{radius_sphere}')
def calculation_sphere_volume(radius_spheres: float):
    if radius_spheres > 0:
        result = 4 / 3 * (math.pi * (radius_spheres ** 3))
        result = round(result, 3)
        return {
            'SphereVolume': result,
            'RadiusSphere': radius_spheres,
            'status': 'ok'
        }
    else:
        return {
            'status': 'Parameters cannot be less than or equal to zero'
        }


@app.get('/cylinder/{radius_cylinder}')
def calculation_cylinder_volume(radius_cylinder: float, height_cylinder: float):
    if radius_cylinder and height_cylinder > 0:
        result = math.pi * radius_cylinder ** 2 * height_cylinder
        result = round(result, 3)
        return {
            'CylinderVolume': result,
            'RadiusCylinder': radius_cylinder,
            'HeightCylinder': height_cylinder,
            'status': 'ok'
        }
    else:
        return {
            'status': 'Parameters cannot be less than or equal to zero'
        }
