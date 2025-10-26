import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import messagebox

# Step 1: Load the data
data = pd.read_csv("solar_cell_data.csv")

# Print columns to make sure they're correct
print(data.columns)

# Step 2: Only use the rows with 'solution combustion' method
data = data[data['synthesis_method'].str.lower() == 'solution combustion']

# Step 3: Features (X) are the two substance weights; Targets (y) are jsc, voc, ff
X = data[['weight_a', 'weight_b']]
y = data[['jsc', 'voc', 'ff']]

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Test model accuracy
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 7: GUI using tkinter
def predict_efficiency():
    try:
        # Get user input
        weight_a = float(weight_a_entry.get())
        weight_b = float(weight_b_entry.get())

        # Create DataFrame for prediction
        input_df = pd.DataFrame([[weight_a, weight_b]], columns=['weight_a', 'weight_b'])

        # Predict jsc, voc, ff
        prediction = model.predict(input_df)
        jsc, voc, ff = prediction[0]

        # Calculate efficiency
        efficiency = (jsc * voc * ff) / 100

        # Display results
        jsc_label.config(text=f"Predicted Jsc: {jsc:.2f}")
        voc_label.config(text=f"Predicted Voc: {voc:.2f}")
        ff_label.config(text=f"Predicted FF: {ff:.2f}")
        efficiency_label.config(text=f"Efficiency: {efficiency:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the GUI
root = tk.Tk()
root.title("Solar Cell Efficiency Predictor")

# Title
title = tk.Label(root, text="Enter weights of two substances", font=("Arial", 14))
title.pack(pady=10)

# Inputs
tk.Label(root, text="Weight A:").pack()
weight_a_entry = tk.Entry(root)
weight_a_entry.pack()

tk.Label(root, text="Weight B:").pack()
weight_b_entry = tk.Entry(root)
weight_b_entry.pack()

# Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_efficiency)
predict_button.pack(pady=10)

# Results
jsc_label = tk.Label(root, text="Predicted Jsc: ")
jsc_label.pack()
voc_label = tk.Label(root, text="Predicted Voc: ")
voc_label.pack()
ff_label = tk.Label(root, text="Predicted FF: ")
ff_label.pack()
efficiency_label = tk.Label(root, text="Efficiency: ")
efficiency_label.pack()

# Run GUI
root.mainloop()
