# _setup.py - MATH1810 notebook startup (2026/27)
"""Startup code for every MATH1810 notebook.

The first cell of each notebook runs:

    from google.colab import drive
    drive.mount('/content/drive')
    %run "/content/drive/MyDrive/MATH1810/math1810/_setup.py"

This replaces the 2025/26 _setup.py. Student-visible behaviour is deliberately
unchanged, apart from these repairs:

  * one Drive mount and one course path (2025/26 mounted twice, and the
    notebooks disagreed about where the course folder was);
  * no pip install - nothing outside Colab's preinstalled packages is needed;
  * no 'imp' shim - it existed for IPython autoreload, which no notebook uses;
  * the exercise id is persistent. In 2025/26 it was regenerated on every run,
    so a Colab reconnect silently gave a student different questions;
  * set_trace comes from ipdb when available, otherwise the standard library,
    so no package has to be installed for Notebook 7;
  * if words.txt is installed beside valres.py, exercise a4 reads its word
    list from there instead of downloading it mid-exercise.
"""

import os
import sys

COURSE_DIRNAME = "math1810"
DRIVE_ROOT = os.environ.get("MATH1810_DRIVE_ROOT", "/content/drive/MyDrive")
MODULE_ROOT = os.path.join(DRIVE_ROOT, "MATH1810")
COURSE_DIR = os.path.join(MODULE_ROOT, COURSE_DIRNAME)
STATE_DIR = os.path.join(MODULE_ROOT, "state")
# Where 2025/26 installed the course; still honoured so a student who has not
# re-run onboarding is not left stranded.
LEGACY_COURSE_DIR = os.path.join(DRIVE_ROOT, "Colab Notebooks", "MATH1810", "math1810")

PSLEN = 100  # length of the parameter string valres builds from the id


def _mount_drive():
    """Mount Drive once, if we are in Colab and it is not already mounted."""
    try:
        from google.colab import drive  # noqa: F401
    except ImportError:
        return False  # not in Colab (local testing)
    mount_point = "/content/drive"
    if os.path.ismount(mount_point):
        try:
            os.listdir(os.path.join(mount_point, "MyDrive"))
            return True
        except OSError:
            drive.mount(mount_point, force_remount=True)
            return True
    drive.mount(mount_point)
    return True


def _find_course_dir():
    if os.path.isdir(COURSE_DIR):
        return COURSE_DIR
    if os.path.isdir(LEGACY_COURSE_DIR):
        print(
            "Note: using the old course folder in 'Colab Notebooks'.\n"
            "      Run the onboarding notebook again when convenient to move to\n"
            "      MyDrive/MATH1810/."
        )
        return LEGACY_COURSE_DIR
    raise SystemExit(
        "MATH1810 course folder not found in your Google Drive.\n"
        "Expected: MyDrive/MATH1810/math1810\n"
        "Run the onboarding notebook (Course_Setup) first, then re-run this cell."
    )


def _persistent_id(course_dir):
    """Return this student's 6-digit exercise id, creating it once if needed.

    The id fixes the parameters of exercises a1-a8. It lives outside the course
    folder so that reinstalling or updating the course does not change anyone's
    questions. If Drive will not let us write there, fall back to the course
    folder, and finally to a session-only id.
    """
    import random

    for path in (os.path.join(STATE_DIR, "id.txt"), os.path.join(course_dir, ".id.txt")):
        try:
            if os.path.exists(path):
                value = int(open(path).read().strip())
                if 100000 <= value <= 999999:
                    return value
        except (ValueError, OSError):
            pass  # unreadable or corrupt: fall through and make a new one

    value = random.randint(100000, 999999)
    for path in (os.path.join(STATE_DIR, "id.txt"), os.path.join(course_dir, ".id.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as fh:
                fh.write(str(value))
            return value
        except OSError:
            continue
    print(
        "Warning: could not save your exercise id to Drive, so your questions\n"
        "         may change if the runtime restarts. Tell your lecturer."
    )
    return value


def _install_wordlist_shim(course_dir):
    """Serve a4's word list from disk instead of downloading it.

    valres.a4 does `import requests` and fetches a fixed URL. When words.txt is
    installed beside valres.py we put a small stand-in in sys.modules that
    returns those bytes for that URL and delegates anything else to the real
    requests. Same bytes as the download, so the words themselves do not change.
    """
    words = os.path.join(course_dir, "words.txt")
    if not os.path.exists(words) or os.environ.get("MATH1810_NO_WORDS_SHIM"):
        return False
    import types

    try:
        import requests as _real
    except Exception:
        # Any failure here (not just ImportError) must not stop a student's
        # notebook from starting; a4 only needs the local word list.
        _real = None

    payload = open(words, "rb").read()

    class _Response:
        def __init__(self, content):
            self.content = content
            self.status_code = 200

    def get(url, *args, **kwargs):
        if "linuxwords" in url:
            return _Response(payload)
        if _real is not None:
            return _real.get(url, *args, **kwargs)
        raise RuntimeError("No network access available in this session.")

    shim = types.ModuleType("requests")
    shim.get = get
    shim.packages = types.SimpleNamespace(
        urllib3=types.SimpleNamespace(disable_warnings=lambda *a, **k: None)
    )
    if _real is not None:
        for name in ("post", "Session", "exceptions", "adapters"):
            if hasattr(_real, name):
                setattr(shim, name, getattr(_real, name))
    sys.modules["requests"] = shim
    return True


_mount_drive()
COURSE_DIR = _find_course_dir()

os.chdir(COURSE_DIR)
if COURSE_DIR not in sys.path:
    sys.path.insert(0, COURSE_DIR)

_install_wordlist_shim(COURSE_DIR)

# ---- the environment the notebooks expect -------------------------------
import matplotlib.pyplot as plt  # noqa: E402,F401
from IPython.core.interactiveshell import InteractiveShell  # noqa: E402

InteractiveShell.ast_node_interactivity = "all"

import valres as vr  # noqa: E402
vr.validate_live_config()  # fail clearly at startup if a switch was mistyped
import numpy as np  # noqa: E402
from scipy.integrate import odeint  # noqa: E402,F401
import pylab  # noqa: E402,F401

# Persistent id, then the parameter string valres derives from it.
vr.rid = _persistent_id(COURSE_DIR)
vr.getco(PSLEN)

from importlib import reload  # noqa: E402,F401

try:
    from ipdb import set_trace  # noqa: F401
except ImportError:  # Colab does not ship ipdb; the standard library is fine
    from pdb import set_trace  # noqa: F401

print("\nSetup complete :-)\n")
print("Your MATH1810 exercise id is {} (quote it if you ask for help).".format(vr.rid))
