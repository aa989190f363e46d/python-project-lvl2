import pytest


@pytest.fixture()
def complex_json_old():
    return open('tests/fixtures/complex_json_before.json')


@pytest.fixture()
def complex_json_new():
    return open('tests/fixtures/complex_json_after.json')


@pytest.fixture()
def complex_result_yaml():
    return open('tests/fixtures/complex_result_yaml.yml')


@pytest.fixture()
def plain_result_txt():
    return open('tests/fixtures/plain_result.txt')


@pytest.fixture()
def complex_result_txt():
    return open('tests/fixtures/complex_result.txt')


@pytest.fixture()
def complex_result_json():
    return open('tests/fixtures/complex_result_json.json')
