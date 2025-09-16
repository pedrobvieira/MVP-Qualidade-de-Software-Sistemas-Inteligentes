# 🩺 Previsão de Doença Cardíaca - MVP de Qualidade de Software, Segurança e Sistemas Inteligentes

Breve descrição do projeto que utiliza algoritmos de **Machine Learning** para prever o risco de doença cardíaca em pacientes. O projeto é composto por um modelo de **classificação**, uma **API** em Flask para disponibilizá-lo e uma **interface web** interativa.

---

## 💻 Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

* **Linguagem:** Python, JavaScript
* **Machine Learning:** `Scikit-Learn`, `Pandas`, `NumPy`
* **Back-end:** `Flask`, `Flask-CORS`
* **Front-end:** HTML5, CSS3, JavaScript (Vanilla)
* **Testes:** `PyTest`

---

## 🚀 Como Executar o Projeto

Para rodar a aplicação, siga os passos abaixo. É necessário ter **Python 3** e **pip** instalados.

### 1. Executar o Back-end (API)

A partir da raiz do projeto, navegue até a pasta `api` e execute os comandos:

```bash
# 1. Navegue para a pasta da API
cd api

# 2. Crie e ative o ambiente virtual
python -m venv venv
# No Windows (cmd): .\venv\Scripts\activate.bat
# No macOS/Linux: source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor Flask
flask run

A API estará em execução em http://127.0.0.1:5000. Mantenha este terminal aberto.

2. Executar o Front-end
Abra a pasta front e execute o arquivo index.html em seu navegador. A forma mais fácil é usando a extensão Live Server no VS Code.

🧠 Sobre o Modelo de Machine Learning
O processo de criação do modelo está documentado no notebook_treinamento.ipynb e inclui as seguintes etapas:

Análise Exploratória dos dados.

Pré-processamento com Pipelines e StandardScaler.

Treino e Otimização de hiperparâmetros (com GridSearchCV) para os algoritmos KNN, Árvore de Decisão, Naive Bayes e SVM.

Avaliação dos modelos para seleção do mais adequado.

Exportação do modelo final para o arquivo heart_disease_model.pkl.

✅ Testes Automatizados
Para garantir a qualidade, foi implementado um teste automatizado com PyTest.

A partir da pasta api (e com o ambiente virtual ativado), execute o comando:

Bash

pytest
O teste verifica se o modelo carrega corretamente e se a sua acurácia está acima de um limiar pré-definido, prevenindo a implantação de um modelo de baixa performance.

🛡️ Segurança e Privacidade
Lidar com dados de saúde exige atenção redobrada à segurança e privacidade. As boas práticas de Desenvolvimento de Software Seguro (SSD) foram consideradas:

Anonimização de Dados: O dataset usado é anônimo. Em um cenário real, dados sensíveis seriam submetidos a pseudonimização, generalização e mascaramento.

Segurança da Aplicação: A API deve validar rigorosamente todos os dados recebidos (validação no back-end), e a comunicação em produção deve ser feita sobre HTTPS. Para garantir que apenas usuários autorizados acessem a API, seria implementado um sistema de autenticação e autorização.
