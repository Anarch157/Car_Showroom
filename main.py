from tkinter import *
import sqlite3

# main window

root = Tk()
root.title('Inventory')
root.iconbitmap('c:/Users/Anarch3/Pictures/pics/anarchylogo.ico')
root.geometry("400x500")

# Info entries

car_name = Entry(root)
car_name.grid(row=0, column=1, pady=10, padx=10)
cost_price = Entry(root)
cost_price.grid(row=1, column=1, pady=10, padx=10)
selling_price = Entry(root)
selling_price.grid(row=2, column=1, pady=10, padx=10)
customer_name = Entry(root)
customer_name.grid(row=3, column=1, pady=10, padx=10)
salesman_name = Entry(root)
salesman_name.grid(row=4, column=1, pady=10, padx=10)

# Info labels

car_name_label = Label(root, text="car name")
car_name_label.grid(row=0, column=0, pady=10, padx=10)
cost_price_label = Label(root, text="cost price")
cost_price_label.grid(row=1, column=0, pady=10, padx=10)
selling_price_label = Label(root, text="selling price")
selling_price_label.grid(row=2, column=0, pady=10, padx=10)
customer_name_label = Label(root, text="customer name")
customer_name_label.grid(row=3, column=0, pady=10, padx=10)
salesman_name_label = Label(root, text="salesman name")
salesman_name_label.grid(row=4, column=0, pady=10, padx=10)


# Save

def save():
    connection = sqlite3.connect('cars.db')
    c = connection.cursor()

    c.execute("INSERT INTO inventory VALUES (:car_name, :cost_price, :selling_price, :customer_name, :salesman_name)",
              {
                  'car_name': car_name.get(),
                  'cost_price': cost_price.get(),
                  'selling_price': selling_price.get(),
                  'customer_name': customer_name.get(),
                  'salesman_name': salesman_name.get(),
              })

    connection.commit()
    connection.close()

    car_name.delete(0, END)
    cost_price.delete(0, END)
    selling_price.delete(0, END)
    customer_name.delete(0, END)
    salesman_name.delete(0, END)


save_button = Button(root, text="Save record", command=save)
save_button.grid(row=5, column=1, pady=10, padx=10)


# Query

def show():
    connection = sqlite3.connect('cars.db')
    c = connection.cursor()

    c.execute("SELECT *, oid FROM inventory")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[5]) + " " + str(record[0]) + " " + str(record[1]) + " " + str(
            record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"

    show_label = Label(root, text=print_records)
    show_label.grid(row=6, column=1, columnspan=2)
    connection.commit()
    connection.close()


show_button = Button(root, text="Show records", command=show)
show_button.grid(row=5, column=2, pady=10, padx=10)


# Update

def update():
    connection = sqlite3.connect('cars.db')
    c = connection.cursor()

    record_id = id_box.get()

    c.execute("""UPDATE inventory SET
            car_name = :car_name,
            cost_price = :cost_price,
            selling_price = :selling_price,
            customer_name = :customer_name,
            salesman_name = :salesman_name

            WHERE oid = :oid""",
              {'car_name': car_name_editor.get(),
               'cost_price': cost_price_editor.get(),
               'selling_price': selling_price_editor.get(),
               'customer_name': customer_name_editor.get(),
               'salesman_name': salesman_name_editor.get(),
               'oid': record_id
               }
              )

    connection.commit()
    connection.close()

    editor.destroy()


# Edit

def edit():
    # editor window

    global editor
    editor = Tk()
    editor.title('Editor')
    editor.iconbitmap('c:/Users/Anarch3/Downloads/anarchylogo.ico')
    editor.geometry("400x500")
    connection = sqlite3.connect('cars.db')
    c = connection.cursor()
    record_id = id_box.get()
    c.execute("SELECT * FROM inventory WHERE oid = " + record_id)
    records = c.fetchall()

    global car_name_editor
    global cost_price_editor
    global selling_price_editor
    global customer_name_editor
    global salesman_name_editor

    # Info entries

    car_name_editor = Entry(editor)
    car_name_editor.grid(row=0, column=1, pady=10, padx=10)
    cost_price_editor = Entry(editor)
    cost_price_editor.grid(row=1, column=1, pady=10, padx=10)
    selling_price_editor = Entry(editor)
    selling_price_editor.grid(row=2, column=1, pady=10, padx=10)
    customer_name_editor = Entry(editor)
    customer_name_editor.grid(row=3, column=1, pady=10, padx=10)
    salesman_name_editor = Entry(editor)
    salesman_name_editor.grid(row=4, column=1, pady=10, padx=10)

    # Info labels

    car_name_label_editor = Label(editor, text="car name")
    car_name_label_editor.grid(row=0, column=0, pady=10, padx=10)
    cost_price_label_editor = Label(editor, text="cost price")
    cost_price_label_editor.grid(row=1, column=0, pady=10, padx=10)
    selling_price_label_editor = Label(editor, text="selling price")
    selling_price_label_editor.grid(row=2, column=0, pady=10, padx=10)
    customer_name_label_editor = Label(editor, text="customer name")
    customer_name_label_editor.grid(row=3, column=0, pady=10, padx=10)
    salesman_name_label_editor = Label(editor, text="salesman name")
    salesman_name_label_editor.grid(row=4, column=0, pady=10, padx=10)

    for record in records:
        car_name_editor.insert(0, record[0])
        cost_price_editor.insert(0, record[1])
        selling_price_editor.insert(0, record[2])
        customer_name_editor.insert(0, record[3])
        salesman_name_editor.insert(0, record[4])

    # Update

    update_button = Button(editor, text="Update record", command=update)
    update_button.grid(row=4, column=2, pady=10, padx=10)

    connection.commit()
    connection.close()


edit_button = Button(root, text="Edit record", command=edit)
edit_button.grid(row=8, column=2, pady=10, padx=10)


# Delete

def delete():
    connection = sqlite3.connect('cars.db')
    c = connection.cursor()

    c.execute("DELETE from inventory WHERE oid = " + id_box.get())
    id_box.delete(0, END)

    connection.commit()
    connection.close()


id_box_label = Label(root, text="ID no.")
id_box_label.grid(row=7, column=0, pady=10, padx=10)

id_box = Entry(root)
id_box.grid(row=7, column=1, pady=10, padx=10)

delete_button = Button(root, text="Delete record", command=delete)
delete_button.grid(row=8, column=1, pady=10, padx=10)

root.mainloop()
