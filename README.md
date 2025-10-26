# Solar Cell Efficiency Predictor

This project uses a simple machine learning model to predict the efficiency of a solar cell based on the weights of two input substances.

The model is a **Linear Regression** trained to predict three key solar cell parameters:
* **Jsc** (Short-circuit current)
* **Voc** (Open-circuit voltage)
* **FF** (Fill Factor)

It then calculates the final **Efficiency** using these three values. The application includes a simple Graphical User Interface (GUI) built with Tkinter for easy prediction.

This model is trained *only* on data where the `synthesis_method` is 'solution combustion'.

## Features
* Trains a multi-output Linear Regression model using `scikit-learn`.
* Filters a dataset to use only a specific synthesis method.
* Provides a simple GUI to input two substance weights.
* Outputs the predicted Jsc, Voc, FF, and the final calculated Efficiency.
* Prints the model's Mean Squared Error (MSE) to the console upon running.

## Requirements
* Python 3.x
* The following Python libraries:
    * `pandas`
    * `numpy`
    * `scikit-learn`
    * `tkinter` (This is included in most standard Python installations)

## Data Requirements

To run this script, you must have a file named **`solar_cell_data.csv`** in the same directory.

This CSV file **must** contain the following columns:
* `synthesis_method`: The synthesis method used (e.g., 'solution combustion').
* `weight_a`: The weight of the first substance.
* `weight_b`: The weight of the second substance.
* `jsc`: The short-circuit current value.
* `voc`: The open-circuit voltage value.
* `ff`: The fill factor value.

## How to Use

1.  **Install the dependencies:**
    ```bash
    pip install pandas numpy scikit-learn
    ```

2.  **Prepare your data:**
    Ensure your `solar_cell_data.csv` file is in the same folder as the Python script.

3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your file)

4.  **Use the GUI:**
    * A window titled "Solar Cell Efficiency Predictor" will open.
    * Enter a value for "Weight A".
    * Enter a value for "Weight B".
    * Click the "Predict" button.
    * The predicted Jsc, Voc, FF, and final Efficiency will appear below the button.

## How It Works

1.  **Load Data**: The script loads `solar_cell_data.csv` into a pandas DataFrame.
2.  **Filter**: It filters the DataFrame to *only* include rows where the `synthesis_method` is 'solution combustion'.
3.  **Define Features (X) and Targets (y)**:
    * **X (Features)**: `weight_a`, `weight_b`
    * **y (Targets)**: `jsc`, `voc`, `ff`
4.  **Train Model**: The data is split into training (80%) and testing (20%) sets. A `LinearRegression` model is then trained on the training data.
5.  **Evaluate**: The model's Mean Squared Error (MSE) is calculated on the test set and printed to the console.
6.  **Predict**: The GUI captures user input for `weight_a` and `weight_b`, feeds it to the trained model, and gets the three predicted target values.
7.  **Calculate Efficiency**: The final efficiency is calculated using the standard formula:

    $$
    \text{Efficiency} = \frac{Jsc \times Voc \times FF}{100}
    $$
