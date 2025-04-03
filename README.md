# Linked List Implementation and Unit Testing

## Description
This project demonstrates the implementation of a **singly linked circular list** and a list based on built-in arrays/lists in Python. The project includes a full set of **unit tests** to ensure correctness and a configured **Continuous Integration (CI) pipeline** using GitHub Actions.

## Variant Calculation and Description
16 % 4 = 0

Variant 0:

The implementation follows the given variant specifications:
- **Initial implementation:** Singly linked circular list.
- **Second implementation:** List based on built-in arrays/lists.

## Features
The implemented list supports the following operations:
- `length() -> int` : Returns the number of elements.
- `append(element: Character) -> None` : Adds an element to the end.
- `insert(element: Character, index: int) -> None` : Inserts an element at a specified position.
- `delete(index: int) -> Character` : Removes and returns an element at a given position.
- `deleteAll(element: Character) -> None` : Removes all occurrences of an element.
- `get(index: int) -> Character` : Retrieves an element at a given index.
- `clone() -> List` : Creates a copy of the list.
- `reverse() -> None` : Reverses the list order.
- `findFirst(element: Character) -> int` : Finds the first occurrence of an element.
- `findLast(element: Character) -> int` : Finds the last occurrence of an element.
- `clear() -> None` : Clears the list.
- `extend(elements: List) -> None` : Merges another list into the current list.

## Setup and Running Tests
### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/meluni9/circular-linked-list.git
   cd circular-linked-list
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests
To run the unit tests:
```sh
pytest
```

### CI Configuration
- **GitHub Actions** is set up to run tests automatically on each push to the main branch.
- The repository includes a commit where tests failed to demonstrate CI catching errors.

## CI Failure Example
A test failure commit can be found [here](https://github.com/meluni9/circular-linked-list/commit/75151d62ad7da085a43ce32c4230e3c9d7d5f0ec).

## Conclusions
Unit testing proved to be extremely useful in catching errors early, ensuring code reliability, and making refactoring safer. Setting up CI added an extra layer of automation that guarantees code correctness after every change. While unit testing requires additional effort, it ultimately saves time by preventing future debugging issues.

