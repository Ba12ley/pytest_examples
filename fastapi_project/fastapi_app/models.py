from typing import Optional

from pydantic import BaseModel, Field


class AppSchema(BaseModel):
    event: str = Field(...)
    start: str = Field(...)
    end: str = Field(...)
    completed: bool = False

    class Config:
        schema_extra = {
            'appschema': {
                'event': 'test event',
                'start': 'started',
                'end': 'ended',
                'completed': True,

            }
        }


class UpdateAppSchema(BaseModel):
    event: Optional[str]
    start: Optional[str]
    end: Optional[str]
    completed: Optional[bool]

    class Config:
        schema_extra = {
            'appschema': {
                'event': 'test event',
                'start': 'started',
                'end': 'ended',
                'completed': True,

            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
