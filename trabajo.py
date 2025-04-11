def obtener_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("Ingrese las temperaturas de los 7 días:")
    for i in range(7):
        while True:
            try:
                temp = float(input(f"{dias[i]}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingrese un número válido.")
    return temperaturas

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def encontrar_max_min(lista):
    max_temp = max(lista)
    min_temp = min(lista)
    dia_max = lista.index(max_temp)
    dia_min = lista.index(min_temp)
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return max_temp, dias_semana[dia_max], min_temp, dias_semana[dia_min]

def mostrar_alertas(lista):
    alertas = []
    for temp in lista:
      if temp > 40:
          alertas.append(f"ALERTA: Temperatura peligrosamente alta ({temp}°C)")
      elif temp < 0:
            alertas.append(f"ALERTA: Temperatura peligrosamente baja ({temp}°C)")
    return alertas

def main():
    print("\n--- Análisis de Temperaturas Semanales ---")
    temps = obtener_temperaturas()
    promedio = calcular_promedio(temps)
    max_temp, dia_max, min_temp, dia_min = encontrar_max_min(temps)
    alertas = mostrar_alertas(temps)
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dias_sobre_promedio = [dias_semana[i] for i in range(7) if temps[i] > promedio]

    print("\n--- Resultados ---")
    print(f"🔹 Máxima: {max_temp}°C (Día: {dia_max})")
    print(f"🔹 Mínima: {min_temp}°C (Día: {dia_min})")
    print(f"🔹 Promedio semanal: {promedio:.2f}°C")
    print(f"🔹 Días sobre el promedio: {', '.join(dias_sobre_promedio) or 'Ninguno'}")

    if alertas:
        print("\n⚠️ Alertas:")
        for alerta in alertas:
            print(alerta)

if __name__ == "__main__":
    main()