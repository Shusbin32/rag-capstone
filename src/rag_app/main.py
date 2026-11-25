import logging

from rag_app.config import load_settings
from rag_app.exceptions import RagAppError
from rag_app.loader import TextFileLoader
from rag_app.logging_config import setup_logging


logger = logging.getLogger(__name__)

def main() -> int:
    setup_logging()
    try:
        settings = load_settings()
        setup_logging(settings.log_level.value)
    
        logger.info(
            "Application starting",
            extra={
                "context": {
                    "app": settings.app_name,
                    "chunk_size": settings.chunk_size,
                }
            },
        )
    
        documents = TextFileLoader(settings.data_dir).load_all()
    
    except RagAppError:
        logger.exception("Application failed")
        return 1
    
    for doc in documents:
        logger.info(
            "Document ready",
            extra={
                "context": {
                    "source": doc.source,
                    "words": doc.word_count,
                }
            },
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())