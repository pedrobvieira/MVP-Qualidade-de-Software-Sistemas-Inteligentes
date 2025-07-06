document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultArea = document.getElementById('result-area');
    const submitButton = form.querySelector('.submit-button');
    const buttonText = submitButton.querySelector('.button-text');
    const buttonLoader = submitButton.querySelector('.button-loader');

    // URL completa da sua API Flask
    const API_URL = 'http://127.0.0.1:5000/predict';

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        setLoading(true);

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            // Usamos a URL completa da API
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Ocorreu um erro no servidor.');
            }

            const result = await response.json();
            displayResult(result);

        } catch (error) {
            displayError(error.message);
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        if (isLoading) {
            submitButton.disabled = true;
            buttonText.style.display = 'none';
            buttonLoader.style.display = 'inline-block';
        } else {
            submitButton.disabled = false;
            buttonText.style.display = 'inline-block';
            buttonLoader.style.display = 'none';
        }
    }

    function displayResult(result) {
        const isDanger = result.prediction === 1;
        const resultClass = isDanger ? 'result-danger' : 'result-success';
        const resultIcon = isDanger ? '💔' : '💚';
        
        resultArea.innerHTML = `
            <div class="${resultClass}">
                <h2>${result.interpretation} ${resultIcon}</h2>
                <p>O modelo prevê este resultado com uma confiança de 
                    <strong>${result.confidence}</strong>.
                </p>
                <p class="disclaimer">
                    Atenção: Este é um resultado gerado por um modelo de machine learning e não substitui uma avaliação médica profissional.
                </p>
            </div>
        `;
        resultArea.style.display = 'block';
    }

    function displayError(errorMessage) {
        resultArea.innerHTML = `
            <div class="result-error">
                <strong>Erro ao processar a predição:</strong>
                <p>${errorMessage}</p>
            </div>
        `;
        resultArea.style.display = 'block';
    }
});
