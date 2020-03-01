import pytest

@pytest.fixture()
def complex_json_old():
    return open('tests/fixtures/complex_json_before.json')


@pytest.fixture()
def complex_json_new():
    return open('tests/fixtures/complex_json_after.json')


@pytest.fixture()
def complex_yaml_old():
    return open('tests/fixtures/complex_yaml_before.yml')


@pytest.fixture()
def complex_yaml_new():
    return open('tests/fixtures/complex_yaml_after.yml')


@pytest.fixture()
def plain_json_old():
    return open('tests/fixtures/plain_json_before.json')


@pytest.fixture()
def plain_json_new():
    return open('tests/fixtures/plain_json_after.json')


@pytest.fixture()
def plain_yaml_old():
    return open('tests/fixtures/plain_yaml_before.yml')


@pytest.fixture()
def plain_yaml_new():
    return open('tests/fixtures/plain_yaml_after.yml')


@pytest.fixture()
def plain_result_txt():
    return open('tests/fixtures/plain_result.txt')


@pytest.fixture()
def complex_result_txt():
    return open('tests/fixtures/complex_result.txt')


@pytest.fixture()
def complex_diff():
    from gendiff.enums import ChangesEnum as changes
    return  [[changes.NESTED, 'group1',
                [[changes.INTACT, 'foo', 'bar'],
                 [changes.ALTERED, 'baz', ('bas', 'bars')]]],
            [changes.NESTED, 'common',
                [[changes.INTACT, 'setting1', 'Value 1'],
                 [changes.INTACT, 'setting3', True],
                 [changes.ADDED, 'setting5', {'key5': 'value5'}],
                 [changes.ADDED, 'setting4', 'blah blah'],
                 [changes.REMOVED, 'setting6', {'key': 'value'}],
                 [changes.REMOVED, 'setting2', '200']]],
            [changes.ADDED, 'group3', {'fee': '100500'}],
            [changes.REMOVED, 'group2', {'abc': '12345'}]]