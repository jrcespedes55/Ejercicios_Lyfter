# ---- Suma de números ----

def sum_numbers(*numbers):
    return sum(numbers)


# ---- Calcular promedio ----

def calculate_average(*numbers):
    if not numbers:
        raise ValueError("At least one number is required")

    return sum(numbers) / len(numbers)


# ---- Conversión de temperatura ----

def convert_temperature(temperature, from_unit):

    if from_unit == "C":
        return (temperature * 9/5) + 32

    elif from_unit == "F":
        return (temperature - 32) * 5/9

    else:
        raise ValueError("Invalid unit. Use 'C' or 'F'")