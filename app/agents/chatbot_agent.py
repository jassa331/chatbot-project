from app.services.llm_service import ask_llm
from app.tools.database_tool import run_query

def chatbot_agent(state):

    question = state["question"]

    prompt = f"""
You are a SQL Server expert.

Database tables:

Table: Products
Columns:
Id
Name
Description
Price
Category
IsActive
CreatedDate
UpdatedDate

Table: ProductVariants
Columns:
Id
ProductId
Weight
OriginalPrice
SellPrice
IsActive
CreatedAt

Relationship:
ProductVariants.ProductId = Products.Id

Rules:
- Return only SQL query
- Do not use ```
- SQL Server syntax only

Question:
{question}
"""

    sql_query = ask_llm(prompt)

    print("Generated SQL:", sql_query)

    result = run_query(sql_query)

    return {
        "answer": str(result)
    }