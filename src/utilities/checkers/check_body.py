from pydantic import ValidationError, BaseModel

from typing import Type

from src.exceptions.exceptions import SuperException


async def check_body(body: any, type_obj: Type[BaseModel]):
    try:
        data = type_obj.model_validate(body)

        return data
    except ValidationError as ve:
        print(ve)
        raise SuperException(
            message="body has invalid data",
            code=400
        )
