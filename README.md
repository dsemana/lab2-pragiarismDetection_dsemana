## Plagiarism Detector (Lab 2)

This project is a simple plagiarism detector written in Python. It compares two text essays and reports their similarity using **Jaccard similarity** on cleaned word sets. It also supports word search and saving a similarity report.

### Project Structure

- `plagiarism-detector.py` – main Python application.
- `setup.sh` – Bash script to create required folders and log the setup.
- `essays/` – directory where you place `essay1.txt` and `essay2.txt`.
- `reports/` – directory where similarity reports are saved.
- `setup.log` – log file created by `setup.sh`.

### Requirements

- Python 3.9+ recommended.
- Bash (for running `setup.sh`; on Windows you can use Git Bash, WSL, or another Unix-like shell).

### 1. Run the Setup Script

The setup script creates the `essays` and `reports` directories and logs actions in `setup.log`.

```bash
chmod +x setup.sh
./setup.sh
```

After this, you should see an `essays` folder and a `reports` folder in the project directory.

### 2. Add Test Essays

Place your test essay files in the `essays` directory with the exact names:

- `essays/essay1.txt`
- `essays/essay2.txt`

### 3. Run the Plagiarism Detector

From the project root directory:

```bash
python plagiarism-detector.py
```

The program will:

1. Read `essay1.txt` and `essay2.txt` from the `essays` folder.
2. Ask you for a word to search and show how many times it occurs in each essay.
3. Clean and process the essays (lowercase, remove punctuation, filter stop words).
4. Print common words between the two processed essays.
5. Compute and print the **plagiarism percentage** using Jaccard similarity.
6. Ask if you want to save the similarity report:
   - If you answer `y`, it writes a list of common (intersection) words to `reports/similarity_report.txt`.

### Jaccard Similarity Formula

The plagiarism percentage is calculated as:

\[
\text{Plagiarism \%} = \left( \frac{|\text{Intersection of word sets}|}{|\text{Union of word sets}|} \right) \times 100
\]

If the resulting percentage is **50% or more**, the program reports that similarity is likely; otherwise it reports that similarity is unlikely.


