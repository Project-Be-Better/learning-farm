@echo off

@echo Activating virtual environment...
@REM activate virtual environment
call .\backend\venv\Scripts\activate.bat

@REM start backend FastAPI
cd .\backend

@echo Starting backend FastAPI server...
uvicorn server:app --reload