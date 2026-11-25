from rag_app.models import DocumentType

doc_type = DocumentType.MARKDOWN
print(doc_type.value)
print(doc_type == DocumentType.Ma)