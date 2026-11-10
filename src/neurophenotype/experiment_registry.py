"""Minimal reproducible experiment registry for local and Colab runs.

Artifacts are written to local scratch space first, then copied to Drive with
hash verification. This is not a replacement for immutable backups or DVC.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import uuid


def sha256_file(path, block_size=1024 * 1024):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(block_size), b""):
            digest.update(block)
    return digest.hexdigest()


def create_run(root, *, project, code_commit, kind="environment_check", details=None):
    """Create a unique, append-only JSON run record. Returns (run_id, path)."""
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
    run_dir = root / run_id
    run_dir.mkdir(exist_ok=False)
    payload = {
        "schema_version": 1,
        "run_id": run_id,
        "created_at_utc": now.isoformat(),
        "project": str(project),
        "kind": str(kind),
        "code_commit": str(code_commit),
        "details": details or {},
        "note": "Infrastructure test only; no biological model trained.",
    }
    metadata = run_dir / "run.json"
    metadata.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return run_id, metadata


def export_file_verified(source, destination):
    """Copy a file without overwriting a different existing artifact."""
    source = Path(source)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    digest = sha256_file(source)
    if destination.exists():
        if sha256_file(destination) == digest:
            return digest
        raise FileExistsError(f"Conflicting artifact exists: {destination}")
    # Copy to a temporary name in the same folder then rename.
    temp = destination.with_name(destination.name + "." + uuid.uuid4().hex[:8] + ".partial")
    try:
        shutil.copy2(source, temp)
        if sha256_file(temp) != digest:
            raise IOError("Copy checksum verification failed")
        temp.rename(destination)
        if sha256_file(destination) != digest:
            raise IOError("Final checksum verification failed")
        return digest
    finally:
        if temp.exists():
            temp.unlink()
