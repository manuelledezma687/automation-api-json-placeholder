from jsonschema.validators import Draft202012Validator
from pydantic import BaseModel


class SchemasModel(BaseModel):
    get_post: Draft202012Validator

    class Config:
        arbitrary_types_allowed = True
