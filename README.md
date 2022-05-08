# Corrector-Hackathon

Aquest és un projecte del Hackathon de l'assignatura de Sistemes Multimedia de la UAB.
El projecte és una web hostejada al Google Cloud que ha de ser capaç de corregir un input de text i indicar les faltes.

## Installation

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

![alt text](https://github.com/cristiangutierrz/Corrector-Hackathon/blob/main/public/fonts/imgs/capt1.png?raw=true)
