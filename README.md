# LabAP
python 3.7.0 virtualenv+requirements.txt
Запуск сервера
waitress-serve --port=8000 app:app
http://localhost:8000/api/v1/hello-world-6

Alembic 
- alembic stamp head
- alembic revision -m "add models" --autogenerate
- alembic upgrade head
- alembic downgrade -1

Curl
Get user by username

curl -X GET http://localhost:5000/user/username2 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgyNTE3MywianRpIjoiMTIwZjhjNDEtMDcwZS00NWY0LWIwOWUtZDAwOTk5NGUwZjFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMSIsIm5iZiI6MTYzNzgyNTE3MywiZXhwIjoxNjM4NDI5OTczfQ.EnpiSOO1g7yMlY9xnLeyVaBrv-_zEg0t-fxh9NLpwWo"

Update user by username

curl -X PUT http://localhost:5000/user/1 -H "Content-Type:application/json" --data-binary "{"first_name": "Boy"}" -H "Authorization: Bearer 

Delete user by username

curl -X DELETE http://localhost:5000/user/username1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgyNTE3MywianRpIjoiMTIwZjhjNDEtMDcwZS00NWY0LWIwOWUtZDAwOTk5NGUwZjFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMSIsIm5iZiI6MTYzNzgyNTE3MywiZXhwIjoxNjM4NDI5OTczfQ.EnpiSOO1g7yMlY9xnLeyVaBrv-_zEg0t-fxh9NLpwWo"