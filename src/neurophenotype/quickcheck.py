"""A small deterministic smoke test, not a trained model."""

import numpy as np

from neurophenotype.features.temporal import spike_train_features
from neurophenotype.features.waveform import waveform_features


def main():
    x = np.linspace(-1, 1, 81)
    w = -np.exp(-((x - 0.05) / 0.12) ** 2) + 0.3 * np.exp(-((x - 0.35) / 0.15) ** 2)
    morphology = waveform_features(w, sampling_rate_hz=20_000)
    dynamics = spike_train_features([0.2, 0.5, 0.9, 1.2], recording_duration_s=2.0)
    print("SYNTHETIC waveform:", morphology)
    print("SYNTHETIC spike train:", dynamics)
    print("Environment check successful; no real neuronal data or ML model was used.")


if __name__ == "__main__":
    main()
