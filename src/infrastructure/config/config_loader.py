import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")

def load_config():
    """Carrega a configuração do arquivo config.yaml"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config

# Carregar a configuraçãoo ao importar o m�dulo
config = load_config()