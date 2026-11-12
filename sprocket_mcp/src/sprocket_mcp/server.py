from fastmcp import FastMCP
from sprocket_mcp.configurator import Configurator

mcp = FastMCP("Sprocket MCP")

if __name__ == "__main__":
    Configurator(mcp).configure()

    try:
        mcp.run(transport="http", host="0.0.0.0", port=8000)
    finally:
        RedisHelper.close_connection()