# Pokémon Finder

O **Pokémon Finder** é uma aplicação web interativa que permite aos usuários buscar informações detalhadas sobre Pokémon diretamente da **PokeAPI**. Desenvolvida com **Flask** no backend e estilizada com **Tailwind CSS** no frontend, a aplicação oferece uma experiência de usuário moderna, responsiva e fácil de usar.

## Funcionalidades Principais

### 🔍 Busca de Pokémon
Insira o nome de um Pokémon e obtenha informações completas, incluindo:
- **Nome:** O nome do Pokémon.
- **Imagem:** Uma imagem oficial do Pokémon.
- **Tipos:** Os tipos do Pokémon (ex: Fogo, Água, Elétrico).
- **Habilidades:** As habilidades especiais do Pokémon.
- **Altura:** A altura do Pokémon em metros.
- **Peso:** O peso do Pokémon em quilogramas.

### 🎨 Interface Amigável
- Design limpo e responsivo, funcionando perfeitamente em dispositivos móveis, tablets e desktops.

### ⚡ Feedback Instantâneo
- Se o Pokémon não for encontrado, o usuário recebe uma mensagem de erro clara.

## 🛠️ Tecnologias Utilizadas

- **Flask:** Um microframework Python utilizado para criar o backend da aplicação, gerenciando rotas e integração com a API.
- **Tailwind CSS:** Um framework CSS utilitário que permite criar designs responsivos e modernos de forma rápida.
- **PokeAPI:** Uma API RESTful que fornece dados detalhados sobre Pokémon, incluindo sprites, tipos, habilidades e muito mais.
- **JavaScript:** Utilizado para fazer requisições assíncronas (AJAX) e atualizar a interface do usuário sem recarregar a página.

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos
- Python 3.x instalado.
- pip para gerenciamento de dependências.

### 📌 Passos para Execução
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/pokemon-finder.git
   cd pokemon-finder
   ```
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python app.py
   ```
5. Acesse a aplicação no navegador:
   - http://127.0.0.1:5000/

## 📂 Estrutura do Projeto

- **app.py:** O coração do backend, contendo as rotas Flask e a lógica de integração com a PokeAPI.
- **templates/index.html:** A interface do usuário, construída com HTML, Tailwind CSS e JavaScript para interatividade.
- **requirements.txt:** Lista todas as dependências necessárias para executar o projeto.

## 💡 Exemplo de Uso
1. Acesse a aplicação no navegador.
2. No campo de busca, insira o nome de um Pokémon (ex: "pikachu").
3. Clique em **"Procurar"**.
4. Veja as informações do Pokémon, incluindo imagem, tipos, habilidades, altura e peso.

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m "Adicionando nova feature"
   ```
4. Envie as alterações:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um **Pull Request** explicando suas mudanças.

## 📜 Licença
Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo LICENSE para mais detalhes.

## 📞 Contato
Se você tiver dúvidas, sugestões ou quiser contribuir, entre em contato:

- **Nome:** [Seu Nome]
- **Email:** [seu-email@example.com]
- **GitHub:** [seu-usuario]

O **Pokémon Finder** é uma ferramenta simples e divertida para fãs de Pokémon que desejam explorar informações sobre seus Pokémon favoritos. **Divirta-se explorando o mundo dos Pokémon!** 🚀

## 📸 Capturas de Tela (Opcional)
Caso queira adicionar capturas de tela da aplicação em funcionamento, você pode incluir imagens demonstrativas.

- **Página Inicial**
- **Resultado da Busca**

