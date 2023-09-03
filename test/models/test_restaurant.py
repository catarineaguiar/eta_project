from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = f"Nome do restaurante: {restaurant_name}" \
                          f"O que serve: {cuisine_type}" \
                          f"Clientes já atendendidos: 0."

        result = restaurant.describe_restaurant()

        assert result == expected_result

    def test_open_restaurant_success(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = f"{restaurant_name} agora está aberto!"

        result = restaurant.open_restaurant()

        assert result == expected_result

    def test_open_restaurant_already_open(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open = True
        expected_result = f"{restaurant_name} já está aberto!"

        result = restaurant.open_restaurant()

        assert result == expected_result

    def test_close_restaurant(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open = True
        expected_result = f"{restaurant_name} agora está fechado!"

        result = restaurant.close_restaurant()

        assert result == expected_result

    def test_close_restaurant_already_closed(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = f"{restaurant_name} já está fechado!"

        result = restaurant.close_restaurant()

        assert result == expected_result

    def test_set_number_served(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open = True
        total_customers = 10

        result = restaurant.set_number_served(total_customers)

        assert result == total_customers

    def test_set_number_served_closed_restaurant(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = f"{restaurant_name} está fechado!"
        total_customers = 10

        result = restaurant.set_number_served(total_customers)

        assert result == expected_result

    def test_increment_number_served(self):
        restaurant_name = "Comida Boa Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        restaurant.open = True
        initial_customers = 5
        increment_customers = 3
        expected_customers = initial_customers + increment_customers

        restaurant.number_served = initial_customers
        result = restaurant.increment_number_served(increment_customers)

        assert expected_customers == result
