import subprocess
import sys
from pathlib import Path


def test_main_saves_input_and_prints_success(tmp_path: Path) -> None:
    script_path = Path(__file__).resolve().parent / "main.py"

    result = subprocess.run(
        [sys.executable, str(script_path)],
        input="今天学习很顺利\n",
        text=True,
        capture_output=True,
        cwd=tmp_path,
        check=True,
    )

    assert "请输入一句话：" in result.stdout
    assert "保存成功" in result.stdout

    notes_path = tmp_path / "notes.txt"
    assert notes_path.exists()
    assert notes_path.read_text(encoding="utf-8") == "今天学习很顺利\n"
