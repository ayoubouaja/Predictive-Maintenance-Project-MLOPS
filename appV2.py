from flask import Flask, request, render_template_string
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle entraîné
model_path = "/mnt/c/Users/fayed/Desktop/flask/modele_forest_simplifie.pkl"
modele = joblib.load(model_path)

# Nouvelle route pour l'interface utilisateur
@app.route('/', methods=['GET'])
def home():
    return render_template_string('''
<html>
<head>
    <title>Predictive Maintenance</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            padding-top: 20px;
        }
        .predict-form {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2 class="mb-4">Entrez vos données pour la prédiction</h2>
        <form action="/predict" method="post" class="predict-form">
            <div class="mb-3">
                <label for="Type_H" class="form-label">Type_H:</label>
                <input type="number" class="form-control" id="Type_H" name="Type_H" required>
            </div>
            <div class="mb-3">
                <label for="Type_L" class="form-label">Type_L:</label>
                <input type="number" class="form-control" id="Type_L" name="Type_L" required>
            </div>
            <div class="mb-3">
                <label for="Type_M" class="form-label">Type_M:</label>
                <input type="number" class="form-control" id="Type_M" name="Type_M" required>
            </div>
            <div class="mb-3">
                <label for="AirTemperatureK" class="form-label">Air temperature [K]:</label>
                <input type="number" class="form-control" id="AirTemperatureK" name="Air temperature [K]" required>
            </div>
            <div class="mb-3">
                <label for="ProcessTemperatureK" class="form-label">Process temperature [K]:</label>
                <input type="number" class="form-control" id="ProcessTemperatureK" name="Process temperature [K]" required>
            </div>
            <div class="mb-3">
                <label for="RotationalSpeedRpm" class="form-label">Rotational speed [rpm]:</label>
                <input type="number" class="form-control" id="RotationalSpeedRpm" name="Rotational speed [rpm]" required>
            </div>
            <div class="mb-3">
                <label for="TorqueNm" class="form-label">Torque [Nm]:</label>
                <input type="number" class="form-control" id="TorqueNm" name="Torque [Nm]" required>
            </div>
            <div class="mb-3">
                <label for="ToolWearMin" class="form-label">Tool wear [min]:</label>
                <input type="number" class="form-control" id="ToolWearMin" name="Tool wear [min]" required>
            </div>
            <div class="mb-3">
                <label for="TWF" class="form-label">TWF:</label>
                <input type="number" class="form-control" id="TWF" name="TWF" required>
            </div>
            <div class="mb-3">
                <label for="HDF" class="form-label">HDF:</label>
                <input type="number" class="form-control" id="HDF" name="HDF" required>
            </div>
            <div class="mb-3">
                <label for="PWF" class="form-label">PWF:</label>
                <input type="number" class="form-control" id="PWF" name="PWF" required>
            </div>
            <div class="mb-3">
                <label for="OSF" class="form-label">OSF:</label>
                <input type="number" class="form-control" id="OSF" name="OSF" required>
            </div>
            <div class="mb-3">
                <label for="RNF" class="form-label">RNF:</label>
                <input type="number" class="form-control" id="RNF" name="RNF" required>
            </div>
            <button type="submit" class="btn btn-primary">Prédire</button>
        </form>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    print(data)
    data_df = pd.DataFrame([data])

   

    # Retirer les colonnes inutilisées
    data_df = data_df.drop(columns=['Machine failure', 'Product ID', 'UDI'], errors='ignore')


    # S'assurer que l'ordre des colonnes correspond à celui attendu par le modèle
    # Vous devrez lister ici toutes les colonnes dans le même ordre que lors de l'entraînement du modèle
    data_df = data_df[["Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]", "TWF", "HDF", "PWF", "OSF", "RNF","Type_H", "Type_L",    "Type_M"]]

    prediction = modele.predict(data_df)
    # Convertir les prédictions en un type de données standard de Python
    prediction = prediction.tolist()  # Convertir en liste si c'est un tableau NumPy
    return 'Prédiction : {}'.format(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
