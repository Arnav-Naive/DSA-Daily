<https://colab.research.google.com/drive/19flsEfygzFnpW9vocq_-XLBwyBtwEdyQ>
|
--> for practice questions



# JSON in Python - Exercises

## Problem 1

Create `library.json` with the following content, then read it into Python and print each book's title, availability, and rating.

```json
[
  {"title": "To Kill a Mockingbird", "available": true, "rating": 9.1},
  {"title": "The Great Gatsby", "available": false, "rating": null},
  {"title": "1984", "available": true, "rating": 9.4}
]
```

**Sample output**

```
To Kill a Mockingbird is available and has a 9.1 rating
The Great Gatsby is not available and has a None rating
1984 is available and has a 9.4 rating
```

import json

# TODO

## Problem 2

Load `library.json` and add a new book to the list. Write the updated list back to `library.json`, then open the file to confirm it was written correctly.

import json

# TODO

## Problem 3

Overwrite `library.json` with the following content:

```json
[
  {"title": "To Kill a Mockingbird", "genres": ["fiction", "historical fiction"]},
  {"title": "The Great Gatsby", "genres": ["fiction", "classic"]},
  {"title": "1984"},
  {"title": "Pride and Prejudice", "genres": ["romance", "classic"]}
]
```

> You can overwrite `library.json` by writing this JSON string to it in Python, or by replacing its contents manually in your text editor.

Then load `library.json` and print each book's title and genres. If a book doesn't have a `genres` field, print `"No genres listed"` instead.

**Sample output**

```
To Kill a Mockingbird: fiction, historical fiction
The Great Gatsby: fiction, classic
1984: No genres listed
Pride and Prejudice: romance, classic
```

import json

# Step 1: Write the JSON content to library.json

# TODO

import json

# Step 2: Load library.json and print each book's genres

# TODO
