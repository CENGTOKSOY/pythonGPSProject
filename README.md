# GPS ve Hava Durumu Haritası Uygulaması

Bu proje, kullanıcıların harita üzerindeki herhangi bir noktaya tıklayarak o yerin anlık hava durumu bilgisini almasını sağlayan bir web uygulamasıdır.

## Özellikler

- Harita üzerinde istediğiniz yere tıklayarak o yerin koordinatlarını alabilirsiniz.
- Tıklanan noktanın hava durumu bilgileri, OpenWeatherMap API'si kullanılarak alınır ve gösterilir.

## Kullanılan Teknolojiler

- Python
- Folium: Harita oluşturmak ve işaretçiler eklemek için kullanılır.
- Geopy: Adresleri koordinatlara çevirmek için kullanılır.
- Requests: API istekleri yapmak için kullanılır.

## Kurulum

Projeyi çalıştırmadan önce gerekli kütüphaneleri yüklemeniz gerekmektedir:


pip install folium geopy requests


## Kullanım

Uygulamayı çalıştırmak için `main.py` dosyasını çalıştırın. Tarayıcınızda açılan `interactive_map.html` dosyasında, harita üzerinde istediğiniz yere tıklayarak hava durumu bilgisini alabilirsiniz.
