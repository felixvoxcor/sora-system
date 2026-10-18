"""Archivo de respuestas crudas de la API. Cada captura queda en data/raw/ (gzip determinista)
y su SHA-256 se guarda en la fila del snapshot: permite re-auditar y detectar cambios de formato."""
import gzip, hashlib, json
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def canonical(payload):
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256(payload):
    return hashlib.sha256(canonical(payload)).hexdigest()


def save(name, payload, root=None):
    """Guarda payload como <root>/<name>.json.gz (mtime=0 => bytes reproducibles). Devuelve el sha256."""
    if payload is None:
        return None
    root = Path(root) if root else RAW_DIR
    root.mkdir(parents=True, exist_ok=True)
    data = canonical(payload)
    path = root / f"{name}.json.gz"
    if not path.exists():                      # append-only: nunca se sobreescribe
        with gzip.GzipFile(path, "wb", mtime=0) as f:
            f.write(data)
    return hashlib.sha256(data).hexdigest()
