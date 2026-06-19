from app.metadata.metadata_rules import DEPARTMENT_RULES
import re

class MetadataExtractor:
    def extract_department(self, text: str) -> str:
        text = text.lower()
        
        scores = {}

        for department, keywords in (DEPARTMENT_RULES.items()):
            score = 0
            for keyword in keywords:
                if re.search(rf"\b{re.escape(keyword)}\b", text):
                    score += 1
            scores[department] = score
            
        best_department = max(scores, key=scores.get)
        
        if scores[best_department] == 0:
            return "Unknown"
        
        return best_department

    def extract_tags(self, text: str):
        text = text.lower()
        tags = []
        for keywords in (DEPARTMENT_RULES.values()):
            for keyword in keywords:
                if re.search(rf"\b{re.escape(keyword)}\b", text):
                    tags.append(keyword)
        return list(set(tags))