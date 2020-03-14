import pytest
import yaml

import gendiff.formatters.plain
import gendiff.formatters.yaml
import gendiff.formatters.tree
from gendiff.parsers import parse_yaml
from gendiff.diff_tree import generate_diff


@pytest.fixture()
def complex_yaml_old():
    return open('tests/fixtures/complex_yaml_before.yml')


@pytest.fixture()
def complex_yaml_new():
    return open('tests/fixtures/complex_yaml_after.yml')


@pytest.fixture()
def plain_yaml_old():
    return open('tests/fixtures/plain_yaml_before.yml')


@pytest.fixture()
def plain_yaml_new():
    return open('tests/fixtures/plain_yaml_after.yml')


def test_complex_yaml_plain(complex_yaml_old, complex_yaml_new, complex_result_plain):
    format_diff = gendiff.formatters.plain.format_diff
    old_map, new_map = parse_yaml(complex_yaml_old), parse_yaml(complex_yaml_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = complex_result_plain.read()
    assert test_diff == ethalon_diff


def test_complex_yaml_tree(complex_yaml_old, complex_yaml_new, complex_result_tree):
    format_diff = gendiff.formatters.tree.format_diff
    old_map, new_map = parse_yaml(complex_yaml_old), parse_yaml(complex_yaml_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = complex_result_tree.read()
    assert test_diff == ethalon_diff


def test_complex_yaml_yaml(complex_yaml_old, complex_yaml_new, complex_result_yaml):
    format_diff = gendiff.formatters.yaml.format_diff
    old_map, new_map = parse_yaml(complex_yaml_old), parse_yaml(complex_yaml_new)
    test_diff = yaml.load(format_diff(generate_diff(old_map, new_map)), 
                          Loader=yaml.SafeLoader)
    ethalon_diff = yaml.load(complex_result_yaml, Loader=yaml.SafeLoader)
    assert test_diff == ethalon_diff


def test_plain_yaml(plain_yaml_old, plain_yaml_new, plain_result_plain):
    format_diff = gendiff.formatters.plain.format_diff
    old_map, new_map = parse_yaml(plain_yaml_old), parse_yaml(plain_yaml_new)
    test_diff = format_diff(generate_diff(old_map, new_map))
    ethalon_diff = plain_result_plain.read()
    assert test_diff == ethalon_diff
