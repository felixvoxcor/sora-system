"""SQLite append-only. Los snapshots (predicciones) NO se pueden modificar ni borrar:
asi el historial no se puede reescribir despues de ver el resultado."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "lab.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS results(
  event_id TEXT PRIMARY KEY, ts TEXT, day_et TEXT, season INTEGER,
  home TEXT, away TEXT, home_score INTEGER, away_score INTEGER);
CREATE TABLE IF NOT EXISTS snapshots(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id TEXT, label TEXT, taken_at TEXT, tip_ts TEXT, home TEXT, away TEXT,
  provider_id TEXT, line REAL, home_px REAL, away_px REAL, open_line REAL, total REAL,
  pred_a REAL, pred_b REAL, inj_adj REAL, model_version TEXT, injuries_json TEXT,
  raw_sha256 TEXT, inj_sha256 TEXT,
  UNIQUE(event_id, label));
CREATE TABLE IF NOT EXISTS games_seen(
  event_id TEXT PRIMARY KEY, tip_ts TEXT, home TEXT, away TEXT, first_seen TEXT);
CREATE TABLE IF NOT EXISTS capture_log(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id TEXT, label TEXT, attempted_at TEXT, tte_hours REAL, status TEXT);
CREATE TABLE IF NOT EXISTS closes(
  event_id TEXT PRIMARY KEY, provider_id TEXT, close_line REAL,
  home_px REAL, away_px REAL, fetched_at TEXT);
CREATE TABLE IF NOT EXISTS minutes(
  event_id TEXT, player_id TEXT, team TEXT, day_et TEXT, minutes REAL, pm REAL,
  PRIMARY KEY(event_id, player_id));
CREATE TABLE IF NOT EXISTS line_path(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id TEXT, taken_at TEXT, tte_hours REAL, provider_id TEXT,
  line REAL, home_px REAL, away_px REAL, total REAL);
CREATE TABLE IF NOT EXISTS injury_log(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  taken_at TEXT, team TEXT, player_id TEXT, name TEXT, status TEXT);
CREATE TRIGGER IF NOT EXISTS snapshots_no_update BEFORE UPDATE ON snapshots
  BEGIN SELECT RAISE(ABORT, 'snapshots es append-only'); END;
CREATE TRIGGER IF NOT EXISTS snapshots_no_delete BEFORE DELETE ON snapshots
  BEGIN SELECT RAISE(ABORT, 'snapshots es append-only'); END;
"""


def connect(path=None):
    p = Path(path) if path else DB_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(p)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    cols = {r["name"] for r in con.execute("PRAGMA table_info(snapshots)")}
    for c in ("raw_sha256", "inj_sha256"):          # migracion de bases creadas con v1.0
        if c not in cols:
            con.execute(f"ALTER TABLE snapshots ADD COLUMN {c} TEXT")
    return con
