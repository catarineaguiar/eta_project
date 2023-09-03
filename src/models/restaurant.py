class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        restaurant_description = f"Nome do restaurante: {self.restaurant_name}" \
                                 f"O que serve: {self.cuisine_type}" \
                                 f"Clientes já atendendidos: {self.number_served}."

        return restaurant_description

    # correção de typo e escrita do método

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True  # deve ser true para abrir o restaurante e não é necessário número de clientes servidos
            return f"{self.restaurant_name} agora está aberto!"  # return ao invés de print
        else:
            return f"{self.restaurant_name} já está aberto!"  # return ao invés de print

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            # não é necessário o número de clientes atendidos
            return f"{self.restaurant_name} agora está fechado!"  # return ao invés de print
        else:
            return f"{self.restaurant_name} já está fechado!"  # return ao invés de print

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return total_customers  # adicionar o output do método
        else:
            return f"{self.restaurant_name} está fechado!"  # return ao invés de print

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers  # incrementar corretamente o número de clientes atendidos com +=
            return self.number_served  # adicionar o output do método
        else:
            return f"{self.restaurant_name} está fechado!"  # return ao invéns de print
