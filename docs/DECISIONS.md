# Research decision log

## 2026-11-10 — Initial architecture
- Google Colab for notebooks and first training; use independent cloud GPU only when justified.
- GitHub tracks software and configuration; Google Drive stores large artifacts.
- No recordings, credentials or unreviewed pretrained weights in Git.
- Compare waveform-only against firing/burst and multiscale temporal feature blocks.
- One-class pilot is a similarity/outlier task, not definitive NA-vs-DA classification.
- Independent molecular or optotagged identity, not firing patterns, should provide training labels.
- Dataset license and hardware provenance must be checked before mixing sources.
- CI and quickcheck use **synthetic test data**, never claimed biological results.
