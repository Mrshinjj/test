from pyupdater.client import Client
from client_config import ClientConfig
def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print (downloaded, total, status)

if __name__ == '__main__':
    APP_NAME = 'test'
    APP_VERSION = '1.0.0'
    client = Client(
                ClientConfig(), refresh=True, progress_hooks=[print_status_info]
            )

    app_update = client.update_check(APP_NAME, APP_VERSION)

    if app_update is not None:
        print('app_update is not None')
        reulst =app_update.download()
        print('app_update.downlaod() 종료')
        if app_update.is_downloaded():
            print(f'is_downloaded() : {app_update.is_downloaded()}')
            # app_update.extract_overwrite()
            app_update.extract_restart()  
    else:
        print('app_update is None , 다운받을거 없음')