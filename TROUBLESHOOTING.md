# MATH1810: getting started and common fixes

You do **not** need a GitHub account or to download a ZIP file. Your notebooks
will live in your own Google Drive. Most problems are fixed by checking which
Google account is open, finding the Drive copy, or running the notebook's first
setup cell.

## Start here

1. Open [Course Setup in Google Colab](https://colab.research.google.com/github/notulae/math1810/blob/main/onboard.ipynb).
2. Check that Colab is signed in to the Google account where you want your
   coursework saved. Run **both** cells in the setup notebook, in order. You
   can click each cell and press **Shift-Enter**, or choose **Runtime → Run all**.
3. Colab will ask to connect to Google Drive. Read the prompts, select that
   same account, and allow the Drive access needed to save your notebooks.
   Wait until you see **“MATH1810 is installed”** and a link to your folder.
4. Open **Welcome.ipynb** from that folder. Your course notebooks are in
   **My Drive → MATH1810 → math1810**. Start with Welcome, then Notebook1.

**Work in the copies in your Drive.** Notebooks opened from GitHub are course
originals, not the copies where your work is saved.

## I cannot get through setup or Drive permissions

- **Do I need to register on GitHub?** No. You only need a Google account that
  can use Colab and Drive.
- **Colab or Drive is showing the wrong account.** Check the account picture at
  the top right of Colab and Drive. Select the account you want to use, then
  reopen Course Setup. If several accounts are signed in, a private browser
  window signed in to just the intended account can make the choice clearer.
- **I dismissed or denied a permission prompt.** Rerun the setup cell that
  connects Drive and complete the prompts. Check which account each prompt
  names. You need to allow Colab to access Drive for the course to install.
- **The browser blocked a sign-in window.** Allow the Colab/Google sign-in
  window in your browser and retry. If your school account says an administrator
  has blocked access, contact your school's IT support or the lecturer; repeated
  clicks will not change an administrator setting.
- **The download failed or stopped.** Check your connection and run Course
  Setup again. It verifies the download before replacing course files. If you
  already had a working copy, a failed download leaves it in place.

## I cannot find my notebooks

Look in **Google Drive → My Drive → MATH1810 → math1810**. You should see
`Welcome.ipynb` and `Notebook1.ipynb` through `Notebook9.ipynb`. Make sure
Drive is showing the same Google account you used for Course Setup. You can
also open Colab, choose **File → Open notebook → Google Drive**, and navigate
to that folder. If the folder is absent, reopen Course Setup and run both cells.

If Drive does not offer to open an `.ipynb` file in Colab, right-click the file
and choose **Open with → Google Colaboratory**.

## A notebook says `vr` is undefined, or a cell does not work

At the start of **every new Colab session**, run the first code cell near the
top of that notebook. It connects Drive and loads the course setup. Wait for
**“Setup complete :-)”** and your six-digit exercise ID before working lower
down. Run earlier code cells in order where later cells depend on them. Use
**Shift-Enter** to run a selected cell.

If you restarted or disconnected the runtime, run the notebook's setup cell
again. Your saved notebook and exercise ID are still in Drive.

## How do the in-class CA exercises work?

Read the task above the CA cells and run the cells in the order shown. Some
exercises have one cell, such as `vr.a1()`, which asks for an answer. Others
have a **question cell** such as `vr.a3(True)` and a later **answer cell** such
as `vr.a3(False)`. Run the question cell, work out and test your solution, then
run the answer cell when you are ready. Follow the exact cells in *your*
notebook; your question may differ from another student's.

An incorrect attempt can reduce the mark for that CA, and there may be a short
wait before another attempt. Take your time rather than guessing. If a cell
says **“This CA test is not currently live,”** it is not available now; wait
for your lecturer's instructions. Reinstalling the course will not turn it on.
If it says the live configuration is unavailable, check your connection and
try again shortly. Tell your lecturer if the message continues.

## Which code goes into Brightspace?

After a correct answer, look for **“Enter this code into Brightspace:”**.
Copy the **whole receipt exactly as displayed**, including the `#` at each
end, into the Brightspace entry for **that same CA**. Do not copy the words
around it, quotation marks, a neighbour's code, or your six-digit exercise ID.
Check that no character was missed when pasting. Your receipt may look
different from examples in the notebook; use the one produced for you.

If you have a correct answer but cannot find a receipt, scroll through the
output directly below the answer cell. Run the notebook's setup cell if you
have started a new runtime, then return to the CA cell. If Brightspace rejects
a receipt, check the CA entry and paste the full code again. If it still fails,
contact the lecturer through Brightspace with the CA number and your exercise
ID. Do not post your receipt publicly.

## Will running Course Setup again erase my work?

No. An update keeps the previous `math1810` folder as a numbered backup and
puts a fresh course copy beside it. Any notebook you changed is also copied
into the new folder with a name such as
`Notebook3 (your earlier version).ipynb`. Your exercise ID and recorded
attempts are carried forward. Open your earlier version if you need to copy
work into the fresh notebook. Do not delete backup folders until you have
checked your work.

## Still stuck?

Send the lecturer a Brightspace message saying which step or notebook failed,
what you expected, and the exact error message or a screenshot. Include your
six-digit exercise ID if the notebook printed it. **Do not send a password or
post a CA receipt publicly.**
