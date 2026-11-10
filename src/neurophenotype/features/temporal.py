"""Spike-train features; inputs are spike timestamps in seconds."""

import numpy as np


def spike_train_features(spike_times_s, recording_duration_s):
    """FR, ISI CV and local CV2; use NaN when too few events are available."""
    times = np.asarray(spike_times_s, dtype=np.float64)
    if times.ndim != 1 or not np.all(np.isfinite(times)):
        raise ValueError("timestamps must be a finite one-dimensional vector")
    if recording_duration_s <= 0:
        raise ValueError("recording_duration_s must be positive")
    if times.size and (times[0] < 0 or times[-1] > recording_duration_s):
        raise ValueError("timestamps outside recording interval")
    if np.any(np.diff(times) <= 0):
        raise ValueError("timestamps must be strictly increasing")
    isi = np.diff(times)
    cv = float(np.std(isi, ddof=1) / np.mean(isi)) if isi.size >= 2 else float("nan")
    if isi.size >= 2:
        cv2_values = 2 * np.abs(np.diff(isi)) / (isi[:-1] + isi[1:])
        cv2 = float(np.mean(cv2_values))
    else:
        cv2 = float("nan")
    return {
        "spike_count": int(times.size),
        "mean_firing_rate_hz": float(times.size / recording_duration_s),
        "median_isi_s": float(np.median(isi)) if isi.size else float("nan"),
        "isi_cv": cv,
        "isi_cv2": cv2,
    }
