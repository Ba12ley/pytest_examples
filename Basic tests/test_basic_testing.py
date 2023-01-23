import pytest

from model import Event


# Simple test to ensure that tests are running and behaving as expected.

def test_pytest():
    assert (1, 2, 3) == (1, 2, 3)


# def test_fail():
#     assert (1, 2, 3) == (3, 2, 1)


def test_event_defaults():
    event1 = Event()
    event2 = Event(None, None, None, False, None)

    assert event1 == event2


def test_event():
    event = Event('Test Event', 'started', 'ended', True, '1')
    assert (event.category, event.start, event.end, event.completed, event.id) == ('Test Event',
                                                                                   'started',
                                                                                   'ended',
                                                                                   True,
                                                                                   '1')


def test_event_asdict():
    event = Event('Test Event', 'started', 'ended', True, '1')
    event_dict = event._asdict()
    expected_dict = {
        'category': 'Test Event',
        'start': 'started',
        'end': 'ended',
        'completed': True,
        'id': '1',
    }
    assert event_dict == expected_dict
