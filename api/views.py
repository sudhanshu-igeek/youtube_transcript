from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class GetTranscriptData(APIView):
    def post(self, request, *args, **kwargs):
        try:
            import requests

            url = request.data.get('url')

            payload = {}
            headers = {
            'origin': 'https://www.youtube.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'LOGIN_INFO=AFmmF2swRAIgau42Yk1Fwk21F-yUhs3o1HinqfFxfZu4x1-e4vbEHMECICWeRpsTsQc_tytjlklOXXX7UvsrHAEoovzPXPnz4LI9:QUQ3MjNmeXpvUnJXeEkySTRlYTRVLXVOWGFxUjlHV0NJMG5FR2JRWk5PcU1PZllhaVVWLU01VzRyc2FkT0NuNzlOS1FRazBMQnFfa0VTbEg2R0w1Qkw5ZWg5bWVIVHhPZVZBcERkVXB1Y0Q2Um93b2RRbHlxa0h5TXdXZTd5UmFUbm5rYU5QUHdpSHhRbXYxTi1KOE9BQmtMSEFEbUJENWt3; VISITOR_INFO1_LIVE=mdRARbkTgoo; VISITOR_PRIVACY_METADATA=CgJJThIEGgAgXw%3D%3D; _gcl_au=1.1.1541613745.1720700817; PREF=f7=4100&f6=40000000&tz=Asia.Calcutta&f5=30000; SID=g.a000nwiXaIxqv6IvTxMezioPOdR_r3kRS9_2ua5A6AP4COqfEkijKebtMd1xujYAHvvRUJbByAACgYKAcUSARMSFQHGX2Mie-QHnTXvMmL0fH-asor47RoVAUF8yKqHkdD62EbpEm2jHrjrlrYp0076; __Secure-1PSID=g.a000nwiXaIxqv6IvTxMezioPOdR_r3kRS9_2ua5A6AP4COqfEkijL0xDovOZI6V6O8ZmBG7VSAACgYKAUMSARMSFQHGX2Mikz9BoO_cqXCeue3kSI5xvxoVAUF8yKotr3yekdB_xl4z7wXQPgNf0076; __Secure-3PSID=g.a000nwiXaIxqv6IvTxMezioPOdR_r3kRS9_2ua5A6AP4COqfEkijY3cu02efIlwo2kn5saTPUgACgYKAQwSARMSFQHGX2MicbYsgq3L_hM8QH_dI5AbMhoVAUF8yKryi5HjEARAPrIP_9nO8k680076; HSID=ABDDnwW_mpnL1PD-g; SSID=AisfDULC7YrIdvhS3; APISID=doBb1kl20qZjZltF/Avp7z2UoSZp_C7haT; SAPISID=jz2mh5iqxIraz0Q_/AEBIzWm1-jjQBiVzg; __Secure-1PAPISID=jz2mh5iqxIraz0Q_/AEBIzWm1-jjQBiVzg; __Secure-3PAPISID=jz2mh5iqxIraz0Q_/AEBIzWm1-jjQBiVzg; YSC=XZcLVG7hjeg; __Secure-1PSIDTS=sidts-CjIBQlrA-IXVFq89On98J2LczUiNWCXdJI45Hcvmt5sQXP9-HY6VyMw_ULmOfRA7q7jJ4BAA; __Secure-3PSIDTS=sidts-CjIBQlrA-IXVFq89On98J2LczUiNWCXdJI45Hcvmt5sQXP9-HY6VyMw_ULmOfRA7q7jJ4BAA; SIDCC=AKEyXzVVxjfPqNJU_RXdxouf7mdZD2kPSPm2CSlQ-MvnoXHGOgBbHavUep0IQv0BH1unrLuikqc; __Secure-1PSIDCC=AKEyXzV5wliwuARJ_PLQ-1ral52hVIQ4HxNZzGISn3rxUojPKdWZkdtv3PWORge-83yjkyLCdg; __Secure-3PSIDCC=AKEyXzWc7xa19-y-JsPidNSo0SrsFGVIO14OdUYUqBq2sBDbhPKffzG9EEfUM3sGaEO6MVP1GGA; SIDCC=AKEyXzUAAUU33nIdYlz6fN8YpEgXoOhjpUjdXVGnRTiNBHZ_A2xJ1ftj4HQHJxhDSsFpYpaEZi0; __Secure-1PSIDCC=AKEyXzXoY6TNA3-C6-zKf-7vQ6Lml67OSDhWKreg_6E1wgyWCc9WriOIuY0wjtY9iz4XbA1Dtw; __Secure-3PSIDCC=AKEyXzVTio5gU-WPGuNOneHZ6U0qqs2S3rGgXqGJM6Nrz7iY9ER28ZBUsthQTyv06XJIdtOyYNo',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-form-factors': '"Desktop"',
            'sec-ch-ua-full-version': '"127.0.6533.119"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.119", "Chromium";v="127.0.6533.119"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"6.8.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'service-worker-navigation-preload': 'true',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-client-data': 'CP7nygE='
            }

            proxies = {
                "http": None,
                "https": None,
            }
            
            response = requests.request("GET", url, headers=headers, data=payload, verify=False, proxies=proxies)

            return Response({'message': 'Transcript data successfully retrieved.', 'data':response.text,  'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Exception as e:  
            return Response({'message': str(e), 'data': None,'status': status.HTTP_500_INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# import yt_dlp

# def get_download_url(video_url):
#     ydl_opts = {
#         'format': 'best',  # Get the best available quality
#         # 'username': 'sudhanshu.igeek@gmail.com',
#         # 'password': 'Sudhanshu@iGeek18',
#         'quiet': True,     # Suppress output
#         'noplaylist': True,  # Ensure we only download a single video
#         'extract_flat': True,  # Only get the URL, not download
#         'geo_bypass': True,
#         'proxy': 'http://qukxmoyl:d07h8p0o8rns@38.154.227.167:5868',
#         'cookiefile': 'cookies.txt'
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(video_url, download=False)
#         download_url = info_dict.get('url', None)
#         return download_url

# def download_audio(video_url):
#     ydl_opts = {
#         'format': 'bestaudio/best',  # Download the best audio available
#         'extractaudio': True,         # Extract audio
#         'audioformat': 'mp3',         # Specify audio format (can be mp3, wav, etc.)
#         'outtmpl': '%(title)s.%(ext)s',  # Template for output filename
#         'postprocessors': [{           # Define postprocessors
#             'key': 'FFmpegExtractAudio',  # Use FFmpeg to convert audio
#             'preferredcodec': 'mp3',       # Preferred audio codec
#             'preferredquality': '192',      # Preferred audio quality
#         }],
#         'geo_bypass': True,
#         'proxy': 'http://qukxmoyl:d07h8p0o8rns@38.154.227.167:5868',
#         'cookiefile': 'cookies.txt'
#     }
    
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         try:
#             ydl.download([video_url])
#             print("Audio downloaded successfully.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
            
            
class GetYTvideo(APIView):
    def post(self, request, *args, **kwargs):
        # try:
            video_url = request.data.get('url', None)

            # download_audio(video_url)
            # download_url = get_download_url(video_url)

            # if download_url:
            #     print(f"Download URL: {download_url}")
            #     return Response({'message': 'Video downloaded successfully.', 'data': download_url,'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
            # else:
            #     print("Failed to get the download URL.")
            #     return Response({'message': 'Failed to download the video.', 'data': None,'status': status.HTTP_500_INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            import os 
            from pytubefix import YouTube
            
            po_token = "MnQJwVEB38OF7gn5jGPt3kNCBI8jHoxoVaGJqiH_RxOFNmAfWZpi7t2fVHgNOWRBH_Kpfe3GcDGXeDz4W31UECKfz_wB"
            visitor_data = "CgtMWkhKZ2ZKaHFfQSiNgtq3BjIKCgJJThIEGgAgYA%3D%3D"
            
            yt = YouTube(video_url, proxies={'http':'http://qukxmoyl:d07h8p0o8rns@38.154.227.167:5868'}, use_po_token=True, visitor_data=visitor_data, po_token=po_token)
            video = yt.streams.filter(only_audio = True).first()
            destination = '/home/sudhanshu/Documents/Learning/djangoBE_on_pythonanywhere/youtube_transcript/'
            out_file = video.download(output_path = destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            return Response({'message':'Success', 'status':status.HTTP_200_OK}, status=status.HTTP_200_OK)
        # except Exception as e:
        #     # Handle other potential exceptions like invalid URLs, etc.
        #     return Response({'message': str(e), 'data': None,'status': status.HTTP_500_INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)