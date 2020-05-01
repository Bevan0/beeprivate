# Credit to github.com/kem0o who has made the code for Neonite available - it was a huge help in this

import asyncio

# Import Sanic (web framework)
from sanic import Sanic
from sanic.response import text, json

# Setup Sanic
app = Sanic("BeePrivate")


# Test page - this is never queried by Fortnite so we're using it to ensure the web server is running correctly when debugging
@app.route("/")
async def test_page(req):
    return text("Testing...")


# Lightswitch Status API - we're returning static data for now
@app.route("/lightswitch/api/service/bulk/status")
async def lightswitch_status(req):
    return json({
        "serviceInstanceId": "fortnite",
        "status": "UP",
        "message": "WIP epic gamers",
        "maintenanceUri": None,
        "overrideCatalogIds": ["a7f138b2e51945ffbfdacc1af0541053"],
        "allowedActions": ["PLAY", "DOWNLOAD"],
        "banned": False,
        "launcherInfoDTO": {
            "appName": "Fortnite",
            "catalogItemId": "4fe75bbc5a674f4f9b356b5c90567da5",
            "namespace": "fn"
        }
    })


# Run web server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
