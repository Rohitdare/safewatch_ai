from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
import json
from pathlib import Path

# 1️⃣ CREATE APP FIRST
app = FastAPI(
    title="SafeWatch AI",
    description="Real-time Risk Escalation API",
    version="1.0"
)

# 2️⃣ ALERT STORE
ALERTS_FILE = Path("backend/app/alerts/alerts.json")

def load_alerts():
    if not ALERTS_FILE.exists():
        return []
    return json.loads(ALERTS_FILE.read_text())

# 3️⃣ API ROUTES
@app.get("/alerts")
def get_alerts():
    return load_alerts()

@app.get("/alerts/{alert_id}")
def get_alert(alert_id: str):
    for alert in load_alerts():
        if alert["id"] == alert_id:
            return alert
    raise HTTPException(status_code=404, detail="Alert not found")

@app.get("/alerts/{alert_id}/snapshot")
def get_snapshot(alert_id: str):
    for alert in load_alerts():
        if alert["id"] == alert_id:
            return FileResponse(alert["snapshot_path"])
    raise HTTPException(status_code=404, detail="Snapshot not found")

# 4️⃣ DASHBOARD (ROOT)
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return open("backend/app/static/index.html").read()
