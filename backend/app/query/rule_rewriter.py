class RuleRewriter:
    REPLACEMENTS = {
        "auth":
        "authentication",

        "db":
        "database",

        "pwd":
        "password",

        "k8s":
        "kubernetes",

        "infra":
        "infrastructure",

        "login":
        "authentication login",

        "token":
        "authentication token"
    }

    def rewrite(self, query):
        query = query.lower()
        
        for short, full in (self.REPLACEMENTS.items()):
            query = query.replace(short, full)

        return query