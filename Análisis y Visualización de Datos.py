import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class GraphApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gráfica de Barras")
        self.geometry("600x400")

        self.column_names = ["Categoría"]
        self.data_values = {}

        self.create_widgets()

    def create_widgets(self):
        self.category_label = tk.Label(self, text="Categoría")
        self.category_label.grid(row=0, column=0)

        self.value_label = tk.Label(self, text="Valor")
        self.value_label.grid(row=0, column=1)

        self.category_listbox = tk.Listbox(self, width=20)
        self.category_listbox.grid(row=1, column=0)

        self.value_listbox = tk.Listbox(self, width=20)
        self.value_listbox.grid(row=1, column=1)

        self.category_listbox.bind("<<ListboxSelect>>", self.edit_category_data)
        self.value_listbox.bind("<<ListboxSelect>>", self.edit_value_data)

        self.add_column_button = tk.Button(self, text="Agregar Columna", command=self.add_column)
        self.add_column_button.grid(row=2, column=0, columnspan=2)

        self.data_category_entry = tk.Entry(self)
        self.data_category_entry.grid(row=3, column=0)

        self.data_value_entry = tk.Entry(self)
        self.data_value_entry.grid(row=3, column=1)

        self.add_category_data_button = tk.Button(self, text="Datos Categoría", command=self.add_category_data)
        self.add_category_data_button.grid(row=4, column=0)

        self.add_value_data_button = tk.Button(self, text="Datos Valor", command=self.add_value_data)
        self.add_value_data_button.grid(row=4, column=1)

        self.delete_data_button = tk.Button(self, text="Eliminar Dato", command=self.delete_data)
        self.delete_data_button.grid(row=5, column=0, columnspan=2)

        self.plot_button = tk.Button(self, text="Graficar", command=self.plot_graph)
        self.plot_button.grid(row=6, column=0, columnspan=2)

    def add_column(self):
        self.column_names.append(f"Categoría {len(self.column_names)}")
        self.category_listbox.insert(tk.END, self.column_names[-1])
        self.value_listbox.insert(tk.END, "")

    def add_category_data(self):
        data_category = self.data_category_entry.get()
        data_value = self.data_value_entry.get()

        if data_category:
            if not data_value:
                data_value = "0"
            self.add_data(data_category, data_value)
            self.data_category_entry.delete(0, tk.END)
            self.data_value_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo Vacío", "Llene el campo antes de subir los datos.")

    def add_value_data(self):
        data_category = self.data_category_entry.get()
        data_value = self.data_value_entry.get()

        if data_category and data_value:
            self.add_data(data_category, data_value)
            self.data_category_entry.delete(0, tk.END)
            self.data_value_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo Vacío", "Llene ambos campos antes de subir los datos.")

    def add_data(self, category, value):
        if category in self.data_values:
            self.data_values[category] += int(value)
        else:
            self.data_values[category] = int(value)

        self.update_listboxes()

    def delete_data(self):
        selected_index = self.category_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            category = self.category_listbox.get(selected_index)
            self.data_values.pop(category, None)
            self.update_listboxes()

    def update_listboxes(self):
        self.category_listbox.delete(0, tk.END)
        self.value_listbox.delete(0, tk.END)

        for category, value in self.data_values.items():
            self.category_listbox.insert(tk.END, category)
            self.value_listbox.insert(tk.END, str(value))

    def edit_category_data(self, event):
        selected_index = self.category_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            data_category = self.category_listbox.get(selected_index)
            self.data_category_entry.delete(0, tk.END)
            self.data_category_entry.insert(tk.END, data_category)

    def edit_value_data(self, event):
        selected_index = self.value_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            data_value = self.value_listbox.get(selected_index)
            self.data_value_entry.delete(0, tk.END)
            self.data_value_entry.insert(tk.END, data_value)

    def plot_graph(self):
        categories = list(self.data_values.keys())
        values = list(self.data_values.values())

        if not categories or not values:
            messagebox.showwarning("Datos Faltantes", "Ingrese datos en ambas tablas antes de graficar.")
            return

        plt.figure(figsize=(8, 6))
        plt.bar(categories, values)
        plt.xlabel("Categoría")
        plt.ylabel("Valor")
        plt.title("Gráfica de Barras")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = GraphApp()
    app.mainloop()
