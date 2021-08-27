from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Sex(str, Enum):
    boy = "SexTrue"
    girl = "SexFalse"
    sexless = "Sex"

class NameDB(BaseModel):
    name: str
    sex: Sex

    def dict(self):
        return {
            'name': self.name,
            'sex': self.sex.name
        }

class FirstNameDB(BaseModel):
    first_name: str

class DetailDB(BaseModel):
    thien_cach: str
    nhan_cach: str
    dia_cach: str
    ngoai_cach: str
    tong_cach: str
    danh_gia: Optional[str]
    liked: Optional[str]
