from googleapiclient.discovery import build
import requests
import csv

#Key da Google Cloud - YouTube v3 ↓
API_KEY = 'INSIRA SUA CHAVE AQUI!!'
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_info(video_id):
    request = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    )
    response = request.execute()
    if not response['items']:
        print("Vídeo não encontrado")
        return

    video = response['items'][0]
    snippet = video['snippet']
    stats = video['statistics']

    dislike_url = f'https://returnyoutubedislikeapi.com/votes?videoId={video_id}'
    dislike_response = requests.get(dislike_url)
    if dislike_response.status_code == 200:
        dislike_data = dislike_response.json()
        dislikes = dislike_data.get('dislikes', 'N/A')
    else:
        dislikes = 'N/A'

    print("Título do vídeo:", snippet['title'])
    print("Canal:", snippet['channelTitle'])
    print("Views:", stats.get('viewCount', 'N/A'))
    print("Likes:", stats.get('likeCount', 'N/A'))
    print("Dislikes (estimado):", dislikes)
    print("Comentários:", stats.get('commentCount', 'N/A'))

    return {
        "Título do vídeo": snippet['title'],
        "Canal": snippet['channelTitle'],
        "Views": stats.get('viewCount', 'N/A'),
        "Likes": stats.get('likeCount', 'N/A'),
        "Dislikes (estimado)": dislikes,
        "Comentários": stats.get('commentCount', 'N/A')
    }

if __name__ == '__main__':
    #insira o ID presente na URL do vídeo no YouTube ↓
    video_id = 'LZGSuj4SkRg'
    info = get_video_info(video_id)

    if info:
        filename = 'youtube_video_info.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=info.keys())
            writer.writeheader()
            writer.writerow(info)
        print(f'Arquivo "{filename}" criado com sucesso.')

#feito para estudos por Felipe Assis.
