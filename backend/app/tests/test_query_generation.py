from app.query.multi_query import MultiQueryGenerator

queries = MultiQueryGenerator().generate("What is Cooking?")

for q in queries:
    print(q)