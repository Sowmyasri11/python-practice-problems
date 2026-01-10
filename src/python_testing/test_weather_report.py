from weather_report import get_weather

def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(2) == "cold"
    assert get_weather(3) == "hot"
    assert get_weather(4) == "cold"

