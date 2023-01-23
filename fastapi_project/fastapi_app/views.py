from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from .db import (add_event, retrieve_event, update_event, delete_event, retrieve_events)
from .models import (AppSchema, UpdateAppSchema, error_response_model, response_model)

router = APIRouter()


@router.post("/", response_description="Event added into the database", status_code=201)
async def add_event_data(event: AppSchema = Body(...)):
    event = jsonable_encoder(event)
    new_event = await add_event(event)
    return response_model(new_event, "Event added successfully.")


@router.get("/", response_description="All events")
async def get_all_events():
    events = await retrieve_events()
    if events:
        return response_model(events, 'Events retieved')
    return error_response_model(events, 'Empty List')


@router.get("/{id}", response_description="Single event")
async def get_event(id):
    event = await retrieve_event(id)
    if event:
        return response_model(event, 'Event retrieved')
    return error_response_model('Error', 404, 'Event does not exist')


@router.put("/{id}")
async def update_event(id: str, req: UpdateAppSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_event = await update_event(id, req)
    if updated_event:
        return response_model(f"Student with ID: {id} name update is successful", "Student name updated successfully", )
    return error_response_model("Error", 404, "There was an error updating the event.", )


@router.delete("/{id}")
async def delete_event(id):
    event_to_delete = await delete_event
    if event_to_delete:
        return response_model(f'Event with id {id} successfully deleted', 'Event deleted')
    return error_response_model('Error', 404, f'Event {id} does not exist')
