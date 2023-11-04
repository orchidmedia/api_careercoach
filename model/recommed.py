from pydantic import BaseModel


class Recommend(BaseModel):
    recommend: str
