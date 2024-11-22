from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(id_new_animal)['id']
        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(
                id_new_animal, id_find_animal))
        id_delete_animal = test_case.delete_animal(id_new_animal)

    def test_second(self):
        test_case = TestCase()
        id_pet = test_case.create_animal('Дружок')
        id_check_pet = test_case.check_pet(id_pet)['id']
        check_pet = test_case.check_pet(id_pet)
        id_delete_pet = test_case.delete_pet(id_pet)
        check_after_delete = test_case.check_pet(id_pet)
        status = ['available', 'pending', 'sold']
        for i in status:
            pets = test_case.find_by_status(i)
            assert check_pet not in pets, \
                f'ID {check_pet} присутствует в списке'
