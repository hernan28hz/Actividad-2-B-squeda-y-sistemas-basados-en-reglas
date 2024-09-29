import networkx as nx
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definición del grafo con distancias (igual que antes)
grafo = {
    'A': {'B': 4, 'C': 8},
    'B': {'C': 1, 'D': 20},
    'C': {'D': 10},
    'D': {} 
}

# Crear un objeto Graph de NetworkX y agregar las aristas con sus pesos
G = nx.Graph()
for nodo, vecinos in grafo.items():
    for vecino, peso in vecinos.items():
        G.add_edge(nodo, vecino, weight=peso)

# Función para encontrar y mostrar la ruta más corta
def encontrar_ruta():
    inicio = entry_inicio.get()
    fin = entry_fin.get()
    try:
        ruta_mas_corta = nx.dijkstra_path(G, source=inicio, target=fin, weight='weight')
        label_resultado.config(text="La ruta más corta es: " + str(ruta_mas_corta))
    except nx.NetworkXNoPath:
        label_resultado.config(text="No se encontró una ruta entre los puntos especificados.")

# Función para dibujar el grafo
def dibujar_grafo():
    # Crear una nueva ventana para el gráfico
    ventana_grafo = tk.Toplevel(ventana)
    ventana_grafo.title("Rutas")
    ventana_grafo.geometry("500x300+600+100")  # Ancho 800, alto 600, x=100, y=100

    # Posicionamiento de los nodos
    pos = nx.spring_layout(G)

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    # Crear un canvas de matplotlib y colocarlo en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafo)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("IA que encuentra la ruta más corta")
ventana.geometry("350x230")

# Crear los elementos de la interfaz
label_inicio = tk.Label(ventana, text="Ingrese Punto de inicio (A,B,C,D):")
entry_inicio = tk.Entry(ventana)
label_fin = tk.Label(ventana, text="Ingrese Punto final (A,B,C,D):")
entry_fin = tk.Entry(ventana)
boton_calcular = tk.Button(ventana, text="Calcular ruta", command=encontrar_ruta)
label_resultado = tk.Label(ventana, text="")

# Botón para dibujar el grafo
boton_dibujar = tk.Button(ventana, text="Mostrar las rutas", command=dibujar_grafo)
boton_dibujar.pack()

# Colocar los elementos en la ventana
label_inicio.pack()
entry_inicio.pack()
label_fin.pack()
entry_fin.pack()
boton_calcular.pack()
label_resultado.pack()

# Iniciar la ventana
ventana.mainloop()