from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas_class_info import GradeCreate, MajorCreate, ClassCreate, DormCreate
from db.database import get_db
from crud.crud_class_info import create_grade, create_major, create_class, create_dorm

router_class_info = APIRouter()


@router_class_info.post("/create_grade", response_model=GradeCreate)
def create_grade_api(grade: GradeCreate, db: Session = Depends(get_db)):
    return create_grade(db, grade_name=grade.GradeName)


@router_class_info.post("/create_major", response_model=MajorCreate)
def create_major_api(major: MajorCreate, db: Session = Depends(get_db)):
    return create_major(db, major_name=major.MajorName, grade_id=major.GradeID)


@router_class_info.post("/create_class", response_model=ClassCreate)
def create_class_api(class_: ClassCreate, db: Session = Depends(get_db)):
    return create_class(db, class_name=class_.ClassName, major_id=class_.MajorID)


@router_class_info.post("/create_dorm", response_model=DormCreate)
def create_dorm_api(dorm: DormCreate, db: Session = Depends(get_db)):
    return create_dorm(db, dorm_name=dorm.DormName, class_id=dorm.ClassID)
