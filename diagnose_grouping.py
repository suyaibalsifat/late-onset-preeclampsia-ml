"""Diagnostic: which columns identify a woman, and how many women does the file really contain?

Run in the notebook (or as a script). Paste the printed output back so the grouping rule can be fixed.
Set DATA_PATH. Nothing here trains a model.
"""
import numpy as np, pandas as pd

DATA_PATH = "preeclampsia.xlsx"
SYNTHETIC = False

df = pd.read_excel(DATA_PATH, sheet_name='Data', header=0, skiprows=[1]) if not SYNTHETIC else SYNTHETIC_DF
df.columns = df.columns.astype(str).str.strip()
if '(rev) dur_week' in df.columns and 'dur_week' in df.columns:
    df = df.drop(columns=['dur_week']).rename(columns={'(rev) dur_week': 'dur_week'})
df = df.loc[:, ~df.columns.str.contains('^Unnamed', regex=True)]
df = df.sort_values('number').reset_index(drop=True)
num = df.apply(pd.to_numeric, errors='coerce')

print("=== 1. First 30 rows, key columns ===")
show = [c for c in ['number', 'dur_week', 'PREG_WK', 'TGT', 'CHK', 'T3_1_1', 'T3_1_2', 'T3_1_3', 'T3_3_1', 'T3_4_2', 'T3_5_8',
                    'Height', 'Weight_pregnancy', 'Weight_at_visit', 'Hypertension_history', 'SBP', 'DBP', 'AL', 'PLT'] if c in df.columns]
print(df[show].head(30).to_string())

prev = num.shift(1)
ga_up = (num['PREG_WK'] > prev['PREG_WK']).to_numpy()
same_del = np.isclose(num['dur_week'], prev['dur_week'], equal_nan=True)
same_tgt = np.isclose(num['TGT'], prev['TGT'], equal_nan=True)
cand = ga_up & same_del & same_tgt                       # candidate "same woman" pairs
other = ~same_del                                        # pairs that are certainly different women
cand[0] = False; other[0] = False
print(f"\n=== 2. Consecutive-row pairs: candidate same-woman {int(cand.sum())}, delivery week differs {int(other.sum())}, rest {len(df)-int(cand.sum())-int(other.sum())-1}")

eq = {}
for c in num.columns:
    if c in ('number', 'PREG_WK', 'dur_week', 'TGT'): continue
    e = np.isclose(num[c], prev[c], equal_nan=True)
    eq[c] = (e[cand].mean(), e[other].mean())
eqdf = pd.DataFrame(eq, index=['equal_in_candidate_pairs', 'equal_in_different_woman_pairs']).T.sort_values('equal_in_candidate_pairs', ascending=False)
print("\n=== 3. Columns by how often they stay identical between consecutive rows of a candidate pair (top 40) ===")
print(eqdf.head(40).round(3).to_string())
print("\nColumns that vary almost every row inside a pair (bottom 15):")
print(eqdf.tail(15).round(3).to_string())

# data-driven identifiers: constant inside candidate pairs but usually different between different women
ids = eqdf[(eqdf['equal_in_candidate_pairs'] >= 0.97) & (eqdf['equal_in_different_woman_pairs'] <= 0.60)].index.tolist()
print("\n=== 4. Data-driven identifier columns (>=97% equal in pairs, <=60% equal across women):", ids)

def count(rule_cols, label):
    same = np.ones(len(df), bool)
    for c in rule_cols:
        same &= np.isclose(num[c], prev[c], equal_nan=True)
    new = ~(same & cand)
    new[0] = True
    pid = np.cumsum(new)
    n = pid.max(); sizes = pd.Series(pid).value_counts()
    print(f"[{label}] women={n}  visits/woman={len(df)/n:.2f}  share single-visit={(sizes==1).mean():.1%}  max visits={sizes.max()}")
    return pid

print("\n=== 5. Women under different rules (Jhee et al.: 11,006 women) ===")
count([], "D: delivery week + outcome + rising visit week")
if ids: pid = count(ids, "E: D + data-driven identifier columns")
hist = ['T3_3_1', 'T3_5_1', 'T3_5_8', 'T3_1_1']
hist = [c for c in hist if c in num.columns]
count(hist, "F: D + hypertension history, family history, prior PE, height (raw codes)")
print("\nPaste everything above back.")
