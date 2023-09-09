from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient_cheese = Ingredient("queijo mussarela")
    assert ingredient_cheese.name == "queijo mussarela"
    assert ingredient_cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient_pineapple = Ingredient("tomate")
    assert ingredient_pineapple.name == "tomate"
    assert ingredient_pineapple.restrictions == set()

    assert repr(ingredient_cheese) == "Ingredient('queijo mussarela')"

    same_ingredient1 = Ingredient("queijo mussarela")
    same_ingredient2 = Ingredient("queijo mussarela")
    assert ingredient_cheese == same_ingredient1
    assert same_ingredient1 == same_ingredient2
    assert not (ingredient_cheese != same_ingredient1)
    assert not (same_ingredient1 != same_ingredient2)

    different_ingredient = Ingredient("queijo baconrela")
    another_different_ingredient = Ingredient("bacon queijorela")
    assert ingredient_cheese != different_ingredient
    assert ingredient_cheese != another_different_ingredient
    assert different_ingredient != another_different_ingredient
    assert not (ingredient_cheese == different_ingredient)
    assert not (ingredient_cheese == another_different_ingredient)
    assert not (different_ingredient == another_different_ingredient)

    assert hash(ingredient_cheese) == hash(same_ingredient1)
    assert hash(ingredient_cheese) == hash(same_ingredient2)
    assert hash(ingredient_cheese) != hash(different_ingredient)
    assert hash(ingredient_cheese) != hash(another_different_ingredient)
