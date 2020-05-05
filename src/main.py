# Credit to github.com/kem0o who has made the code for Neonite available - it was a huge help in this

import asyncio

# Import Sanic (web framework)
from sanic import Sanic
from sanic.response import text, json

# Pages from other files
from api import status

# Setup Sanic
app = Sanic("BeePrivate")


# Test page - this is never queried by Fortnite so we're using it to ensure the web server is running correctly when debugging
async def test_page(req):
    return text("Working!")


# Run web server
if __name__ == "__main__":
    # Add routes
    app.add_route(test_page, "/")

    status_pages = status.get_all_urls()
    for url in status_pages:
        app.add_route(url[1], url[0])

    app.run(host="localhost", port=80)
