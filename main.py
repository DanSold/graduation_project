from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
import math
from pages.router import router
from fastapi.templating import Jinja2Templates

app = FastAPI(title='VolumeСalculator')
templates = Jinja2Templates(directory="templates")

app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(router)


@app.get('/')
def index():
    return {'res': 'res'}


@app.post('/cube')
def calculation_cube_volume(request: Request, cube_side: float = Form(...)):
    result = cube_side ** 3
    result = round(result, 3)
    return templates.TemplateResponse(name='result_calc.html',
                                      context={'request': request, 'data': result, 'type': 'Cube Volume'})


@app.post('/parallelepiped')
def calculation_parallelepiped_volume(request: Request, height_parallelepiped: float = Form(...),
                                      area_parallelepiped: float = Form(...)):
    result = height_parallelepiped * area_parallelepiped
    result = round(result, 3)
    return templates.TemplateResponse(name='result_calc.html',
                                      context={'request': request, 'data': result, 'type': 'Parallelepiped Volume'})


@app.post('/pyramid')
def calculation_area_pyramid_volume(request: Request, height_pyramid: float = Form(...),
                                    area_pyramid: float = Form(...)):
    result = (area_pyramid * height_pyramid) / 3
    result = round(result, 3)
    return templates.TemplateResponse(name='result_calc.html',
                                      context={'request': request, 'data': result, 'type': 'Pyramid Volume'})


@app.post('/sphere')
def calculation_sphere_volume(request: Request, radius_spheres: float = Form(...)):
    result = 4 / 3 * (math.pi * (radius_spheres ** 3))
    result = round(result, 3)
    return templates.TemplateResponse(name='result_calc.html',
                                      context={'request': request, 'data': result, 'type': 'Sphere Volume'})


@app.post('/cylinder')
def calculation_cylinder_volume(request: Request, radius_cylinder: float = Form(...), height_cylinder: float = Form(...)):
    result = math.pi * radius_cylinder ** 2 * height_cylinder
    result = round(result, 3)
    return templates.TemplateResponse(name='result_calc.html',
                                      context={'request': request, 'data': result, 'type': 'Cylinder Volume'})
