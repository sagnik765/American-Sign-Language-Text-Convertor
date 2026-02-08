from pathlib import Path


def test_core_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "Main.ipynb").exists()
    assert (root / "create_data.ipynb").exists()
    assert (root / "app2.py").exists()
    assert (root / "camera.py").exists()
    assert (root / "model").exists()
