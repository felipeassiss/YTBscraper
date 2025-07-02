# YTBscraper

![YouTube Logo](https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg)

Este projeto busca informações básicas de vídeos do YouTube, como título, canal, visualizações, likes, dislikes estimados e quantidade de comentários.

## Funcionalidades

- Pega dados oficiais do vídeo via YouTube Data API
- Consulta dislikes estimados pela API do Return YouTube Dislike
- Exibe as informações no terminal de forma simples

## Como usar

1. Crie uma chave da YouTube Data API (Google Cloud Console)
2. Configure a variável `API_KEY` no código com sua chave
3. Execute o script e informe o ID do vídeo que quer analisar

## Exemplo de saída

```
Título: Gameplay GTA VII
Canal: Gigaton Games
Visualizações: 9,999,999
Likes: 999,999
Dislikes (estimado): 0 
Comentários: 9,999
```

## Dependências

- Python 3.x  
- google-api-python-client  
- requests

Instale as dependências com:

```bash
pip install google-api-python-client requests
```

## Aviso
 
Este projeto utiliza uma API de terceiros para estimar o número de dislikes devido a remoção dos mesmos.
