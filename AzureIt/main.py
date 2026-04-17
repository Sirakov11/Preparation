import requests
def get_weather_by_temperature(temp):
    if temp > 20:
        return "hot"
    else:
        return "cold"
    
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = email
        return True

    def get_user_email(self, username):
        return self.users[username]


def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int (n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_weather(city):
    response = requests.get(f"https://dataservice.accuweather.com/currentconditions/v1/{city}?apikey=YOUR_API_KEY")
    if response.status_code == 200:
        return  response.json()
    else:
        raise ValueError("Failed to fetch weather data")
    
