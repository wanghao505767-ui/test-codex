from pathlib import Path


def main() -> None:
    content = input("请输入一句话：")
    Path("notes.txt").write_text(content + "\n", encoding="utf-8")
    print("保存成功")


if __name__ == "__main__":
    main()
