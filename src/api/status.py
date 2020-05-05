from sanic.response import json


# Retrieves all API calls this file is responsible for
def get_all_urls():
    # Format: (URL, Function)
    return [
        ("/lightswitch/api/service/bulk/status", lightswitch_status)
    ]


# Status call
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