from unittest.mock import Mock, patch
import unittest
import requests

# Function to be tested
def get_weather(city, get_function=requests.get):
    response = get_function(f"https://api.weather.com/{city}")
    return response.json()


class TestWeather(unittest.TestCase):
    def test_get_weather_success(self):
        # Create a mock get function
        mock_get = Mock()
        
        # Configure the mock to return a dummy JSON response
        mock_get.return_value.json.return_value = {
            "city": "Sydney",
            "temperature": 25
        }

        # Call the function with the mock
        result = get_weather("Sydney", get=mock_get)

        # Assertions
        self.assertEqual(result, {"city": "Sydney", "temperature": 25})
        mock_get.assert_called_once_with("https://api.weather.com/Sydney")


# Run the test when the file is executed
if __name__ == "__main__":
    unittest.main()
