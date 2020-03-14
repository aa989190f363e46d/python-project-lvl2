import pytest


@pytest.fixture()
def plain_result_plain():
    return open('tests/fixtures/plain_result_plain.txt')


@pytest.fixture()
def complex_result_yaml():
    return open('tests/fixtures/complex_result_yaml.yml')


@pytest.fixture()
def complex_result_plain():
    return open('tests/fixtures/complex_result_plain.txt')


@pytest.fixture()
def complex_result_tree():
    return open('tests/fixtures/complex_result_tree.txt')


@pytest.fixture()
def complex_result_json():
    return open('tests/fixtures/complex_result_json.json')
