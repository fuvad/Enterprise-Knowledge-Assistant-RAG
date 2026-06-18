from app.query.rule_rewriter import RuleRewriter
from app.query.rewriter import QueryRewriter

class QueryPipeline:
    def __init__(self):
        self.rule_rewriter = RuleRewriter()
        self.llm_rewriter = QueryRewriter()

    def process(self, query: str) -> str:
        rule_written_query = self.rule_rewriter.rewrite(query)
        rewritten_query = self.llm_rewriter.rewrite(rule_written_query)

        return rewritten_query