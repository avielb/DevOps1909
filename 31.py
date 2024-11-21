from typing import List, Dict, Tuple

# Function with type annotations
def greet(name):
    return f"Hello, {name}"
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_average(scores: List[float]) -> float:
    return sum(scores) / len(scores) if scores else 0.0

def get_person_info() -> Dict[str, str]:
    return {
        "name": "Alice",
        "age": "25",
        "height": "5.9"
    }

def get_coordinates() -> Tuple[float, float]:
    return (10.0, 20.0)

# Using the functions
name = "Bob"
name: str = "Bob"
print(greet(name))

scores: List[float] = [90.0, 85.5, 76.0]
average: float = calculate_average(scores)
print("Average Score:", average)

person_info: Dict[str, str] = get_person_info()
print("Person Info:", person_info)

coordinates: Tuple[float, float] = get_coordinates()
print("Coordinates:", coordinates)

