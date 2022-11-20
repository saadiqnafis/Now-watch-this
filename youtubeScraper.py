import os
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def youtubeScraper(inputPlaylist, hours):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "DIRECTORY_OF_JSON_FROM_GOOGLE_CLOUD_OAUTH_CREDENTIALS"
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    api_key = os.environ.get('API_KEY_HERE_FROM_GOOGLE_CLOUD')
    nextPageToken = None

    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')
    data = {}
    while True:
        pl_request = youtube.playlistItems().list(
            part = 'contentDetails, snippet',
            playlistId= inputPlaylist,
            maxResults = 50, 
            pageToken = nextPageToken
        )
        pl_response = pl_request.execute()

        vid_ids = []
        vid_titles = []
        values = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])
            vid_titles.append(item['snippet']['title'])


        vid_request = youtube.videos().list(
            part='contentDetails',
            id=','.join(vid_ids), 
            )

        vid_response = vid_request.execute()
        i = 0
        for item in vid_response['items']:
            durationAsString = item['contentDetails']['duration']
            hours = hours_pattern.search(durationAsString)
            minutes = minutes_pattern.search(durationAsString)
            seconds = seconds_pattern.search(durationAsString)
            hours = int(hours.group(1) if hours else 0)
            minutes = float(minutes.group(1) if minutes else 0)
            seconds = float(seconds.group(1) if seconds else 0)
            value = [(hours + (minutes/60) + (seconds/3600)), ("http://img.youtube.com/vi/%s/0.jpg" % item['id']), vid_titles[i]]
            values.append(value)
            i += 1
        data.update(dict(zip(vid_ids, values)))
        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break

    sortedData = dict(sorted(data.items(), key=lambda item: item[1][0]))
    sortedBackwards = dict(sorted(data.items(), key=lambda item: item[1][0], reverse = True))
    toReturn = None
    for key in sortedData:
        for anotherKey in sortedBackwards:
            sum = sortedData.get(key)[0] + sortedBackwards.get(anotherKey)[0]
            if ((hours - (5/60)) <= sum <= (hours + (5/60))):
                toReturn = [{key: sortedData.get(key)}, {anotherKey: sortedBackwards.get(anotherKey)}]
                return toReturn
          
def main():
    print(youtubeScraper("PLRFyHSEtvvuQMIV8JD0L2IcDLoxTairpN", 1)) # test playlist, 1 hour

if __name__ ==  "__main__":
    main()