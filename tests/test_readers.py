import tempfile
from pathlib import Path
from zero_threat_check.readers.android_face_cache import scan as scan_android
from zero_threat_check.readers.ios_photo_cache import scan as scan_ios_photo
from zero_threat_check.readers.ios_mdm import scan as scan_ios_mdm

def test_android_gap():
    with tempfile.TemporaryDirectory() as d:
        r = scan_android(Path(d))
        assert r["reader"] == "android-face-cache"
        assert any("not present" in g for g in r["gaps"])

def test_ios_photo_gap():
    with tempfile.TemporaryDirectory() as d:
        r = scan_ios_photo(Path(d))
        assert any("not found" in g for g in r["gaps"])

def test_ios_mdm_gap():
    with tempfile.TemporaryDirectory() as d:
        r = scan_ios_mdm(Path(d))
        assert any("no .mobileconfig" in g for g in r["gaps"])
