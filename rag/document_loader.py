from pathlib import Path


def split_markdown(text: str, source: str, min_length: int = 8) -> list[dict]:
    chunks = []
    heading = ""
    paragraph_lines = []

    def add_paragraph() -> None:
        paragraph = "\n".join(paragraph_lines).strip()
        paragraph_lines.clear()

        if len(paragraph) < min_length:
            return

        chunks.append(
            {
                "text": paragraph,
                "source": source,
                "heading": heading,
            }
        )

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if line.startswith("#"):
            add_paragraph()
            heading = line.lstrip("#").strip()
        elif not line:
            add_paragraph()
        else:
            paragraph_lines.append(line)

    add_paragraph()
    return chunks


def load_markdown_chunks(
    project_root: Path, source_files: list[str], min_length: int = 8
) -> list[dict]:
    chunks = []

    for source in source_files:
        path = project_root / source
        if not path.exists():
            raise FileNotFoundError(f"找不到设定文件：{path}")

        text = path.read_text(encoding="utf-8")
        chunks.extend(split_markdown(text, source, min_length=min_length))

    return chunks
