import json

from fastapi_project.fastapi_app import views


def test_add_event_data(test_app, monkeypatch):
    sent_test_data = {'event': 'pytest event',
                      'start': 'started',
                      'end': 'ended',
                      'completed': True,
                      }
    returned_test_data = {'data': [{
        'event': 'pytest event',
        'start': 'started',
        'end': 'ended',
        'completed': True,

    }], 'code': 201, 'message': 'Event added successfully.',
    }

    response = test_app.post('/', content=json.dumps(sent_test_data), )

    assert response.json() == returned_test_data
    assert response.status_code == 201

# def test_get_root(test_app):
#     response = test_app.get('/')
#     assert response.json() == {'Message': 'This is the root endpoint'}
