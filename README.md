# App Microservices

A test of a app web for Flask and MySQL with microservices.

## Prerequisites

Make sure you have Python 3.10 installed on your system and the necessary dependencies installed before running the application. You can install the dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Config Env

The config default is preload, but for setting for production or dev the config is set on variable of enviroment

### PowerShell
```powershell
$env:YOURAPPLICATION_SETTINGS = "config.ProductionConfig"
```

### Bash
```bash
export YOURAPPLICATION_SETTINGS="config.ProductionConfig"
```