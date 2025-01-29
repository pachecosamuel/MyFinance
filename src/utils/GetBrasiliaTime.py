# src/utils/__init__.py
from datetime import datetime, timezone
from pytz import timezone as pytz_timezone

def get_brasilia_time():
    """Retorna a data e hora atual em Brasília (UTC-3)."""
    return datetime.now(timezone.utc).astimezone(pytz_timezone('America/Sao_Paulo'))