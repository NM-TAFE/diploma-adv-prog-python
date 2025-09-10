Build a **document management system**. It must support:

1. Multiple user types (Admin, Editor, Viewer)
2. Notifications when a document is uploaded
3. Logging of all user actions
4. Reading of large log files efficiently
5. Asynchronous retrieval of document metadata from the web

---

## Problem Solve

In your group **analyse the requirements**. For each, decide which pattern or technique is appropriate:

| Feature                                         | What pattern or technique is appropriate? |
| ----------------------------------------------- | ----------------------------------------- |
| 1. Create users based on their role             |                                           |
| 2. Trigger actions on document upload           |                                           |
| 3. Log when users do something                  |                                           |
| 4. Process large logs line-by-line              |                                           |
| 5. Fetch data from an external API concurrently |                                           |

---

### Step 1: User Creation

- Create a base class `User` and subclasses `Admin`, `Editor`, `Viewer`
- Write a `create_user(type, name)` function

---

### Step 2: Document Notification

- Build a `UploadNotifier` class that lets you subscribe multiple functions
- When a document is uploaded, all subscribers should be notified

---

### Step 3: Action Logging

- Use an `@action_logger` wrapper to log who did what
- It should log to the console (or use `logging` library)

---

### Step 4: Read Logs

- Use `yield` to return one line at a time from a large file
- Create a `read_logs(filepath)` function to simulate memory-efficient log reading

---

### Step 5: Fetch Metadata

- Use `aiohttp` and `asyncio` to retrieve mock document metadata (here is a code snippet to help to get going):

  ```python
  import aiohttp

  async def fetch_metadata(doc_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://jsonplaceholder.typicode.com/posts/{doc_id}"
        async with session.get(url) as resp:
            data = await resp.json()
  ```

- Fetch 3 metadata objects concurrently

---
