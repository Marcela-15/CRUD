import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Función para conectar a la base de datos MySQL
def connect_to_db():
    return mysql.connector.connect(
        user='system',
        password='ddx2v8x3',
        host='localhost',
        port='1521',
        database='oracle3'
    )

# Crear la conexión a la base de datos
connection = connect_to_db()

# Función para insertar un nuevo cliente en la base de datos
def insert_customer():
    try:
        cursor = connection.cursor()
        id = entry_id.get()
        name = entry_name.get()
        region = entry_region.get()
        cursor.callproc('insert_customerab', [id, name, region])
        connection.commit()
        messagebox.showinfo("Éxito", "Cliente insertado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()

# Función para actualizar un cliente en la base de datos
def update_customer():
    try:
        cursor = connection.cursor()
        id = entry_id.get()
        name = entry_name.get()
        region = entry_region.get()
        cursor.callproc('update_customerab', [id, name, region])
        connection.commit()
        messagebox.showinfo("Éxito", "Cliente actualizado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()

# Función para eliminar un cliente de la base de datos
def delete_customer():
    try:
        cursor = connection.cursor()
        id = entry_id.get()
        cursor.callproc('delete_customerab', [id])
        connection.commit()
        messagebox.showinfo("Éxito", "Cliente eliminado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()

# Función para consultar información de clientes
def select_customers():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customersab")
        records = cursor.fetchall()
        for record in records:
            print(record)
        messagebox.showinfo("Información", "Datos de clientes recuperados. Verifica la consola para más detalles.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()


root = tk.Tk()
root.title("CRUD para customersab")

tk.Label(root, text="ID").grid(row=0)
tk.Label(root, text="Nombre").grid(row=1)
tk.Label(root, text="Región").grid(row=2)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_region = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_region.grid(row=2, column=1)

tk.Button(root, text="Insertar", command=insert_customer).grid(row=3, column=0)
tk.Button(root, text="Actualizar", command=update_customer).grid(row=3, column=1)
tk.Button(root, text="Eliminar", command=delete_customer).grid(row=3, column=2)
tk.Button(root, text="Consultar información de clientes", command=select_customers).grid(row=4, columnspan=3)

root.mainloop()