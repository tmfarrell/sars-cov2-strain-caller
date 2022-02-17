import pandas as pd
import subprocess
import tempfile

def call_pangolin(fasta: str) -> dict:
    with tempfile.NamedTemporaryFile() as f:
        subprocess.call(["pangolin", fasta, "--outfile", f.name])
        return pd.read_csv(f.name).fillna('').iloc[0].to_dict()