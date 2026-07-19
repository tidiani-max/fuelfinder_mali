# ⛽ FuelFinder Mali

> A community-powered platform that helps people across Mali find available fuel stations, compare prices, and share real-time fuel availability during fuel shortages.

FuelFinder Mali was created in response to recurring fuel shortages in Mali. The platform enables citizens to locate nearby fuel stations, verify fuel availability through community reports, and access up-to-date pricing information.

By combining geolocation, crowdsourced updates, and intelligent verification, FuelFinder Mali improves access to reliable fuel information when it matters most.

---

## ✨ Features

- ⛽ Find nearby fuel stations
- 📍 Interactive map with geolocation
- 💰 Compare fuel prices
- 👥 Community-powered fuel availability reports
- ✅ Verification system for reported information
- 🔍 Smart search and filtering
- 📱 Responsive mobile-friendly interface
- ⚡ Fast and lightweight user experience

---

## 🌍 Why FuelFinder Mali?

Fuel shortages can make it difficult for drivers to know where fuel is available.

FuelFinder Mali provides a centralized platform where users can:

- Discover nearby fuel stations
- Check fuel availability before traveling
- View recent community reports
- Compare prices between stations
- Help others by sharing updates

The platform is designed to improve transparency and reduce unnecessary travel during fuel crises.

---

## 🏗️ System Architecture

```text
Users
   │
   ▼
Interactive Web Platform
   │
   ├───────────────┐
   │               │
   ▼               ▼
Station Database   Community Reports
   │               │
   └───────┬───────┘
           ▼
Verification & Search Engine
           │
           ▼
Interactive Map
```

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- PostgreSQL

### Frontend

- HTML5
- CSS3
- JavaScript

### Services

- Google Maps API
- Geolocation
- REST API

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/tidiani-max/FuelFinder-Mali.git

cd FuelFinder-Mali
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

```bash
cp .env.example .env
```

Update your environment variables.

### Run the server

```bash
python manage.py migrate

python manage.py runserver
```

---

## 📸 Screenshots

Coming soon

- Home Page
- Interactive Map
- Station Details
- Community Reports

---

## 🚀 Impact

- 🇲🇱 Built to address fuel shortages in Mali
- 🌍 Community-driven information sharing
- 📍 Helps users save time and fuel by locating available stations

---

## 🗺️ Roadmap

- Mobile application
- AI-powered fuel demand prediction
- Route optimization
- Push notifications
- Fuel price trends
- Offline map support

---

## 📄 License

MIT License
