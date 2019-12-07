import pytest
from band import Band, Musician, Guitarist, Bassist, Drummer


def do_you_wanna_rock():
    assert "Are you ready for some kick-ass solos?" == Band.moment_of_fame()


def test_Dave_is_instance_of_correct_class(Sam):
    assert isinstance(Sam, Drummer)


def test_Dave_is_instance_of_parent_class(Sam):
    assert isinstance(Sam, Musician)


def test_jimmy_name(Sam):
    assert Sam.name == 'Sam'


def test_Dave_instrument(Sam):
    assert Sam.instrument == 'Drummer'

@pytest.fixture()
def Sam():
    return Drummer('Sam', 'Drummer')


@pytest.fixture(autouse=True)
def clean():
    Band.members = []