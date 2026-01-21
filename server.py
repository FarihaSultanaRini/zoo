import asyncio
import logging
import os
from typing import List, Dict, Any

from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

# Environment variable for security (production)
API_KEY = os.getenv("MCP_API_KEY")

mcp = FastMCP("Zoo Animal MCP Server 🦁🐧🐻")

def verify_access():
    """Simple security check for production. In a real scenario, use middleware or auth headers."""
    # This is a placeholder for more complex auth.
    # For now, we logging that a tool was called.
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
    Can also be used to collect the base data for aggregate queries
    of animals of a specific species - like counting the number of penguins
    or finding the oldest lion.

    Args:
        species: The species of the animal (e.g., 'lion', 'penguin').

    Returns:
        A list of dictionaries, where each dictionary represents an animal
        and contains details like name, age, enclosure, and trail.
    """
    logger.info(f">>> 🛠️ Tool: 'get_animals_by_species' called for '{species}'")
    return [animal for animal in ZOO_ANIMALS if animal["species"].lower() == species.lower()]

@mcp.tool()
def get_animal_details(name: str) -> Dict[str, Any]:
    """
    Retrieves the details of a specific animal by its name.

    Args:
        name: The name of the animal.

    Returns:
        A dictionary with the animal's details (species, name, age, enclosure, trail)
        or an empty dictionary if the animal is not found.
    """
    logger.info(f">>> 🛠️ Tool: 'get_animal_details' called for '{name}'")
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
        logger.info(f"🚀 MCP server starting on port {port} with SSE transport")
        
        # We use the sse_app to add a custom root route for easy verification
        from fastapi import FastAPI
        import uvicorn
        
        # Get the standard FastMCP SSE app
        app = mcp.sse_app()
        
        # Add a simple landing page at the root
        @app.get("/")
        async def root():
            return {
                "status": "Zoo Animal MCP Server is running! 🦁",
                "transport": "SSE",
                "mcp_endpoint": "/sse",
                "instructions": "Connect your MCP client to the /sse endpoint."
            }
        
        # Run it
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        logger.info("🚀 MCP server starting with stdio transport")
        mcp.run()