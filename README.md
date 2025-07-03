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
---

## 🎯 Sua Missão: Conserte e Evolua o Jogo!

Para tornar o aprendizado mais prático e divertido, este projeto foi deixado "quebrado" de propósito. Sua tarefa não é apenas encontrar os bugs, mas também evoluir o código. Pense nisso como um quebra-cabeça e uma oportunidade de mostrar sua criatividade!

### Tarefas Principais

* **Corrigir a Lógica Central:** Sua primeira missão é investigar o código para encontrar e consertar os problemas existentes. A colisão não funciona como deveria? O placar não atualiza corretamente? O personagem se move de forma estranha? Seja o(a) detetive e arrume a casa!
* **Adicionar Novas Funcionalidades:** Depois de consertar o básico, é hora de dar o seu toque especial. Um jogo se torna único com features criativas.

### ✨ Sugestões de Novas Features (para se inspirar)

* Adicionar efeitos sonoros (para movimento, pontuação, game over, etc.).
* Criar uma tela de início com um botão "Jogar" e o título do jogo.
* Implementar um sistema de "Jogar Novamente" que aparece após o fim da partida.
* Fazer a dificuldade aumentar com o tempo (por exemplo, a velocidade do jogo aumenta a cada 10 pontos).
* Salvar a pontuação mais alta (High Score) em um arquivo de texto para que ela persista entre as partidas.

### ✅ Critérios para uma Boa Avaliação

Seu **Pull Request** (sua proposta de contribuição) será analisado com carinho, e vamos levar em conta os seguintes pontos. Não se preocupe em ser perfeito, o esforço no aprendizado é o mais importante!

* **Funcionalidade:**
    * O jogo funciona como esperado após suas correções?
    * As novas features que você adicionou estão operando sem introduzir novos bugs?

* **Qualidade do Código:**
    * Seu código está legível e bem organizado?
    * Você usou nomes de variáveis claros e fáceis de entender (ex: `player_score` em vez de `ps`)?

* **Comentários no Código:**
    * Você comentou as partes mais importantes ou complexas do seu novo código para explicar o que elas fazem? Isso ajuda muito quem vai ler seu código no futuro.

* **Clareza nos Commits do Git:**
    * As mensagens dos seus commits são claras e descritivas? (ex: "Feat: Adiciona sistema de som para o jogador" em vez de "arquivos atualizados").

* **Criatividade e Esforço:**
    * Você foi além do básico? Tentou implementar algo que não estava na lista de sugestões? O esforço para aprender e aplicar novos conceitos será muito valorizado!

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

Parabéns por chegar até aqui! **Divirta‑se programando e jogando! Boa sorte!** 🐍
