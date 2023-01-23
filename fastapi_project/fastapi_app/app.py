from fastapi import FastAPI

from . import views
from .models import AppSchema
from .views import router as ViewRouter

app = FastAPI()

app.include_router(ViewRouter, tags=['route'])


@app.get('/', tags=['Root'])
async def root_get():
    return {'Message': 'This is the root endpoint'}


# @app.post('/', tags=['Add to Root'])
# async def root_post(event: AppSchema):
#     data = await views.add_event_data(event)
#     response_object = {
#         'id': data,
#         'event': event.event,
#         'start': event.start,
#         'end': event.end,
#         'completed': event.completed,
#
#     }
#     return response_object
