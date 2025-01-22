from project import anyl, specific, time_conversion, get_airport_details
from amadeus import Client

amadeus = Client(client_id='5BwgzFezNbfF0jtT7Y7nt93zA5sJs3jQ', client_secret='kDqnTGBswVHc4EG4')
def test_anyl():
    assert anyl('MAD') == True
    assert anyl('hello') == False
    assert anyl('mad') == True


def test_specific():
    assert specific("MAD", "AGP", "2025-07-20") == True
    assert specific("MADe", "21", "2025-07-20") == False
    assert specific("MAD", "AGP", "20261-07-20") == False

def test_time_conversion():
    assert time_conversion("PT50M") == "50 minutes"
    assert time_conversion("PT5H") == "5 hours"
    assert time_conversion("PT1H50M") == "1 hour, 50 minutes"
    assert time_conversion("") == "Invalid duration format"
    assert time_conversion("412asfd") == "Invalid duration format"

def test_get_airport_details():
    assert get_airport_details("MAD") == "Madrid Barajas International Airport, Madrid, ES"
    assert get_airport_details("mia") == "Airport not found."
    assert get_airport_details("Hello Again CS50") == "Airport not found."
