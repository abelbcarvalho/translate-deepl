import json
from typing import Dict

from flask import Response


async def response(body: Dict[str, any], code: int = 200) -> Response:
    content_type = "Application/json"

    return Response(
        content_type=content_type,
        status=code,
        response=json.dumps(body)
    )
