from pydantic import BaseModel


class GradeCreate(BaseModel):
    GradeName: str


class MajorCreate(BaseModel):
    MajorName: str


class ClassCreate(BaseModel):
    ClassName: str


class DormCreate(BaseModel):
    DormName: str
