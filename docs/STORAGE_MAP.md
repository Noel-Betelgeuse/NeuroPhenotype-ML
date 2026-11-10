# Storage map

Google Drive root: https://drive.google.com/drive/folders/1UahinboAZ6jeDY_k7oNrUa_sy3Fg4yWQ

- `01_DATASETS/00_INBOX` — incoming files to inspect before classifying.
- `01_DATASETS/01_RAW_PUBLIC` — original public recordings, immutable.
- `01_DATASETS/02_RAW_INTERNAL` — lab data (restricted permissions required).
- `01_DATASETS/03_DATASET_MANIFESTS` — local checksums and license snapshots.
- `02_PROCESSED_DATA` — feature tables, waveforms, temporal features, data splits.
- `03_MODELS` — checkpoints and release candidates.
- `04_EXPERIMENTS` — runs, benchmark scores, visualizations.
- `05_PUBLICATION` — manuscript, figures, supplementary and releases.
- `06_DOCUMENTATION` — protocols, dataset audit and decision log.
- `07_BACKUPS` — manual snapshots **not an independent backup**.

## Security

This folder was observed with **anyone-with-link: writer** access on 2026-11-10.
Before uploading internal, confidential or unpublished data, change it to Restricted
and grant access only to collaborators. GitHub is private but does not control Drive
permissions.

Use a separately administered backup for irreplaceable recordings.
