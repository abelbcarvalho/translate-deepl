from src.services.service_text import ServiceText


class ControllerText():
    def __init__(self):
        self.service = ServiceText()

    async def translate_text(self, text: any):
        pass
