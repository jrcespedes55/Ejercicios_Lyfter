# ---- Suma de números ----

def sum_numbers(*numbers):
    return sum(numbers)


# ---- Calcular promedio ----

def calculate_average(*numbers):
    if not numbers:
        raise ValueError("At least one number is required")

    return sum(numbers) / len(numbers)


# ---- Conversión de temperatura ----

def convert_temperature(temperature, conversion):
    if conversion == "C":
        return (temperature * 9/5) + 32

    elif conversion == "F":
        return (temperature - 32) * 5/9

    else:
        raise ValueError("Invalid conversion. Use 'C' or 'F'")