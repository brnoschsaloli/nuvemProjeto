# 📚 Cloud

## 👨‍🎓 Nome do Aluno
**Breno Schneider Salles de Oliveira**

## 📝 Descrição do Projeto
Este projeto é uma **API dockerizada** integrada com um banco de dados **PostgreSQL**, desenvolvida para **gerenciar usuários** com funcionalidades de registro, login e autenticação utilizando **JWT**. Utilizando tecnologias como **Python, FastAPI, Docker e SQLAlchemy**, a aplicação realiza **web scraping** no serviço **OpenWeatherMap** para obter a previsão do clima da cidade de **São Paulo** nos próximos **5 dias**. A API permite que os usuários autenticados consultem informações detalhadas como temperatura prevista, condições climáticas, umidade e velocidade do vento. A integração com o banco de dados assegura o armazenamento seguro das credenciais dos usuários e a gestão eficiente das sessões autenticadas, proporcionando uma experiência segura e confiável para acessar dados meteorológicos atualizados.

### **Funcionalidades Implementadas:**
- **Scraping de Dados:** Coleta de informações específicas de **[OpenWeatherMap]**.
- **API RESTful:** Fornece endpoints para acessar os dados coletados.
- **Autenticação JWT:** Segurança para proteger os endpoints da API.
- **Containerização com Docker:** Facilita a implantação e execução da aplicação em qualquer ambiente.

## 🚀 Como Executar a Aplicação

### **Pré-requisitos**
- [Docker](https://www.docker.com/get-started) instalado na sua máquina.
- [Git](https://git-scm.com/downloads) instalado.

### **Passo a Passo**

1. **Baixe o arquivo docker-compose.yaml:** 

    <div style="margin-top:15px;"></div>

    - [docker-compose.yaml](compose/docker-compose.yaml)

    <div style="margin-top:15px;"></div>

2. **Certifique-se de que o Docker está rodando no seu computador**

<div style="margin-top:15px;"></div>

3. **Iniciar os Contêineres com Docker Compose:**

<div style="margin-top:15px;"></div>

   ```bash
   docker compose up -d
   ```

<div style="margin-top:15px;"></div>

4. **Acessar a Aplicação:**

    <div style="margin-top:15px;"></div>

    - A API estará disponível em [http://localhost:8000/docs](http://localhost:8000/docs).

## 📚 Documentação dos Endpoints da API

### **Autenticação**
- **Registrar Usuário**
  - **URL:** `/register/`
  - **Método:** `POST`
  - **Body:**
    ```json
    {
      "nome": "seu nome",
      "email": "seu email",
      "senha": "sua senha"
    }
    ```
  - **Descrição:** Registra um novo usuário e retorna um token JWT.

- **Login**
  - **URL:** `/login/`
  - **Método:** `POST`
  - **Body:**
    ```json
    {
      "email": "seu email",
      "senha": "sua senha"
    }
    ```
  - **Descrição:** Autentica um usuário e retorna um token JWT.

### **Previsão do Tempo**
- **Consultar Clima**
  - **URL:** `/consultar/`
  - **Método:** `GET`
  - **Headers:**
    ```
    Authorization: Bearer <seu_token_jwt>
    ```
  - **Descrição:** Retorna a previsão do tempo baseada nos dados coletados pelo web scraping.
  - **Resposta:**
    ```json
    {
      "previsao": [
        {
          "data": "2024-10-15",
          "temperatura_minima": 16.55,
          "temperatura_maxima": 26.89,
          "descricao": "nublado"
        },
        {
          "data": "2024-10-16",
          "temperatura_minima": 19.94,
          "temperatura_maxima": 30.03,
          "descricao": "nublado"
        }
        // Mais previsões...
      ]
    }
    ```

## 📸 Screenshots dos Endpoints Testados
![Exemplo de Uso do Endpoint Consultar Clima](./screenshots/registrar_usuario.png)

*Descrição da screenshot: Mostrando a resposta do endpoint `/registrar/`.*

![Exemplo de Uso do Endpoint Registrar Usuario](./screenshots/login_usuario.png)

*Descrição da screenshot: Mostrando a resposta do endpoint `/login/`.*

![Exemplo de Uso do Endpoint Login Usuario](./screenshots/consulta_clima.png)

*Descrição da screenshot: Mostrando a resposta do endpoint `/consultar/` com a previsão do tempo.*


## 🎥 Vídeo de Execução da Aplicação

<a href="https://youtu.be/Z46RP-SC9Jo" style="display: block; border: 2px solid black; padding: 10px; width: fit-content; margin-bottom: 20px; ">
    <img src="screenshots/video_thumbnail.png" alt="Exemplo de imagem" width="400" style="display: block; max-width: 100%; height: auto;">
</a>

*Descrição: Vídeo demonstrando a execução da aplicação e a interação com os endpoints da API.*

## 📦 Link para o Docker Hub do Projeto
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-Repository-blue)](https://hub.docker.com/r/brnoschsaloli/nuvemprojeto)

*Descrição: Link para a imagem Docker do projeto no Docker Hub.*

---