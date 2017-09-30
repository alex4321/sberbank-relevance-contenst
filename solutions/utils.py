from ipywidgets import IntProgress
from IPython.display import display


def log_progress(sequence, every=10):
    progress = IntProgress(min=0, max=len(sequence), value=0)
    display(progress)
    for index, record in enumerate(sequence):
        if index % every == 0:
            progress.value = index
        yield record
