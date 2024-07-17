from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str
    email: str
    account_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError("account_id must be greater than 0")
        return value


user = User(name="John Doe", email="john@doe.com", account_id="123")
print(user)
print(user.name)

# Return JSON string
user_json_obj = user.json()
print(user_json_obj)

# Return a python dictionary
user_dict_obj = user.dict()
print(user_dict_obj)


# Convert a json string into a pydantic model
json_str = '{"name": "Jane Doe", "email": "janedoe.com", "account_id": 2}'
user_from_json = User.parse_raw(json_str)
print(user_from_json)
