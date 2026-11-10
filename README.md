# NeuroPhenotype-ML

Reproducible research for **neurotransmitter-phenotype inference from in vivo extracellular single-unit recordings**.

> **Status:** infrastructure + initial feature extraction. No validated phenotype classifier has been trained. Electrophysiological predictions are not molecular ground truth.

## Research questions

1. Can *normalized extracellular spike waveforms* distinguish independently identified neuronal populations?
2. What is added by firing/burst and long-range temporal patterns?
3. Do predictions generalize across animals, studies, electrodes and recording conditions?
4. Can a system reject unknown or out-of-distribution cell types?

## Principles

- Ground truth requires independent labeling (e.g., verified optotagging or juxtacellular tagging + histology).
- Raw recordings are immutable; datasets and sources have checksums and licensing metadata.
- Never split individual spikes of the same neuron across train and test. Prefer animal- and dataset-level holdouts.
- Compare waveform-only, temporal-only and combined models. Track recording modality, filtering, state and origin as possible confounds.
- Avoid treating TH+ alone as universal proof of dopaminergic identity.
- Keep secrets, recordings and trained checkpoints out of Git.

## Where everything lives

- **GitHub:** source, lightweight notebooks, configs, manifests, documentation, tests.
- **Google Drive:** [NeuroPhenotype-ML](https://drive.google.com/drive/folders/1UahinboAZ6jeDY_k7oNrUa_sy3Fg4yWQ) for raw and processed recordings, training outputs, models and publication assets.
- **Google Colab:** interactive CPU/GPU notebooks. External GPU providers can run the same Python package/configs later.

See [storage map](docs/STORAGE_MAP.md), [research decisions](docs/DECISIONS.md) and [dataset registry](manifests/datasets.csv).

## Start on a machine with a checked-out repository

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m neurophenotype.quickcheck
```

For Colab, open [the environment notebook](notebooks/00_environment_check.ipynb) from GitHub (Colab → File → Open notebook → GitHub); follow instructions in its cells. This is a **private repository**, so you must authenticate to access and clone it in a Colab runtime. Opening a notebook and installing its Python package are separate actions. Never paste access tokens into notebooks or commit outputs containing credentials.

## Project organization

```text
src/neurophenotype/          reusable Python features and loaders
notebooks/                   short interactive studies
configs/experiments/         experiment specifications, not results
manifests/                   dataset provenance and labels
tests/                       automated checks
docs/                        protocols, decisions and storage documentation
data/, models/, runs/        local temporary copies (ignored by Git)
```

## Current milestones

- [x] Provision Drive and repository layout
- [x] Initial waveform / ISI feature functions and automated tests
- [ ] Audit identified LC and VTA sources at the **file-array** level
- [ ] Implement source-specific ABF/MAT/NWB adapters
- [ ] Validate train/test grouping by animal and domain
- [ ] Train baseline classifiers and evaluate out-of-distribution detection
- [ ] Add versioned cloud experiment execution and automatic checkpoints

## Publication readiness

Record data license, animal/session/neuron identifiers, acquisition and filtering metadata, preprocessing, Git commit, environment, split groups, random seed, model settings, evaluation metrics and model artifact for each experiment. Public data/code releases require rights review. No code license is selected yet.
