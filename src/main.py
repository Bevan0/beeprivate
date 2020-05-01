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


# Run web server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)