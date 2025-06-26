import jwt
from datetime import datetime , timedelta , UTC

SECRET_KEY  = "12345tyuiklkjhgfd"

def create_jwt(user_id: int):
    payload = {
        "user_id" : user_id,
        "exp" : datetime.now(UTC) + timedelta(hours=1),
        "iat" : datetime.now(UTC),
    }

    return jwt.encode(payload , SECRET_KEY  , algorithm="HS256")

def decode_jwt_token(token : str):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}



token = create_jwt(123)
print(token)

user_data = decode_jwt_token(token)
print(f"DECODED JWT :- \n {user_data}")

