# Videoflix Backend

Ein skalierbares Backend für die Videoflix-Anwendung, entwickelt mit Django und Django REST Framework (DRF). Dieses Backend ermöglicht die Konvertierung von Videos in verschiedene Formate mithilfe des RQ-Workers.

## Features
- **API**: RESTful API für CRUD-Operationen auf Videos und Benutzerdaten, basierend auf Django REST Framework.
- **Video-Konvertierung**: Automatische Verarbeitung und Konvertierung hochgeladener Videos in verschiedene Formate mit `rqworker` und Redis.

---

## Installation

### Voraussetzungen
- Python 3.10+
- Linux WSL (Windows Subsystem for Linux), falls der RQ-Worker auf einem Windows-System ausgeführt wird.

### Setup
1. **Repository klonen**:
   ```bash
   git clone <https://github.com/Wilhelm910/videoflix-backend>
   cd videoflix-backend

2. **Virtuell Umgebung erstellen**
python -m venv env
env\Scripts\activate

python3 -m venv env-lin
source env-lin/bin/activate


3. **Abhängigkeiten installieren**
pip install -r requirements.txt
pip install -r requirements-lin.txt


env starten: "env/scripts/activate"
backend starten: python manage.py runserver

env-lin starten: source env-lin/bin/activate
rq worker starten: python manage.py rqworker default


Testing:
pytest users_app/tests/test_models.py
pytest users_app/tests/test_views.py
pytest videos_app/tests/test_models.py
pytest videos_app/tests/test_views.py


