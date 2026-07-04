from typing import Protocol
# variables
name: str = "Alice"
count: int = 30
ratio: float = 0.75
active: bool = True

# Functions 
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"

def process(items: list[str]) -> None:
    for item in items:
        print(f"Processing item: {item}")

def find(id: int) -> int | None:
    if id > 0:
        return id
    return None

def config() -> dict[str, int]:
    return {"host": 80, "port": 8080}

class TestReader(Protocol):
    def read(self) -> str:
        ...

class FileReader:
    def read(self) -> str:
        return "Reading from a file."

class ApiReader:
    def read(self) -> str:
        return "Reading from an API."

class CacheReader:
    def read(self) -> str:
        return "Reading from cache."

def summarise(reader: TestReader) -> str:
    return reader.read()

print(summarise(FileReader()))
print(summarise(ApiReader()))
print(summarise(CacheReader()))

summarise(43)