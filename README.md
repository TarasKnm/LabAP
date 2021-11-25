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

curl -X GET http://localhost:5000/user/username2 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgyNzU4MiwianRpIjoiZjNhMTM0ZTMtZTJhMi00YzQyLWE5NGQtZThjNjI5MDExZGZjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMiIsIm5iZiI6MTYzNzgyNzU4MiwiZXhwIjoxNjM4NDMyMzgyfQ.RUt1U2cT6cM7xLXMttbKrvic8uL5EhvIIOlAG33al2Y"

Update user by username

curl -X PUT http://localhost:5000/user/1 -H "Content-Type:application/json" --data-binary "{"first_name": "Boy"}" -H "Authorization: Bearer 

Delete user by username

curl -X DELETE http://localhost:5000/user/username1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgyNTE3MywianRpIjoiMTIwZjhjNDEtMDcwZS00NWY0LWIwOWUtZDAwOTk5NGUwZjFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMSIsIm5iZiI6MTYzNzgyNTE3MywiZXhwIjoxNjM4NDI5OTczfQ.EnpiSOO1g7yMlY9xnLeyVaBrv-_zEg0t-fxh9NLpwWo"
Add good
curl -X POST http://localhost:5000/store/goods/1 -H "Content-Type:application/json" --data-binary "{\"id\":0,\"name\":\"string\",\"isAvailable\":true,\"photoUrls\":[\"string\"],\"status\":\"available\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzQyNywianRpIjoiMmUwNGUwYWItZDY4MS00ZGRmLTk4NzItNWEzMWVkNDZiOWQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODUzNDI3LCJleHAiOjE2Mzg0NTgyMjd9.fmgU4c-gZQvELVKDE4oAuKPb2SDuOWJRKziJbL-MrOM"
Add store
admin
curl -X POST http://localhost:5000/store/store -H "Content-Type:application/json" --data-binary "{\"name\":\"name1\",\"category\":\"category1\",\"goods\":[{\"id\":0,\"name\":\"name1\",\"isAvailable\":true,\"photoUrls\":[\"string\"],\"status\":\"available\"}]}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1NzU1MCwianRpIjoiZDMzNmVjMGItYWVmMy00MDRiLTgyYTUtZmU3ZjU1MDk2OWQ4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODU3NTUwLCJleHAiOjE2Mzg0NjIzNTB9.9gjXWsiVW0J5IfNJPcS6TgWq0wtk_r7r77dyFGOuEzQ"
user
curl -X POST http://localhost:5000/store/store -H "Content-Type:application/json" --data-binary "{\"name\":\"name1\",\"category\":\"category1\",\"goods\":[{\"id\":0,\"name\":\"name1\",\"isAvailable\":true,\"photoUrls\":[\"string\"],\"status\":\"available\"}]}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg0NDA1MywianRpIjoiNzhjZjBlMzQtY2FlZC00NWJmLWE1MjctMjg1ZjZlNDkxMDc1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lMiIsIm5iZiI6MTYzNzg0NDA1MywiZXhwIjoxNjM4NDQ4ODUzfQ.ko5Izs43Btri5nafuH29jFmygl8FXtUmlH66yYzjA2M"

Get Order by id
Admin
curl -X GET http://localhost:5000/store/order/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzQyNywianRpIjoiMmUwNGUwYWItZDY4MS00ZGRmLTk4NzItNWEzMWVkNDZiOWQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODUzNDI3LCJleHAiOjE2Mzg0NTgyMjd9.fmgU4c-gZQvELVKDE4oAuKPb2SDuOWJRKziJbL-MrOM"
Correct user
curl -X GET http://localhost:5000/store/order/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgzNDQ1NSwianRpIjoiNmVkNjc1ZWYtNTdjYi00NDk5LTkwODktOGJkNjU2OTM1MWFjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODM0NDU1LCJleHAiOjE2Mzg0MzkyNTV9.ivswSODpOt9pSjeldPgkALWhAssO1YTPf8I00vFl-Gk"
Uncorrect user
curl -X GET http://localhost:5000/store/order/1 -H "Authorization: Bearer "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzAyMCwianRpIjoiN2IzOGIwNTktOWU3Mi00NTg4LWJkNmItMjM4OTEwOWU2MTk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5hbWUiLCJuYmYiOjE2Mzc4NTMwMjAsImV4cCI6MTYzODQ1NzgyMH0.MbPsiw2FLLCYmO4JA_SzommiiSH0Vadw5L-CBpz3gHc"

