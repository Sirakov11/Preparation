from main import get_weather
from main import divide
from main import UserManager
from main import is_prime
import pytest

#def test_get_weather_temp():
    #assert get_weather(25) == "hot"
    #assert get_weather(15) == "cold"
def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by 0!"):
        divide(10, 0)
        
@pytest.fixture
def manager():
    return UserManager()

def test_add_user(manager):
    assert manager.add_user("Ivan Sirakov", "vanio_carq@abv.bg") == True
    assert manager.get_user("Ivan Sirakov") == "vanio_carq@abv.bg"
  
    #with pytest.raises(ValueError, match="Username already exists"):
        #manager.add_user("Adolf", "hudojnika@abv.bg")
    #with pytest.raises(ValueError, match="Username already exists"):        
        #manager.add_user("Ivan Sirakov", "AnotherEmail@abv.bg")

@pytest.mark.parametrize("num", "expected"[
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (17, True),
    (20, False)
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected
# Pop folk and unittests

def test_get_weather(mocker):
    mock_get = mocker.patch ('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}
    result = get_weather("Sofia")
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://dataservice.accuweather.com/currentconditions/v1/Sofia?apikey=YOUR_API_KEY")



