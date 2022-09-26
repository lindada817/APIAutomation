import pytest
import yaml


def add(x, y):
    return x + y


def test_get_data():
    # data = yaml.safe_load(open('data/dataForCalculator.yaml'))
    with open("data/dataForCalculator.yaml", 'r', encoding="UTF-8") as file:
        data = yaml.safe_load(file.read())
        data1 = []
        for i in data:
            data1.append(i)
        # print(data1)
        return data1


ids = ["x:{} + y:{} = result:{}".format(x, y, result) for x, y, result in test_get_data()]


class TestAdd:

    @pytest.mark.parametrize('x, y, result', test_get_data(), ids=ids)
    def test_add(self, x, y, result):
        assert add(x, y) == result
