from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    # Criando pratos
    bolo = Dish("bolo", 15.00)
    meal = Dish("bife", 20.00)
    macarrao = Dish("macarrao carbonara", 25.00)

    # Testando os nomes dos pratos
    assert bolo.name == "bolo"
    assert meal.name == "bife"
    assert macarrao.name == "macarrao carbonara"

    # Testando o método __hash__
    assert bolo.__hash__() != meal.__hash__()
    assert bolo.__hash__() == bolo.__hash__()
    assert bolo.__hash__() != macarrao.__hash__()

    # Testando o método __repr__
    assert bolo.__repr__() == "Dish('bolo', R$15.00)"
    assert meal.__repr__() == "Dish('bife', R$20.00)"
    assert macarrao.__repr__() == "Dish('macarrao carbonara', R$25.00)"

    # Adicionando ingredientes aos pratos
    ingredient_farinha = Ingredient("farinha")
    bolo.add_ingredient_dependency(ingredient_farinha, 1)
    meal.add_ingredient_dependency(ingredient_farinha, 2)
    macarrao.add_ingredient_dependency(ingredient_farinha, 3)

    # Testando o método __eq__
    assert bolo == bolo
    assert bolo != meal

    # Testando criação inválida de Dish (preço negativo)
    with pytest.raises(ValueError):
        Dish("bolo", -10.0)

    # Testando o método get_restrictions
    assert bolo.get_restrictions() == ingredient_farinha.restrictions
    assert meal.get_restrictions() == ingredient_farinha.restrictions
    assert macarrao.get_restrictions() == ingredient_farinha.restrictions

    # Testando o método get_ingredients
    assert bolo.get_ingredients() == {ingredient_farinha}
    assert meal.get_ingredients() == {ingredient_farinha}
    assert macarrao.get_ingredients() == {ingredient_farinha}
