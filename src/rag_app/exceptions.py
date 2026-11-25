class RagAppError(Exception):
 """Base class for all errors raised by this application."""
class ConfigurationError(RagAppError):
 """Raised when the application settings are invalid."""
class DocumentLoadError(RagAppError):
 """Raised when a document cannot be loaded."""
class EmptyDocumentError(DocumentLoadError):
 """Raised when a document file contains no text."""
 