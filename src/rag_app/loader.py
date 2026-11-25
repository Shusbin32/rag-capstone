import logging
from pathlib import Path
from rag_app.exceptions import DocumentLoadError, EmptyDocumentError
from rag_app.models import Document, DocumentType

logger = logging.getLogger(__name__)

class TextFileLoader:
    SUPPORTED: dict[str, DocumentType] = {
        ".txt": DocumentType.TEXT,
        ".md": DocumentType.MARKDOWN,
    }

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir

    def load_file(self, path: Path) -> Document:
        """Load one file, or raise a DocumentLoadError."""
        doc_type = self.SUPPORTED.get(path.suffix.lower())
        if doc_type is None:
            raise DocumentLoadError(f"Unsupported file type: {path.suffix}")

        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise DocumentLoadError(f"Cannot read file: {path}") from exc

        if not text.strip():
            raise EmptyDocumentError(f"Empty document: {path}")

        return Document(source=path.name, text=text, doc_type=doc_type)

    def load_all(self) -> list[Document]:
        """Load every supported file in the data folder."""
        if not self.data_dir.is_dir():
            raise DocumentLoadError(f"Data folder not found: {self.data_dir}")

        documents: list[Document] = []
        for path in sorted(self.data_dir.iterdir()):
            if path.suffix.lower() not in self.SUPPORTED:
                continue

            try:
                documents.append(self.load_file(path))
            except EmptyDocumentError:
                logger.warning(
                    "Skipping empty file",
                    extra={"context": {"file": path.name}},
                )

        logger.info(
            "Documents loaded",
            extra={"context": {"count": len(documents)}},
        )
        return documents

