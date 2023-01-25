from collections import namedtuple

Event = namedtuple('Event', ['category', 'start', 'end', 'completed', 'id'])
Event.__new__.__defaults__ = (None, None, None, False, None)


