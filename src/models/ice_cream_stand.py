from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            print("No momento temos os seguintes sabores de sorvete disponíveis:")
            return self.flavors  # retornar lista de sabores
        else:
            return "Estamos sem estoque atualmente!"  # return ao invés de print

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Sabor {flavor} disponível!"  # retornar apenas o sabor pedido
            else:
                return f"Sabor {flavor} não disponível!"  # retornar apenas o sabor pedido
        else:
            return "Estamos sem estoque atualmente!"  # return ao invés de print

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponível!"  # return ao invés de print
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"  # return ao invés de print
        else:
            print("Estamos sem estoque atualmente!")
