winget install -e --id Python.Python.3.11
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python build.py