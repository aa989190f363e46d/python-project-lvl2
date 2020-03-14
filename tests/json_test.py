import pytest
import json

import gendiff.formatters.plain
import gendiff.formatters.json
import gendiff.formatters.tree
from gendiff.parsers import parse_json
from gendiff.diff_tree import generate_diff


@pytest.fixture()
def plain_json_old():
    return open('tests/fixtures/plain_json_before.json')


@pytest.fixture()
def plain_json_new():
    return open('tests/fixtures/plain_json_after.json')


@pytest.fixture()
def complex_json_old():
    return open('tests/fixtures/complex_json_before.json')


@pytest.fixture()
def complex_json_new():
    return open('tests/fixtures/complex_json_after.json')


def test_complex_json_plain(complex_json_old, complex_json_new, complex_result_plain):
    format_diff = gendiff.formatters.plain.format_diff
    old_map, new_map = parse_json(complex_json_old), parse_json(complex_json_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = complex_result_plain.read()
    assert test_diff == ethalon_diff


def test_complex_json_tree(complex_json_old, complex_json_new, complex_result_tree):
    format_diff = gendiff.formatters.tree.format_diff
    old_map, new_map = parse_json(complex_json_old), parse_json(complex_json_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = complex_result_tree.read()
    assert test_diff == ethalon_diff


def test_complex_json_json(complex_json_old, complex_json_new, complex_result_json):
    format_diff =  gendiff.formatters.json.format_diff
    old_map, new_map = parse_json(complex_json_old), parse_json(complex_json_new)
    test_diff = json.loads(format_diff(generate_diff(old_map, new_map)))
    ethalon_diff = json.load(complex_result_json)
    assert test_diff == ethalon_diff


def test_plain_json(plain_json_old, plain_json_new, plain_result_plain):
    format_diff = gendiff.formatters.plain.format_diff
    old_map, new_map = parse_json(plain_json_old), parse_json(plain_json_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = plain_result_plain.read()
    assert test_diff == ethalon_diff
