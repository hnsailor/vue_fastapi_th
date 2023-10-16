from pydantic import BaseModel
from typing import List


class GradeCreate(BaseModel):
    GradeName: str


class MajorCreate(BaseModel):
    MajorName: str


class ClassCreate(BaseModel):
    ClassName: str


class DormCreate(BaseModel):
    DormName: str


class ClassInfoIn(BaseModel):
    info: List[str]


class SanitationCreate(BaseModel):
    WeekNumber: int
    Weekday: int
    Status: str
    DormID: int
