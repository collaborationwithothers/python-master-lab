class PDF:
    kind = "PDF"

class HTML:
    kind = "HTML"
REG = {
    "pdf": PDF,
    "html": HTML,}
def make_report(kind: str):
    return REG[kind.lower()]()

print(type(make_report("pdf")).__name__)  # Output: PDF
print(type(make_report("html")).__name__)  # Output: HTML