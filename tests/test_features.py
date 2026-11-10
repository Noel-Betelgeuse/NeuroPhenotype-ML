import numpy as np
import pytest

from neurophenotype.features.temporal import spike_train_features
from neurophenotype.features.waveform import normalize_waveform, waveform_features


def test_trough_normalization_removes_amplitude_scale():
    w = np.array([0.0, 0.0, 0.0, -0.2, -1, -0.4, 0.5, 0.2, 0.0, 0.0])
    np.testing.assert_allclose(normalize_waveform(w), normalize_waveform(3.0 * w))
    assert normalize_waveform(w).min() == pytest.approx(-1.0)


def test_waveform_features_have_positive_width():
    x = np.linspace(-1, 1, 101)
    w = -np.exp(-((x - 0.02) / 0.12) ** 2) + 0.3 * np.exp(-((x - 0.35) / 0.15) ** 2)
    result = waveform_features(w, 20_000)
    assert result["trough_to_peak_ms"] > 0
    assert result["negative_half_width_ms"] > 0


def test_temporal_regular_spikes():
    result = spike_train_features([0.1, 0.3, 0.5, 0.7], 1.0)
    assert result["mean_firing_rate_hz"] == 4.0
    assert result["isi_cv2"] == pytest.approx(0.0)


def test_reject_unsorted_spikes():
    with pytest.raises(ValueError):
        spike_train_features([0.2, 0.1], 1.0)
