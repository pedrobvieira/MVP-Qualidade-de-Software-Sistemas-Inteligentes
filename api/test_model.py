# ==============================================================================
# ARQUIVO: api/test_model.py (TESTE AUTOMATIZADO COM PYTEST)
#
# Para rodar:
# 1. Instale o pytest: `pip install pytest`
# 2. Execute o comando no terminal na pasta `api`: `pytest`
# ==============================================================================

import pytest
import joblib
import pandas as pd
import numpy as np 
from sklearn.metrics import accuracy_score

# Carrega o modelo uma vez para todos os testes
try:
    model = joblib.load('heart_disease_model.pkl')
except FileNotFoundError:
    model = None

# Define um threshold (limite) de desempenho aceitável
PERFORMANCE_THRESHOLD = 0.80

@pytest.fixture
def test_data():
    """ Fornece dados de teste para avaliação do modelo. """
    data = {
        'age': [63, 57, 58, 52], 'sex': [1, 0, 1, 1], 'cp': [3, 0, 0, 2],
        'trestbps': [145, 120, 132, 172], 'chol': [233, 354, 224, 199],
        'fbs': [1, 0, 0, 1], 'restecg': [0, 1, 0, 1], 'thalach': [150, 163, 173, 162],
        'exang': [0, 1, 0, 0], 'oldpeak': [2.3, 0.6, 3.2, 0.5],
        'slope': [0, 2, 2, 2], 'ca': [0, 0, 2, 0], 'thal': [1, 2, 3, 3]
    }
    labels = [1, 1, 0, 1] # Labels verdadeiros correspondentes
    df = pd.DataFrame(data)
    return {"features": df, "labels": labels}

@pytest.mark.skipif(model is None, reason="Modelo 'heart_disease_model.pkl' não encontrado.")
def test_model_performance(test_data):
    """ Testa se a acurácia do modelo no conjunto de teste está acima do threshold. """
    X_test_sample = test_data["features"]
    y_test_sample = test_data["labels"]
    predictions = model.predict(X_test_sample)
    accuracy = accuracy_score(y_test_sample, predictions)
    assert accuracy >= PERFORMANCE_THRESHOLD, f"Desempenho do modelo ({accuracy:.2f}) abaixo do esperado ({PERFORMANCE_THRESHOLD:.2f})."

@pytest.mark.skipif(model is None, reason="Modelo 'heart_disease_model.pkl' não encontrado.")
def test_prediction_output_type_and_shape():
    """ Testa se a saída da predição tem o tipo e formato esperados. """
    sample_input = np.array([[60, 1, 2, 140, 250, 0, 1, 155, 0, 1.5, 1, 0, 2]])
    prediction = model.predict(sample_input)
    probability = model.predict_proba(sample_input)
    assert isinstance(prediction[0], (np.int64, np.int32)), "A predição não é um inteiro."
    assert prediction.shape == (1,), "O formato da predição está incorreto."
    assert probability.shape == (1, 2), "O formato da probabilidade está incorreto."

