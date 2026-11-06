from sprocket_mcp.tools.excel_io import ExcelIo
from fastmcp import FastMCP

class Configurator:
    def __init__(self, fast_mcp: FastMCP) -> None:
        self.fast_mcp: FastMCP = fast_mcp

    def configure(self) -> None:
        excel_io = ExcelIo()
        self.fast_mcp.add_tool(excel_io.get_sheet_names)
        self.fast_mcp.add_tool(excel_io.read_excel)