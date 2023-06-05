from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import main

router = APIRouter(
    prefix='/web'
)

templates = Jinja2Templates(directory='templates')


@router.get('/')
def get_volume_info(request: Request):
    return templates.TemplateResponse(
        'VolumeСalculator.html',
        context={'request': request,
                 'result': main.calculation_cube_volume}
    )
