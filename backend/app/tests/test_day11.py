from app.query.query_pipeline import QueryPipeline

pipeline = QueryPipeline()

queries = [
    "auth",

    "token expired",

    "login problem",

    "db performance issue",

    "k8s deployment failure",

    "infra"
]

for query in queries:
    rewritten = pipeline.process(query)

    print()
    print("=" * 80)

    print(f"Original : {query}")
    print(f"Rewritten: {rewritten}")