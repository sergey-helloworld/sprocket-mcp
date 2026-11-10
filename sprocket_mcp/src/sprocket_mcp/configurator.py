from sprocket_mcp.tools.excel_io import ExcelIo
from sprocket_mcp.tools.telegram_io import TelegramIo
from fastmcp import FastMCP
from fastmcp.tools import Tool

class Configurator:
    def __init__(self, fast_mcp: FastMCP) -> None:
        self.fast_mcp: FastMCP = fast_mcp
        self.excel_io: ExcelIo = ExcelIo()
        self.telegram_io: TelegramIo = TelegramIo()

    def configure(self) -> None:
        self.fast_mcp.add_tool(
            Tool.from_function(
                self.excel_io.get_sheet_names, 
                name="excel.get_sheet_names"
            )
        )
        self.fast_mcp.add_tool(
            Tool.from_function(
                self.excel_io.read_excel, 
                name="excel.read_sheet"
            )
        )
        self.fast_mcp.add_tool(
            Tool.from_function(
                self.telegram_io.send_message, 
                name="telegram.send_message"
            )
        )
        self.fast_mcp.add_tool(
            Tool.from_function(
                self.telegram_io.get_updates, 
                name="telegram.get_updates"
            )
        )