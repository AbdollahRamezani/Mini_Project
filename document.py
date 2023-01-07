from media import Media
class Document(Media):
    def __init__(self, document_type) :
        super().__init__()
        self.document_type=document_type
