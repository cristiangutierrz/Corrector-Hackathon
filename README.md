# Corrector-Hackathon

https://corrector-hackathon-xdmdxx2tlq-ew.a.run.app

Aquest és un projecte del Hackathon de l'assignatura de Sistemes Multimedia de la UAB.
El projecte és una web hostejada al Google Cloud que ha de ser capaç de corregir un input de text i indicar les faltes.

## Probant el container en local
Abans de fer deploy al Google Cloud ens assegurem que el container es crea exitosament en la nostre màquina local.

### Prerequisites
Cal tindre Docker Desktop instalat per a veure la versió local de la web.

### Instalació Local
```bash
git clone https://github.com/cristiangutierrz/Corrector-Hackathon.git ~/.
cd ~/Corrector-Hackathon
docker build -t projecte_sm_gcp:latest .
docker run -p 8080:443 projecte_sm_gcp:latest
```

Si s'han fet bé els pasos a l'adreça http://localhost:8080 es podrà veure la UI de la web.

## Prototype Web UI

![alt text](https://github.com/cristiangutierrz/Corrector-Hackathon/blob/main/public/imgs/capt1.png?raw=true)

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
``


![alt text](https://github.com/cristiangutierrz/Corrector-Hackathon/blob/main/public/imgs/diagram.drawio.png?raw=true)