Delete order by id
Admin
curl -X DELETE http://localhost:5000/store/order/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzQyNywianRpIjoiMmUwNGUwYWItZDY4MS00ZGRmLTk4NzItNWEzMWVkNDZiOWQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODUzNDI3LCJleHAiOjE2Mzg0NTgyMjd9.fmgU4c-gZQvELVKDE4oAuKPb2SDuOWJRKziJbL-MrOM"
Correct user
curl -X DELETE http://localhost:5000/store/order/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzgzNDQ1NSwianRpIjoiNmVkNjc1ZWYtNTdjYi00NDk5LTkwODktOGJkNjU2OTM1MWFjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODM0NDU1LCJleHAiOjE2Mzg0MzkyNTV9.ivswSODpOt9pSjeldPgkALWhAssO1YTPf8I00vFl-Gk"
Uncorrect user
curl -X DELETE http://localhost:5000/store/order/1 -H "Authorization: Bearer "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzAyMCwianRpIjoiN2IzOGIwNTktOWU3Mi00NTg4LWJkNmItMjM4OTEwOWU2MTk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im5hbWUiLCJuYmYiOjE2Mzc4NTMwMjAsImV4cCI6MTYzODQ1NzgyMH0.MbPsiw2FLLCYmO4JA_SzommiiSH0Vadw5L-CBpz3gHc"

Delete good by id
User
curl -X DELETE http://localhost:5000/goods/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1NzYwNiwianRpIjoiYzRlNmM2NWYtNjZjZS00MzE2LWJhMDUtODM3Mzk5YTBhYzM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lIiwibmJmIjoxNjM3ODU3NjA2LCJleHAiOjE2Mzg0NjI0MDZ9.2a77Zo33sNXUc0SOwvB6UyQ6uQqplDKVdMjU1WYkldw"
Admin
curl -X DELETE http://localhost:5000/goods/1 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzQyNywianRpIjoiMmUwNGUwYWItZDY4MS00ZGRmLTk4NzItNWEzMWVkNDZiOWQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODUzNDI3LCJleHAiOjE2Mzg0NTgyMjd9.fmgU4c-gZQvELVKDE4oAuKPb2SDuOWJRKziJbL-MrOM"

Update good by name
Admin
curl -X PUT http://localhost:5000/goods/string -H "Content-Type:application/json" --data-binary "{\"id\":2,\"name\":\"kk\",\"isAvailable\":true,\"photoUrls\":[\"string\"],\"status\":\"available\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1MzQyNywianRpIjoiMmUwNGUwYWItZDY4MS00ZGRmLTk4NzItNWEzMWVkNDZiOWQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNjM3ODUzNDI3LCJleHAiOjE2Mzg0NTgyMjd9.fmgU4c-gZQvELVKDE4oAuKPb2SDuOWJRKziJbL-MrOM"
User
curl -X PUT http://localhost:5000/goods/jura -H "Content-Type:application/json" --data-binary "{\"id\":2,\"name\":\"las\",\"isAvailable\":true,\"photoUrls\":[\"string\"],\"status\":\"available\"}" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNzg1NzYwNiwianRpIjoiYzRlNmM2NWYtNjZjZS00MzE2LWJhMDUtODM3Mzk5YTBhYzM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJuYW1lIiwibmJmIjoxNjM3ODU3NjA2LCJleHAiOjE2Mzg0NjI0MDZ9.2a77Zo33sNXUc0SOwvB6UyQ6uQqplDKVdMjU1WYkldw"
