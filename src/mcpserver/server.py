from fastmcp import FastMCP

# Create your FastMCP server
mcp = FastMCP("MyServer")

@mcp.tool
def analyze(data: str) -> dict:
    """Analyze the given data and return a summary."""
    return {"result": f"Analyzed: {data}"}

@mcp.tool
def get_bio() -> dict:
    """Return the biography of the agent."""
    return {}


@mcp.resource("behavior://personality")
def define_personality() -> str:
    """Define the personality of the server."""
    return "Be friendly and helpful, your name is Kevin, please respond in a casual tone."