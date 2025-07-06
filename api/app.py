from flask import Flask, request, jsonify
from flask_cors import CORS  # Importe o CORS
import joblib
import numpy as np
import pandas as pd

# Inicializa a aplicação Flask
app = Flask(__name__)

# Habilita o CORS para a aplicação, permitindo requisições de qualquer origem.
# Em produção, você pode restringir para o domínio do seu front-end.
CORS(app)

# Carrega o modelo de machine learning treinado
try:
    model = joblib.load('heart_disease_model.pkl')
    print("Modelo carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    model = None

# Rota opcional para verificar se a API está no ar ("health check")
@app.route('/')
def health_check():
    return jsonify({"status": "API está no ar"}), 200

# Define a rota para realizar a predição
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo não foi carregado. Verifique os logs do servidor.'}), 500

    try:
        data = request.get_json(force=True)
        features_order = [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
            'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]
        input_data = [float(data[feature]) for feature in features_order]
        final_features = np.array(input_data).reshape(1, -1)

        prediction = model.predict(final_features)
        probability = model.predict_proba(final_features)

        output = int(prediction[0])
        confidence = probability[0][1]

        return jsonify({
            'prediction': output,
            'confidence': f'{confidence:.2%}',
            'interpretation': 'Risco de Doença Cardíaca' if output == 1 else 'Baixo Risco de Doença Cardíaca'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Permite executar a aplicação diretamente com 'python app.py'
if __name__ == '__main__':
    # O host '0.0.0.0' torna a API acessível na sua rede local
    app.run(host='0.0.0.0', port=5000, debug=True)
