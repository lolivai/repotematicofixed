import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','2055511005:AAF1CxoYtvSNZaBBJRMpDyFVQTNE4hi9XEI')
API_ID =  os.environ.get('api_id','7618603')
API_HASH = os.environ.get('api_hash','5646106d87debbd9becfb7f13856763f')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Krixt0').split(';')
#ACCES_USERS = ('tl_admin_user','Krixt0','MelodicSpinach','JMiguel07','DTB86','KiritoOMG')
#ACCES_USERS = os.environ.get(ACCES_USERS)
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc',''))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
