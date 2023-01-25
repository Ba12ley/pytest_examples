import os.path
from pathlib import Path

import pytest
from program import Certification
from tempfile import TemporaryDirectory


@pytest.fixture()
def certification_data():
    new_cert = Certification('A+', 'Comptia', 'Entry', False)
    new_cert.write_to_db()
    return new_cert


def test_certification_class(certification_data):
    assert certification_data.title == 'A+'
    assert certification_data.awarding_body == 'Comptia'
    assert certification_data.level == 'Entry'
    assert certification_data.completed == False
    assert certification_data.to_dict() == {'title': 'A+',
                                            'awarding_body': 'Comptia',
                                            'level': 'Entry',
                                            'completed': False, }


def test_certification_score(certification_data):
    assert certification_data.score() == 1


def test_certification_file_write(certification_data):
    assert os.path.exists(f'{certification_data.title}.txt')
