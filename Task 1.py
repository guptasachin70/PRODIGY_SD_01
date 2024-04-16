import tkinter as tk

tempCels = 0.0
tempFahr = 0.0
tempKelvin = 0.0

def tempConverter(temp_unit_var, result_label):
    temp_str = entry.get()
    temp_unit = temp_unit_var.get()

    if not temp_str or not temp_str.replace(".","").isdigit():
        result_label.config(text = "Enter a valid temperature!")
        return
    
    temperature = float(temp_str)
    global tempCels, tempFahr, tempKelvin

    if temp_unit == "Celsius":
        tempFahr = (temperature * 9/5) + 32
        tempKelvin = temperature + 273.15
    elif temp_unit == "Fahrenheit":
        tempCels = (temperature - 32) * 5/9
        tempKelvin = (temperature - 32) * 5/9 + 273.15
    else:
        tempCels = temperature - 273.15
        tempFahr = (temperature - 273.15) * 9/5 + 32
    
    result_label.config(text = f"Celsius: {tempCels:.2f} \nFahrenheit: {tempFahr:.2f} \nKelvin: {tempKelvin:.2f} K")

window = tk.Tk()
window.title("Temerature Converter")

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

entry_label = tk.Label(window, text= "Enter Temperature: ", font = ("Helvetica", 12))
entry_label.pack()

entry = tk.Entry(window, font = ("Helvetica", 12))
entry.pack()

temp_unit_var = tk.StringVar(window)
temp_unit_var.set("Celsius")
unit_options = ["Celsius", "Fahrenheir", "Kelvin"]
unit_dropdown = tk.OptionMenu(window, temp_unit_var, *unit_options)
unit_dropdown.config(font = ("Helvetica", 12))
unit_dropdown.pack(pady=10)

convertButton = tk.Button(window, text = "Convert",command = lambda: tempConverter(temp_unit_var, result_label), font = ("Helvetica", 12))
convertButton.pack()

window.mainloop()