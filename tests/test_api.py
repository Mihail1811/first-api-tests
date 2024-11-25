from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(new_animal)['id']
        assert new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(
                new_animal, id_find_animal))
        test_case.delete_animal(new_animal)
        check_pet = test_case.find_animal(new_animal)
        assert check_pet['message'] == "Pet not found", "Pet was not daleted!"


    def test_second(self):
        test_case = TestCase()
        id_pet = test_case.create_animal('Дружок')
        id_check_pet = test_case.check_pet(id_pet)['id']
        assert id_pet == id_check_pet, "Ids don't match"
        check_pet = test_case.check_pet(id_pet)
        test_case.delete_pet(id_pet)
        status = ['available', 'pending', 'sold']
        for i in status:
            pets = test_case.find_pets_by_status(i)
            assert check_pet not in pets, \
                f"ID {check_pet} присутствует в списке"
