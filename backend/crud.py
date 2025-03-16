from sqlalchemy.orm import Session
from models import Report
from schema import ReportCreate

def create_report(db: Session, report: ReportCreate):
    db_report = Report(title=report.title, content=report.content)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_reports(db: Session):
    return db.query(Report).all()

def get_report(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).first()

def delete_report(db: Session, report_id: int):
    db_report = db.query(Report).filter(Report.id == report_id).first()
    if db_report:
        db.delete(db_report)
        db.commit()
    return db_report
