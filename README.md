
API for calling strains on SARS-CoV-2 genomes

#### build/ activate local dev environment

```bash 
$ make dev 
$ conda activate pangolin
$ poetry install 
$ poetry run python3 src/main.py
```

#### run test

```bash
$ make test
{
  "taxon": "BS000685.1",
  "lineage": "B.1.1",
  "conflict": "",
  "ambiguity_score": "",
  "scorpio_call": "",
  "scorpio_support": "",
  "scorpio_conflict": "",
  "version": "PANGO-v1.2.124",
  "pangolin_version": "3.1.20",
  "pangoLEARN_version": "2022-02-02",
  "pango_version": "v1.2.124",
  "status": "passed_qc",
  "note": "Assigned from designation hash."
}
```