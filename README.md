# Corrector-Hackathon

Aquest és un projecte del Hackathon de l'assignatura de Sistemes Multimedia de la UAB.
El projecte és una web hostejada al Google Cloud que ha de ser capaç de corregir un input de text i indicar les faltes.

Soporta 2 mètodes:
- Typewise API: Una API externa que es crida amb Cloud Functions.
- pyspellchecker: Un paquet de la lliberia de python que s'executa al backend.

Llengues: 🇬🇧🇪🇸🇩🇪

https://corrector-sm.ew.r.appspot.com

![alt text](https://i.gyazo.com/2c2faec952fa46422f02a6f276eb7e56.gif)

### Instalació Local

```bash
git clone https://github.com/cristiangutierrz/Corrector-Hackathon.git ~/.
cd ~/Corrector-Hackathon
pip3 install -r requirements.txt
python3 main.py
```

Si s'han fet bé els pasos a l'adreça http://localhost:8080 es podrà veure la UI de la web.

Per a poder correr la web en local i que sigui funcional es requereix de les credencials del projecte en .json
Aquestes credencials no són a aquesta repo.

En cas de no tenir les credencials, es mostrarà a consola aquest missatge:
```
Falten les credencials del google cloud .json! No es podrà cridar a la API de Typewise.
```

## Google Cloud
Mitjançant l'api de Cloud Build de Google Cloud som capaços de enllaçar aquest repositori a l'instància del cloud. Això permitirà fer CI/CD donat que cada vegada que es faci un push a la main branch s'activarà un Build Trigger al cloud que llançarà una nova instància del nostre Dockerfile.

### Cloud Builder: `cloudbuild.yaml` file
Aquest trigger cada vegada que detecti canvis en la branc `main` torarà a fer deploy de la app.
* Per a fer-ho s'ha de donar permisos de "App Engine Deployer" a aquest usuari cloud builder.
```
steps:
- name: "gcr.io/cloud-builders/gcloud"
  args: ["app", "deploy"]
timeout: "1600s"
```
### App Engine: `app.yaml` file
Aquest fitxer serà l'utilitzat per fer el deploy de la app. Serà cridat pel cloud builder.
```
runtime: python39

handlers:
- url: /static
  static_dir: static
- url: /.*
  script: auto
```

![alt text](https://github.com/cristiangutierrz/Corrector-Hackathon/blob/main/public/imgs/diagram.drawio.png?raw=true)

Tenim dos mètodes per corregir text:

#### Package Local: pyspellchecker
És un package de python que permet fer correccions de text locals. S'executa en el servidor i només en el servidor.

#### External API: Typewise API
Mitjançant una cloud function podrem cridar a aquesta API externa i retornar els resultats.
