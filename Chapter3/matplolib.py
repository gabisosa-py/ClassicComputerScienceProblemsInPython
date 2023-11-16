import matplotlib.pyplot as plt

def mostrar_mapa(solucion):
    # Datos ficticios de regiones y sus colores
    regiones = list(solucion.keys())
    colores = list(solucion.values())

    # Dibujar el mapa con colores asignados a cada región
    plt.figure(figsize=(8, 6))
    plt.barh(regiones, [1] * len(regiones), color=colores)
    plt.xlabel('Colores')
    plt.title('Asignación de colores a regiones')
    plt.yticks(fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

# Suponiendo que 'solution' contiene la solución obtenida del CSP
solution = {
    'Western Australia': 'red',
    'Northern Territory': 'green',
    'South Australia': 'blue',
    'Queensland': 'red',
    'New South Wales': 'green',
    'Victoria': 'red',
    'Tasmania': 'blue'
}

mostrar_mapa(solution)
