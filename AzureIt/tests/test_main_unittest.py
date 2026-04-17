import unittest
from unittest.mock import Mock, patch

from main import UserManager, divide, get_weather, is_prime


class DivideTests(unittest.TestCase):
    def test_divide_returns_result_for_valid_inputs(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_raises_for_zero_division(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)


class UserManagerTests(unittest.TestCase):
    def test_add_user_and_get_email(self):
        manager = UserManager()
        self.assertTrue(manager.add_user("ivan", "ivan@example.com"))
        self.assertEqual(manager.get_user_email("ivan"), "ivan@example.com")


class PrimeTests(unittest.TestCase):
    def test_is_prime_for_basic_values(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(9))


class WeatherApiTests(unittest.TestCase):
    @patch("main.requests.get")
    def test_get_weather_returns_json_on_200(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {"temperature": 25}
        mock_get.return_value = response

        result = get_weather("Sofia")

        self.assertEqual(result, {"temperature": 25})


if __name__ == "__main__":
    unittest.main()
