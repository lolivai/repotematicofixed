# ownclouduploader
Bot De Telegram : RepoUploader, Descargador gratis de contenido desde internet a hacia nubes en cuba

# Deploy Usando Git Win Y Heroku Cli Desde PC
```
(CMD)
git clone https://github.com/Masabito/fixed
git init
git add .
git commit -m "OK"
heroku create myherokuapp
heroku git:remote myherokuapp
git push heroku master
```

# Comandos En El Bot (Usuarios nomales)
```/start : Inicar Bot , Te da La info
/ls : obtiene los archivos del root
/rm : remueve un archivo del root (index,range)
/up : comienza a sincronizar archivos desde el bot a la nube (index,range)
/zip : comprime 1 o varios archivos en partes zip (index,range zipsize)
```

# Deploy Directo (Heroku)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Masabito/fixed)
