import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://root:password@mongo"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.events

events_collection = database.get_collection("events_collection")


def event_helper(event) -> dict:
    return {
        'event': event['event'],
        'start': event['start'],
        'end': event['end'],
        'completed': event['completed'],
    }


async def retrieve_events():
    events = []
    async for event in events_collection.find():
        events.append(event_helper(event))
    return events


async def add_event(event_data: dict) -> dict:
    event = await events_collection.insert_one(event_data)
    new_event = await events_collection.find_one({"_id": event.inserted_id})
    return event_helper(new_event)


async def retrieve_event(id: str) -> dict:
    event = await events_collection.find_one({"_id": ObjectId(id)})
    if event:
        return event_helper(event)


async def update_event(id: str, data: dict):
    if len(data) < 1:
        return False
    event = await events_collection.find_one({"_id": ObjectId(id)})
    if event:
        updated_event = await events_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_event:
            return True
        return False


async def delete_event(id: str):
    event = await events_collection.find_one({"_id": ObjectId(id)})
    if event:
        await events_collection.delete_one({"_id": ObjectId(id)})
        return True
