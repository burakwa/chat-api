Chat API, FastAPI ve Poetry kullanılarak geliştirilen, ölçeklenebilir ve profesyonel bir REST API projesidir. Proje, nesne yönelimli programlama (OOP) prensipleri, katmanlı mimari (Layered Architecture) ve SOLID ilkeleri göz önünde bulundurularak tasarlanmıştır. Amaç, gerçek dünyadaki mesajlaşma sistemlerine benzer bir altyapı geliştirirken temiz kod, sürdürülebilirlik ve genişletilebilirlik konularında deneyim kazanmaktır.

Projede kullanıcı yönetimi, JWT tabanlı kimlik doğrulama, bireysel ve grup sohbetleri, mesajlaşma, rol tabanlı yetkilendirme, WebSocket desteği, veri doğrulama, hata yönetimi, testler ve API dokümantasyonu gibi modern backend geliştirme yaklaşımları uygulanacaktır.

## 📁 Proje Yapısı

```text
chat-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI uygulamasının ayağa kalktığı yer
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── chat.py         # HTTP Endpoint'leri (Controller katmanı)
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py           # Ortam değişkenleri ve ayarlar
│   ├── domain/
│   │   ├── __init__.py
│   │   └── models.py           # İş mantığı modelleri (Saf Python sınıfları)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── chat.py             # Pydantic DTO'ları (API'ye girip çıkan veri şekli)
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base.py             # Repository Arayüzü (Interface)
│   │   └── memory.py           # Şimdilik bellek içi (In-Memory) veritabanı
│   └── services/
│       ├── __init__.py
│       └── chat_service.py     # İş Mantığı (Business Logic) katmanı
└── pyproject.toml
│
│
└── tests
```