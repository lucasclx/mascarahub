
# Projeto: Máscara github

Este projeto foi criado como parte de um curso básico de **Git e GitHub** voltado para estudantes do ensino médio. O objetivo é permitir que os alunos pratiquem clonagem de repositórios 
## Descrição
A aplicação sobrepõe uma imagem de mascote ao feed da câmera, exibindo o vídeo apenas nas áreas marcadas em verde (`#22b14c`). O projeto permite capturar uma foto pressionando a tecla `f` e fechar a janela com a tecla `q`.

## Requisitos
- Python 3.x
- OpenCV
- NumPy

## Funcionalidades
- Sobrepõe uma imagem ao feed da câmera.
- Mostra o feed apenas nas áreas marcadas em verde.
- Salva uma imagem pressionando a tecla `f`.
- Fecha a câmera pressionando a tecla `q`.

## Instruções para Clonar e Executar
1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute o script**:
   ```bash
   python mascarahub.py
   ```
4. **Teclas de atalho**:
   - `f`: Captura uma foto.
   - `q`: Fecha a câmera.

## Estrutura do Projeto
- `mascarahub.py`: Código principal do projeto.
- `mascote.png`: Imagem usada como sobreposição.

## Exemplo de Uso
O feed da câmera será exibido apenas na área verde da imagem:

![Exemplo de Uso](https://via.placeholder.com/600x300) <!-- Substitua por um exemplo real -->

## Atividades Adicionais no GitHub
Como parte do curso, os alunos aprenderão a interagir com repositórios GitHub, incluindo as seguintes atividades:

1. **Criar um fork deste projeto**:
   - Clique no botão "Fork" no canto superior direito da página do repositório.
   - O fork criará uma cópia deste projeto no seu próprio perfil do GitHub.

2. **Abrir uma issue**:
   - Vá para a aba `Issues` e clique em `New issue`.
   - Descreva um possível problema ou sugestão de melhoria para o projeto.

3. **Criar um pull request**:
   - Modifique o código no seu fork e envie um pull request para contribuir com o projeto original.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
