import pytest

# test_parametrize.py
# @pytest.mark.parametrize runs the test_addition function with each pair of input and expected values.
# The test checks if adding 1 to input gives the expected result.
@pytest.mark.parametrize("input, expected", [(1, 2), (3, 4), (5, 6)])
def test_addition(input, expected):
    result = input + 1
    assert result == expected
    
# test_fixtures.py
# @pytest.fixture defines a setup function (sample_data) that returns a value.
# test_with_fixture uses this fixture to get the setup data.
@pytest.fixture
def api_response_test():
    # Simulated response obejct taken from Weather API
    response_object = {
        "coord": { "lon": 115.86, "lat": -31.95 },
        "weather": [
            { "id": 800, "main": "Clear", "description": "clear sky", "icon": "01d" }
        ],
        "base": "stations",
        "main": {
            "temp": 20.69,
            "feels_like": 20.17,
            "temp_min": 20.69,
            "temp_max": 20.69,
            "pressure": 1020,
            "humidity": 52,
            "sea_level": 1020,
            "grnd_level": 1016
        },
        "visibility": 10000,
        "wind": { "speed": 4.58, "deg": 208, "gust": 3.41 },
        "clouds": { "all": 9 },
        "dt": 1756798906,
        "sys": { "country": "AU", "sunrise": 1756765958, "sunset": 1756807229 },
        "timezone": 28800,
        "id": 2063523,
        "name": "Perth",
        "cod": 200
    }

    return response_object


def test_with_fixture(sample_data):
    assert api_response_test["name"] == "Perth"
    assert api_response_test["cod"] == 200


# test_assertions.py
def test_simple_assertions():
    a = 10
    b = 10
    assert a == b 