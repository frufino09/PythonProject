from Provider import Provider


class Fabric:
    def __init__(self):
        self.provider_list = [
            Provider("Emil", 12),
            Provider("juanito", 15),
            Provider("pablito", 10)
        ]

    def show_average_unit_value(self):
        sum_value = 0
        for provider in self.provider_list:
            sum_value += provider.unit_value
        average = sum_value / len(self.provider_list)
        return average

    def show_name_provider_low_unit_value(self):
        low_unit_value = 9999999999
        name_provider = ""
        for provider in self.provider_list:
            if low_unit_value > provider.unit_value:
                low_unit_value = provider.unit_value
                name_provider = provider.name
        return name_provider

    def show_unit_value_by_name_provider(self, name_provider):
        for provider in self.provider_list:
            if provider.name == name_provider:
                return provider.unit_value
        return -1
