# 🚀 Minha Primeira Maratona 🎮

Bem‑vindo(a) à mini-maratona! Este é um espaço criado especialmente para quem está começando no mundo da programação. Para deixar as coisas mais animadas, vamos desenvolver em **Python** e no desenvolvimento de jogos com a biblioteca **Pygame**.

---

## O que é Pygame?

[Pygame](https://www.pygame.org/news) é um conjunto de módulos Python projetado para escrever videogames. Ele adiciona funcionalidades sobre a biblioteca **SDL**, permitindo que você crie jogos e programas multimídia ricos em recursos, de forma simples e divertida.

---

## 📋 Pré‑requisitos

Antes de começar, garanta que você tenha **todos** os softwares a seguir instalados na sua máquina:

- **Python 3.8 ou superior** – [Download do Python](https://www.python.org/downloads/)
- **Git** – [Download do Git](https://git-scm.com/downloads)

Verifique se o Python está instalado abrindo seu terminal (Prompt de Comando, PowerShell ou Bash) e digitando:

```bash
python --version
```

---

## ⚙️ Como Começar (Passo a Passo)

Siga estes passos para colocar o projeto para rodar em seu computador.

### Passo 1 – Faça um *Fork* do Projeto

1. Clique no botão **Fork** no canto superior direito desta página.
2. Agora você terá uma cópia do repositório em **github.com/SEU‑NOME‑DE‑USUARIO/nome‑do‑projeto**.

### Passo 2 – Clone o Seu Fork

Baixe o projeto para a sua máquina clonando o repositório que acabou de criar:

```bash
# Substitua a URL abaixo pela do **seu** fork
git clone https://github.com/SEU-NOME-DE-USUARIO/nome-do-projeto.git
```

### Passo 3 – Navegue até a Pasta do Projeto

```bash
cd nome-do-projeto
```

### Passo 4 – Crie e Ative um Ambiente Virtual

Isolamos as dependências do projeto para não interferir em outras instalações do Python:

```bash
# Cria um ambiente virtual chamado "venv"
python -m venv venv

# Ativa o ambiente virtual
# Windows:
venv\Scripts\activate

# macOS ou Linux:
source venv/bin/activate
```

Após ativar, você verá **(venv)** no início da linha do terminal.

### Passo 5 – Instale as Dependências (`requirements.txt`) ✨

Todos os projetos Python profissionais listam suas bibliotecas externas em um arquivo `requirements.txt`. Instale tudo de uma vez:

```bash
pip install -r requirements.txt
```

### Passo 6 – Rode o Jogo! 🚀

```bash
python main.py
```

*(Se o arquivo principal tiver outro nome, como `game.py`, use esse nome no comando.)*

---

## 🤝 Como Contribuir

1. Certifique‑se de que você já **fez o fork** e **clonou** o projeto.
2. Crie uma nova branch para a sua modificação:

   ```bash
   git checkout -b feature/MinhaNovaFeature
   ```

3. Faça suas alterações e registre seus commits:

   ```bash
   git commit -m "Adiciona uma nova feature incrível"
   ```

4. Envie suas alterações para o seu fork:

   ```bash
   git push origin feature/MinhaNovaFeature
   ```

5. Abra um **Pull Request** para o repositório original.

---

Parabéns por chegar até aqui! **Divirta‑se programando e jogando!** 🐍
