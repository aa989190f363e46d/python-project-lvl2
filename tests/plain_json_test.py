import pytest
from gendiff.comparators.json import generate_diff


def test_plain_json():
    with open('tests/fixtures/plain_json_before.json') as old, \
        open('tests/fixtures/plain_json_after.json') as new, \
        open('tests/fixtures/plain_json_result.txt') as result:
        assert generate_diff(old, new) == result.read()[:-1]