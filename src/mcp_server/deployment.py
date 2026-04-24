from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

#Add an additional tool
@mcp.tool()
def add(a:int , b :int) -> int:
    return a + b