"""Morphology extraction for negative-trough extracellular spike templates.

WARNING: assumes negative-going extracellular action potentials with a
post-trough positive peak. Juxtacellular/positive-going recordings need a
separate validated adapter; never silently flip polarity.
"""

import numpy as np


def normalize_waveform(waveform, method="trough"):
    """Baseline-subtract then amplitude-normalize one 1-D spike template.

    The baseline is the median of the first max(3, 10% of samples) points.
    The waveform is not filtered or resampled here.
    """
    values = np.asarray(waveform, dtype=np.float64)
    if values.ndim != 1 or values.size < 8 or not np.all(np.isfinite(values)):
        raise ValueError("waveform must be finite 1-D with at least 8 points")
    n_baseline = max(3, values.size // 10)
    values = values - np.median(values[:n_baseline])
    if method == "trough":
        scale = abs(float(np.min(values)))
        if np.min(values) >= 0:
            raise ValueError("expected negative-going extracellular trough")
    elif method == "peak_to_peak":
        scale = float(np.ptp(values))
    else:
        raise ValueError("method must be 'trough' or 'peak_to_peak'")
    if scale <= 1e-12:
        raise ValueError("flat/near-flat waveform")
    return values / scale


def waveform_features(waveform, sampling_rate_hz):
    """Simple morphology features in milliseconds (negative trough convention).

    Output includes trough-to-positive-peak and negative half-width;
    these measurements are exploratory and must be checked against sampling,
    filtering and waveform polarity in each source.
    """
    if sampling_rate_hz <= 0:
        raise ValueError("sampling_rate_hz must be positive")
    w = normalize_waveform(waveform)
    trough = int(np.argmin(w))
    if trough >= len(w) - 2:
        raise ValueError("trough too close to waveform end")
    peak = trough + 1 + int(np.argmax(w[trough + 1:]))
    half_level = w[trough] / 2.0
    before = np.where(w[:trough] > half_level)[0]
    after = np.where(w[trough + 1:] > half_level)[0]
    width_ms = float("nan")
    if before.size and after.size:
        last_before = int(before[-1])
        first_after = trough + 1 + int(after[0])
        width_ms = 1000 * (first_after - last_before) / sampling_rate_hz
    return {
        "trough_to_peak_ms": 1000 * (peak - trough) / sampling_rate_hz,
        "negative_half_width_ms": width_ms,
        "normalized_positive_peak": float(w[peak]),
        "trough_sample_index": trough,
    }
