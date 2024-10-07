#  How are you start the project:
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

IP 0.0.0.0 is very important in order to find routes in mobile device

The project split to several components:
1. routes - main.py
2. base_models - these are the schemas that the server can receive
3. user_service - contains the all logic in order to return the right response