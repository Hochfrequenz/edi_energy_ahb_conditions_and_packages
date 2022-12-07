"""
this function is called from a Github Action (consistency_check.yml) that checks the consistency of the data
"""
import json
from pathlib import Path

from ahbicht.mapping_results import (
    ConditionKeyConditionTextMapping,
    ConditionKeyConditionTextMappingSchema,
    PackageKeyConditionExpressionMapping,
    PackageKeyConditionExpressionMappingSchema,
)
from maus.edifact import EdifactFormat, EdifactFormatVersion

_repo_root = Path(__file__).parent.parent


def _condition_load_function(json_list):
    return ConditionKeyConditionTextMappingSchema().load(data=json_list, many=True)


def _condition_key_function(condition_mapping: ConditionKeyConditionTextMapping):
    return condition_mapping.condition_key


def _package_load_function(json_list):
    return PackageKeyConditionExpressionMappingSchema().load(data=json_list, many=True)


def _package_key_function(package_mapping: PackageKeyConditionExpressionMapping):
    return package_mapping.package_key


for format_version in EdifactFormatVersion:
    format_version_path = _repo_root / Path(str(format_version))
    if not format_version_path.exists():
        continue
    for edifact_format in EdifactFormat:
        format_path = format_version_path / Path(str(edifact_format))
        if not format_path.exists():
            continue
        for file_name in ["conditions.json", "packages.json"]:
            file_path = format_path / Path(file_name)
            if not file_path.exists():
                continue
            if file_name == "conditions.json":
                load_function = _condition_load_function  # type:ignore[assignment]
                key_function = _condition_key_function  # type:ignore[assigment]
            elif file_name == "packages.json":
                load_function = _package_load_function  # type:ignore[assignment]
                key_function = _package_key_function  # type:ignore[assignment]
            with open(file_path, "r", encoding="utf-8") as infile:
                json_body = json.load(infile)
            mappings = load_function(json_body)  # must not raise an exception
            keys = [key_function(x) for x in mappings]
            keys_sorted = sorted(keys, key=lambda k: int(k.strip("P")))
            assert keys == keys_sorted  # the entries shall be sorted by key number ASC
            assert len(set(keys)) == len(mappings)  # there shall be no duplicate keys
