# Reglas definir el nombre de variables

# 1. Comenzar con letra o guion bajo.
mi_variable = 30

# 2. Puede continuar con letras, números o guion bajo.
mi_variable_2 = 40
# nota: si inicia con número ejemplo: 3mi_variable = 30 muestra un error.

# 3. Sensible a mayúsculas y minúsculas.
Mi_variable = 50
print("mi_variable: ")
print(mi_variable)
# nota: la variable a ejecutar en este caso es "mi_variable" = 30 todo en minúscula

# 4. No se pueden usar palabras reservadas (keyword)
# class = 50 da error por ser class palabra reservada
klass = 50   # al cambiar C por K ya hace que la palabra no sea la reservada.
print("la variable Klass es de:")
print(klass)


# Buenas prácticas en Python
# Notación Snake Case (notación de serpiente)
nombre_usuario = 'Juan' # Notación Snake Case
nombreUsuario = 'Joel'  # Notación Camel Case ---> No se recomienda en Python
NombreUsuario = 'José'  # Notación Pascal Case --> No se recomienda en Python
# Nota: Existen varias Notaciones, pero no en python solo se recomienda Snake Case.
