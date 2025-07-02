from googleapiclient.discovery import build
import requests

#Key da Google Cloud - YouTube v3
API_KEY = 'AIzaSyDPGxXM8qwTZVirYPH8IqjbZGR8_zqvFrg'
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

    print("Título:", snippet['title'])
    print("Canal:", snippet['channelTitle'])
    print("Visualizações:", stats.get('viewCount', 'N/A'))
    print("Likes:", stats.get('likeCount', 'N/A'))
    print("Dislikes (estimado):", dislikes)
    print("Comentários:", stats.get('commentCount', 'N/A'))

if __name__ == '__main__':
    #insira o ID presente na URL do vídeo no YouTube
    video_id = 'LZGSuj4SkRg'
    get_video_info(video_id)

#feito para estudos por Felipe Assis.