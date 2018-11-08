from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
http = credentials.authorize(httplib2.Http())        
drive_service = discovery.build('drive', 'v3', http=http)








# If modifying these scopes, delete the file token.json.

file_metadata = {
    'name': 'My Report',
    'mimeType': 'application/vnd.google-apps.document'
}
media = MediaFileUpload(r'C:\Users\Bayron\Desktop\Money\43placidln\email\3up.pdf',
                        mimetype='text/plain',
                        resumable=True)
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print('File ID: %s' % file.get('id'))
