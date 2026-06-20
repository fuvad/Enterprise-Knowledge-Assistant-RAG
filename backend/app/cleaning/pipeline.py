from app.cleaning.text_cleaner import TextCleaner

class CleaningPipeline:
    def process(self, document):
        cleaner = TextCleaner()
        
        document.text = cleaner.clean(document.text)

        return document