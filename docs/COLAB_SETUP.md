# Secure Colab workflow (private repository)

## First run

1. Open `notebooks/01_colab_bootstrap.ipynb` from GitHub inside Colab.
2. Make a GitHub **fine-grained personal access token** restricted to the single private repository, permission **Contents: Read-only**.
3. In Colab, open **Secrets** (key icon), add `GITHUB_TOKEN`, turn on notebook access. Never paste the token into notebook code, outputs, Drive docs, URLs or Issues.
4. Execute the cells sequentially. The notebook fetches an immutable GitHub commit archive, installs its local package, mounts Drive, confirms the existing `NeuroPhenotype-ML` folder, computes synthetic checks, and saves `run.json` under `04_EXPERIMENTS/RUNS/<run_id>/`.
5. If Drive folder is missing, **stop and inspect** which Google account is mounted; do not automatically create a duplicate.
6. Remove or revoke token if compromised. Use a dedicated minimal token with an expiry.

## What is and is not automatic

- GitHub Actions tests run automatically on push.
- Colab code runs only when the user executes it (or a separately configured job triggers it); Colab free sessions are not a reliable background scheduler.
- The bootstrap logs a synthetic smoke test, **not a validated phenotype classifier or real training run**.
- No secrets or biological raw data are stored in the GitHub repository.
- A Google Drive folder with link-wide write access is unsafe; restrict sharing before loading real lab data.

## External GPU portability

The Python package and YAML configs are platform-neutral. A future batch entrypoint will accept a config + dataset manifest and produce an immutable run ID, metrics and artifacts. This must be validated before claiming Runpod integration works.
