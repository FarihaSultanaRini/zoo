import asyncio
import logging
import os
import uvicorn
from fastapi import FastAPI
from typing import List, Dict, Any
from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

# Environment variable for security (production)
API_KEY = os.getenv("MCP_API_KEY")

mcp = FastMCP("Zoo Animal MCP Server 🦁🐧🐻")

def verify_access():
    """Simple security check for production placeholder."""
    pass

# Dictionary of animals at the zoo
ZOO_ANIMALS = [
    {
        "species": "lion",
        "name": "Leo",
        "age": 7,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "Nala",
        "age": 6,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "Simba",
        "age": 3,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "lion",
        "name": "King",
        "age": 8,
        "enclosure": "The Big Cat Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "penguin",
        "name": "Waddles",
        "age": 2,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Pip",
        "age": 4,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Skipper",
        "age": 5,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Chilly",
        "age": 3,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Pingu",
        "age": 6,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "penguin",
        "name": "Noot",
        "age": 1,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "elephant",
        "name": "Ellie",
        "age": 15,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Peanut",
        "age": 12,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Dumbo",
        "age": 5,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "elephant",
        "name": "Trunkers",
        "age": 10,
        "enclosure": "The Pachyderm Sanctuary",
        "trail": "Savannah Heights"
    },
    {
        "species": "bear",
        "name": "Smokey",
        "age": 10,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Grizzly",
        "age": 8,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Barnaby",
        "age": 6,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "bear",
        "name": "Bruin",
        "age": 12,
        "enclosure": "The Grizzly Gulch",
        "trail": "Polar Path"
    },
    {
        "species": "giraffe",
        "name": "Gerald",
        "age": 4,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Longneck",
        "age": 5,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Patches",
        "age": 3,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "giraffe",
        "name": "Stretch",
        "age": 6,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Speedy",
        "age": 2,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Dash",
        "age": 3,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Gazelle",
        "age": 4,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "antelope",
        "name": "Swift",
        "age": 5,
        "enclosure": "The Tall Grass Plains",
        "trail": "Savannah Heights"
    },
    {
        "species": "polar bear",
        "name": "Snowflake",
        "age": 7,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "polar bear",
        "name": "Blizzard",
        "age": 5,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "polar bear",
        "name": "Iceberg",
        "age": 9,
        "enclosure": "The Arctic Exhibit",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Wally",
        "age": 10,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Tusker",
        "age": 12,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Moby",
        "age": 8,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    },
    {
        "species": "walrus",
        "name": "Flippers",
        "age": 9,
        "enclosure": "The Walrus Cove",
        "trail": "Polar Path"
    }
]

@mcp.tool()
def get_animals_by_species(species: str) -> List[Dict[str, Any]]:
    """
    Retrieves all animals of a specific species from the zoo.
    """
    logger.info(f">>> \ud83d\udee0\ufe0f Tool: 'get_animals_by_species' called for '{species}'")
    return [animal for animal in ZOO_ANIMALS if animal["species"].lower() == species.lower()]

@mcp.tool()
def get_animal_details(name: str) -> Dict[str, Any]:
    """
    Retrieves the details of a specific animal by its name.
    """
    logger.info(f">>> \ud83d\udee0\ufe0f Tool: 'get_animal_details' called for '{name}'")
    for animal in ZOO_ANIMALS:
        if animal["name"].lower() == name.lower():
            return animal
    return {}

if __name__ == "__main__":
    # Auto-detect Cloud Run environment
    is_cloud_run = os.getenv("K_SERVICE") is not None
    port = int(os.getenv("PORT", 8080))
    transport = os.getenv("TRANSPORT", "sse" if is_cloud_run else "stdio")

    if transport == "sse":
        logger.info(f"🚀 Starting SSE server on port {port}")
        
        from fastapi.responses import HTMLResponse
        app = mcp.sse_app()
        
        @app.get("/", response_class=HTMLResponse)
        async def root():
            return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Zoo Animal MCP Server 🦁</title>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
                <style>
                    body { 
                        font-family: 'Inter', sans-serif; 
                        display: flex; 
                        justify-content: center; 
                        align-items: center; 
                        height: 100vh; 
                        margin: 0; 
                        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); 
                        color: white;
                    }
                    .card {
                        background: rgba(255, 255, 255, 0.1);
                        backdrop-filter: blur(10px);
                        padding: 3rem;
                        border-radius: 20px;
                        border: 1px solid rgba(255, 255, 255, 0.2);
                        text-align: center;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    }
                    h1 { margin-bottom: 0.5rem; color: #4ecca3; }
                    p { color: #a2a8d3; }
                    .endpoint {
                        background: #0f3460;
                        padding: 1rem;
                        border-radius: 10px;
                        margin-top: 2rem;
                        font-family: monospace;
                        border: 1px solid #4ecca3;
                        word-break: break-all;
                    }
                    .status {
                        display: inline-block;
                        padding: 0.2rem 0.8rem;
                        background: #4ecca3;
                        color: #1a1a2e;
                        border-radius: 20px;
                        font-weight: bold;
                        font-size: 0.8rem;
                        margin-top: 1rem;
                    }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>Zoo Animal MCP Server 🦁🐧🐻</h1>
                    <p>Your Model Context Protocol server is live and ready to serve.</p>
                    <div class="status">ONLINE</div>
                    <div class="endpoint">
                        Endpoint: https://""" + os.getenv("K_SERVICE", "demo-zoo-server") + """-512499410551.us-east1.run.app/sse
                    </div>
                </div>
            </body>
            </html>
            """
        
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        logger.info("🚀 Starting stdio server")
        mcp.run()
