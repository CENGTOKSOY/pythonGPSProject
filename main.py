import folium
from geopy.geocoders import Nominatim
import requests

# Cihazın anlık konumunu almak için geopy kullanılır
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("Zonguldak Merkez, Turkey")
latitude = location.latitude
longitude = location.longitude


# OpenWeatherMap API'sini kullanarak anlık hava durumu bilgilerini almak
api_key = "64d127e5caca947884c912a51ab66b61"
weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
weather_data = requests.get(weather_url).json()

# Hava durumu bilgilerini almak
weather_description = weather_data['weather'][0]['description']
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']

# Bir harita oluşturun ve başlangıç noktasını belirleyin
m = folium.Map(location=[latitude, longitude], zoom_start=13)

# Haritaya bir işaretçi ekleyin ve hava durumu bilgilerini popup olarak gösterin
popup_info = f"Hava Durumu: {weather_description}\nSıcaklık: {temperature}°C\nNem: %{humidity}\nRüzgar Hızı: {wind_speed} m/s"
folium.Marker([latitude, longitude], popup=popup_info).add_to(m)

# Haritayı HTML dosyası olarak kaydedin
m.save('zonguldak_merkez_harita.html')
