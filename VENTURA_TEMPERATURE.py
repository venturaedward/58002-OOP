class TempConversion:
    def __init__(self, temp):
        self.__temp = temp  # encapsulation and mangling

    def __f_to_c(self):
        return round((self.__temp - 32) * 5 / 9, 2)

    def __k_to_c(self):
        return round(self.__temp - 273.15, 2)

    def __c_to_f(self):
        return round((self.__temp * 9 / 5) + 32, 2)

    def __k_to_f(self):
        return round((self.__temp * 1.8) - 459.67, 2)

    def __c_to_k(self):
        return round(self.__temp + 273.15, 2)

    def __f_to_k(self):
        return round((self.__temp + 459.67) / 1.8, 2)

    def convert_all(self):
        # show the six consecutive outputs
        print(f"{self.__temp} Fahrenheit is {self.__f_to_c()} Celsius")
        print(f"{self.__temp} Kelvin is {self.__k_to_c()} Celsius")
        print(f"{self.__temp} Celsius is {self.__c_to_f()} Fahrenheit")
        print(f"{self.__temp} Kelvin is {self.__k_to_f()} Fahrenheit")
        print(f"{self.__temp} Celsius is {self.__c_to_k()} Kelvin")
        print(f"{self.__temp} Fahrenheit is {self.__f_to_k()} Kelvin")


f_temp = float(input("Enter temperature in Fahrenheit: "))


temp_conv = TempConversion(f_temp)


temp_conv.convert_all()