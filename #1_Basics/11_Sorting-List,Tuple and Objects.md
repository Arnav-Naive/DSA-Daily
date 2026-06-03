# Python Sorting Tutorial Notes

This tutorial covers the fundamentals of sorting various data types in Python, including lists, tuples, dictionaries, and custom objects.

## 1. Sorting Lists (0:00 - 3:14)
*   **`sorted()` function**: Returns a **new** sorted list, leaving the original list unchanged.
*   **`.sort()` method**: Sorts the list **in-place** and returns `None`.
*   **Descending Order**: Both methods accept the `reverse=True` parameter to sort from highest to lowest.

## 2. Sorting Other Iterables (3:15 - 5:13)
*   The `.sort()` method only works on lists. For other iterables like **tuples** or **dictionaries**, you must use the `sorted()` function.
*   When sorting a dictionary with `sorted()`, it sorts the **keys** by default.

## 3. Custom Sorting Criteria (5:14 - 11:45)
*   **`key` parameter**: Allows you to define custom logic for comparison. It applies a function to every element before sorting.
    *   **Built-in functions**: Example: `key=abs` for sorting numbers by their absolute value (6:25).
    *   **Custom functions**: Define a function that returns the attribute you want to sort by (e.g., sorting objects by name, age, or salary).
    *   **Lambda functions**: Use `lambda` for quick, anonymous sorting logic without defining a full function (9:55).
    *   **`operator.attrgetter`**: An efficient way to sort by specific object attributes (10:55).

## Summary Table of Key Methods
| Method/Function | Use Case | Behavior |
| :--- | :--- | :--- |
| `sorted(iterable)` | Any iterable (list, tuple, dict) | Returns new sorted list |
| `list.sort()` | Lists only | Modifies original list (in-place) |
| `key=...` | Customizing sort logic | Applied to each item during comparison |