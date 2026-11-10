import json

import pytest

from neurophenotype.experiment_registry import (
    create_run,
    export_file_verified,
    sha256_file,
)


def test_create_unique_runs(tmp_path):
    a, file_a = create_run(tmp_path, project="NeuroPhenotype-ML", code_commit="abc123")
    b, file_b = create_run(tmp_path, project="NeuroPhenotype-ML", code_commit="abc123")
    assert a != b
    assert json.loads(file_a.read_text())["code_commit"] == "abc123"
    assert file_b.exists()


def test_export_verifies_and_does_not_overwrite(tmp_path):
    source = tmp_path / "source.json"
    source.write_text('{"ok":true}')
    dst = tmp_path / "remote" / "run.json"
    digest = export_file_verified(source, dst)
    assert digest == sha256_file(dst)
    assert export_file_verified(source, dst) == digest
    source.write_text('{"ok":false}')
    with pytest.raises(FileExistsError):
        export_file_verified(source, dst)
