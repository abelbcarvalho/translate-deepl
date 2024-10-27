from src.exceptions.exceptions import SuperException
from src.models.text import TextModel
from src.services.service_text import ServiceText
from src.utilities.checkers.check_body import check_body
from src.utilities.response.response import response


class ControllerText:
    def __init__(self):
        self.service = ServiceText()

    async def translate_text(self, body: any):
        try:
            text: TextModel = await check_body(body, TextModel)

            data = await self.service.translate_text(text)

            return await response(dict(text=data))
        except SuperException as se:
            return await response(
                body=dict(error=se.message),
                code=se.code
            )
