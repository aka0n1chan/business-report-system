from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schema


app = FastAPI()

# DB セッション取得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# 業務報告の作成
@app.post("/reports/", response_model=schema.ReportResponse)
def create_report(report: schema.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db, report)

# 業務報告の一覧取得
@app.get("/reports/", response_model=list[schema.ReportResponse])
def read_reports(db: Session = Depends(get_db)):
    return crud.get_reports(db)

# 特定の業務報告を取得
@app.get("/reports/{report_id}", response_model=schema.ReportResponse)
def read_report(report_id: int, db: Session = Depends(get_db)):
    report = crud.get_report(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report

# 業務報告の削除
@app.delete("/reports/{report_id}", response_model=schema.ReportResponse)
def delete_report(report_id: int, db: Session = Depends(get_db)):
    report = crud.delete_report(db, report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report