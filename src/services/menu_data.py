import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str):
        # Caminho para o arquivo CSV com os dados do menu
        self.source_path = source_path

        # Conjunto para armazenar todos os pratos
        self.dishes = set()

        # Dicionário tempo para mapear nomes de pratos para instâncias de Dish
        dish_name_to_instance = {}

        # Abrir o arquivo CSV para leitura
        with open(self.source_path, 'r', encoding='utf-8') as file:
            # Criar um leitor CSV baseado em dicionário
            csv_reader = csv.DictReader(file, delimiter=',')

            # Iterar pelas linhas do arquivo CSV
            for row in csv_reader:
                # Extrair informações da linha
                dish_name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                # Verificar se já criamos uma instância para este prato
                if dish_name in dish_name_to_instance:
                    dish_instance = dish_name_to_instance[dish_name]
                else:
                    # Se não, criar uma nova instância de Dish
                    dish_instance = Dish(dish_name, price)
                    # Mapear o nome do prato para a instância
                    dish_name_to_instance[dish_name] = dish_instance

                # Criar uma instância de Ingredient
                ingredient_instance = Ingredient(ingredient_name)
                # Adicionar a dependência de ingrediente ao prato
                dish_instance.add_ingredient_dependency(
                    ingredient_instance, recipe_amount)

                # Adicionar o prato ao conjunto de pratos
                self.dishes.add(dish_instance)
