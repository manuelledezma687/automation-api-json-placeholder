import glob
import json
from pathlib import Path
from typing import List

from jsonschema.validators import Draft202012Validator


class SchemasFiles:

    @staticmethod
    def __get_schemas() -> List[str]:
        path = Path(__file__).parents[1]
        return glob.glob(f'{path}/schemas/*.json')

    @staticmethod
    def __parsed_name(path_file) -> str:
        return path_file.split("schemas/")[1].replace(".json", "")

    @staticmethod
    def __read_schema(file):
        with open(file, "r",encoding="utf8") as file:
            return json.loads(file.read())

    @staticmethod
    def get_dict():
        return {SchemasFiles.__parsed_name(schema): Draft202012Validator(SchemasFiles.__read_schema(schema)) for
                schema in SchemasFiles.__get_schemas()}
