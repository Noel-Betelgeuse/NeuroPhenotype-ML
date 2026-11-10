# Google Colab guide (private repository)

1. In Colab choose **File → Open notebook → GitHub**; sign in/authorize GitHub to access private repositories and select `notebooks/00_environment_check.ipynb`.
2. Execute the notebook cells for CPU/GPU availability and mount Google Drive.
3. The actual Python package is **not installed** merely by opening the notebook. For the first phase inspect code in GitHub and execute tests via a local clone or a properly authenticated runtime clone.
4. Never put a GitHub access token directly in a notebook, notebook output, URL, or committed file. Use a scoped secret/credential helper if cloning a private repository in Colab.
5. Runtime storage is ephemeral. Data should be staged locally for intensive reads, then validated outputs transferred to Drive.
6. Do not claim Colab has a GPU until the notebook reports one. Hardware availability varies.
7. Cloud GPU providers must use the same tagged source commit, dataset manifest and experiment config.

Next integration milestone: create a safe private-repo clone/bootstrap and run logging helper, then validate it on a real Colab instance.
