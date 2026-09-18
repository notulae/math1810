# MATH1810 — Introduction to Scientific Python

Nine notebooks, a welcome guide, and the data files that go with them. Everything
runs in Google Colab. You need a Google account and nothing else.

---

## First time — three steps

### Step 1. Open the setup notebook

[**Open Course Setup in Colab**](https://colab.research.google.com/github/notulae/math1810/blob/main/onboard.ipynb)

Nothing to download, and no GitHub account needed. The link opens the setup
notebook directly in Colab.

**Having trouble?** See the [MATH1810 getting-started and troubleshooting guide](TROUBLESHOOTING.md).

### Step 2. Run it

Click the first cell, then press **Shift-Enter** to run each cell in turn — or
use **Runtime → Run all**.

Google will ask permission to connect your Drive. Accept it: this is how the
notebooks get saved somewhere permanent. The setup then copies the course into

    My Drive / MATH1810 / math1810

### Step 3. Open the Welcome notebook

When setup finishes it prints a link straight to your new folder. From there,
open **`Welcome.ipynb`**.

If you would rather navigate yourself, either route works:

* In Drive: **My Drive → MATH1810 → math1810**, then double-click `Welcome.ipynb`.
  The first time, right-click it and choose **Open with → Google Colaboratory**.
* In Colab: **File → Open notebook → Google Drive**, then pick
  `MATH1810/math1810/Welcome.ipynb`.

Work through `Welcome.ipynb` first, then `Notebook1.ipynb`, and so on.

---

## Afterwards

**Always open your notebooks from your Drive**, not from this page. The copies
here are the pristine originals — anything you type into them is thrown away
when you close the tab. The copies in your Drive are yours, and Colab saves them
as you work.

Every notebook starts with a short setup cell. Run it first, each time you open
a notebook; it prints `Setup complete :-)` and your exercise id.

---

## Getting updated material

When updated material is announced, open the setup notebook again (Step 1) and
run it. You can do this as often as you like.

**Your own work is never overwritten or deleted.** Here is exactly what happens:

1. Your current `math1810` folder is renamed to `math1810_backup_001` — then
   `_backup_002` the next time, and so on. Nothing in it is touched.
2. A fresh `math1810` folder is installed next to it.
3. **Any file you had changed is copied into the new folder beside the fresh
   one**, named like `Notebook3 (your earlier version).ipynb`. You do not have to
   go looking in the backup for your work — it is right there.
4. Your exercise id and your attempt history are carried across automatically,
   so your questions stay the same and earlier attempts still count.

So after an update your folder holds the new `Notebook3.ipynb` and, if you had
worked in it, your `Notebook3 (your earlier version).ipynb` next to it. Open
yours, copy across anything you want to keep, and delete the copy when you are
finished with it. The complete previous folder is still in the numbered backup
as well, so nothing can be lost.

---

## What is here

| | |
|---|---|
| `onboard.ipynb` | setup, and updates |
| `math1810/` | the notebooks, data files and course code |
| `release.json` | points at the current release |

Each release is a fixed, published archive with a checksum. The setup notebook
verifies the download before it touches anything in your Drive, so an
interrupted or corrupted update cannot damage a working installation.

---

## If something goes wrong

Run the setup notebook again. It repairs the course files without touching your
work, and tells you what it changed.

If a notebook still will not start, contact your lecturer through Brightspace and
quote the exercise id printed when a notebook starts.
