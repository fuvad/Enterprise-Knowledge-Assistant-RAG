from app.metadata.metadata_extractor import (
    MetadataExtractor
)

from app.schemas.metadata import Metadata


class MetadataPipeline:
    def process(self,document):
        extractor = MetadataExtractor()
        
        department = (extractor.extract_department(document.text))
        tags = (extractor.extract_tags(document.text))
        document.metadata = Metadata(department=department, tags=tags)

        return document