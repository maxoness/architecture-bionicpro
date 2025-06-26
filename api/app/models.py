from pydantic import BaseModel


class Report(BaseModel):
    data: str
