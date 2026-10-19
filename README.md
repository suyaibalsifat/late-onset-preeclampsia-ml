# Late-onset preeclampsia prediction: leakage-controlled machine learning and explainable AI

Code, result tables and figures for the manuscript submitted to the Journal of Medical Systems:
*Leakage-controlled machine learning and explainable artificial intelligence for prediction of late-onset preeclampsia from antenatal laboratory and clinical data* (Suyaib Al Sifat).

## Data

The analysis uses the S1 Data spreadsheet published with Jhee et al., PLoS ONE 2019 (https://doi.org/10.1371/journal.pone.0221202). The data are not redistributed here. Download the file from the article page and set `DATA_PATH` in the first code cell of the notebook (sheet name: `Data`).

The column `number` in that file is a row counter, not a woman identifier. The notebook reconstructs women from consecutive visit rows (see section 3 of the notebook and `diagnose_grouping.py`).

## Contents

| File or folder | Purpose |
|---|---|
| `preeclampsia_jms_complete_pipeline.ipynb` | Complete analysis, with the outputs of the run reported in the paper |
| `diagnose_grouping.py` | Diagnostic that identifies which columns stay constant within a woman |
| `get_environment.py` | Writes `environment.txt` with exact library versions |
| `requirements.txt` | Python packages |
| `results/` | Result tables, test and out-of-fold predictions, figures |
| `figures/` | Script for the workflow figure (Fig. 1) |

## How to run

1. Install the packages: `pip install -r requirements.txt`
2. Download the S1 Data file and set `DATA_PATH` in the notebook.
3. Run all cells. Set `SYNTHETIC = True` for a quick smoke test without the real data.
4. Repeated random splits (cell 13) are slow and are off by default (`N_SPLITS_REPEAT = 0`).

All random seeds are fixed (`SEED = 42`). LIME was run with seeds 0 to 9.

## Notes

- Preprocessing (imputation, feature selection, scaling) and tuning use the training partition only. The test partition is used once.
- DiCE counterfactuals were not part of the reported results.
- Results come from one split of one cohort and are not validated externally. This is research code, not a clinical tool.

## Citation

Please cite the paper once published. A Zenodo DOI can be added here after the first release.

## License

MIT, see `LICENSE`.
