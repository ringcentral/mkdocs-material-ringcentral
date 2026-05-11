# Code blocks

MkDocs Material's code block system is powered by `pymdownx.highlight` and `pymdownx.superfences`. Features like line numbers, line highlighting, and file titles are applied via attributes on the opening fence — no extra plugins or HTML required.

---

## Basic syntax

A fenced code block opens and closes with triple backticks. The language name on the opening fence enables syntax highlighting.

````markdown
```python
def greet(name: str) -> str:
    return f"Hello from RingCentral, {name}!"
```
````

```python
def greet(name: str) -> str:
    return f"Hello from RingCentral, {name}!"
```

Supported language identifiers include `python`, `javascript`, `typescript`, `bash`, `json`, `yaml`, `html`, `css`, `sql`, `go`, `java`, `csharp`, and [hundreds more](https://pygments.org/languages/).

---

## File title

Add a `title` attribute to label the block with a filename or path.

````markdown
```python title="connector.py"
class SalesforceConnector:
    def __init__(self, access_token: str):
        self.token = access_token
```
````

```python title="connector.py"
class SalesforceConnector:
    def __init__(self, access_token: str):
        self.token = access_token
```

---

## Line numbers

Add `linenums="1"` to enable line numbers. The number sets the starting value — use any integer to begin at a non-zero offset.

=== "Start at 1"

    ````markdown
    ```python linenums="1"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```
    ````

    ```python linenums="1"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```

=== "Start at 42"

    ````markdown
    ```python linenums="42"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```
    ````

    ```python linenums="42"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```

---

## Line highlighting

Use `hl_lines` to draw attention to specific lines. Works with or without line numbers.

=== "Individual lines"

    ````markdown
    ```python hl_lines="2 3"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```
    ````

    ```python hl_lines="2 3"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```

=== "Range"

    ````markdown
    ```python hl_lines="2-4"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```
    ````

    ```python hl_lines="2-4"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```

=== "Mixed"

    ````markdown
    ```python hl_lines="1 3-5"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```
    ````

    ```python hl_lines="1 3-5"
    def authenticate(token: str) -> bool:
        if not token:
            raise ValueError("Token required")
        return validate(token)
    ```

---

## Combining attributes

Title, line numbers, and highlighting can be combined freely.

````markdown
```python title="auth.py" linenums="1" hl_lines="3 4"
def authenticate(token: str) -> bool:
    """Validate an OAuth bearer token."""
    if not token:
        raise ValueError("Token required")
    return validate(token)
```
````

```python title="auth.py" linenums="1" hl_lines="3 4"
def authenticate(token: str) -> bool:
    """Validate an OAuth bearer token."""
    if not token:
        raise ValueError("Token required")
    return validate(token)
```

---

## Inline code

Wrap content in single backticks for inline code. To enable syntax highlighting on inline code, prefix the backtick with a `#!` shebang and language name — requires `pymdownx.inlinehilite`.

````markdown
Call `#!python print("hello")` from any Python context.

Set `#!yaml enabled: true` in your config.
````

Call `#!python print("hello")` from any Python context.

Set `#!yaml enabled: true` in your config.

---

## Code annotations

Annotations attach numbered call-outs to any line. Click the number in the rendered block to expand the note. Place a comment marker in the code (`# (1)!`) then add a matching ordered list immediately after the closing fence.

The `!` suffix strips the comment from the rendered output so readers see clean code.

````markdown
```python linenums="1"
import ringcentral # (1)!

sdk = ringcentral.SDK(
    client_id="YOUR_CLIENT_ID",       # (2)!
    client_secret="YOUR_CLIENT_SECRET",
    server="https://platform.ringcentral.com",
)

platform = sdk.platform()
platform.login(jwt="YOUR_JWT_TOKEN") # (3)!
```

1.  Import the official RingCentral Python SDK.
    Install it with `pip install ringcentral`.
2.  Never hard-code credentials in source files.
    Use environment variables or a secrets manager:
    ```python
    import os
    client_id = os.environ["RC_CLIENT_ID"]
    ```
3.  JWT auth is the recommended flow for server-to-server integrations.
    See the [Auth guide](../getting-started.md) for the full token lifecycle.
````

```python linenums="1"
import ringcentral # (1)!

sdk = ringcentral.SDK(
    client_id="YOUR_CLIENT_ID",       # (2)!
    client_secret="YOUR_CLIENT_SECRET",
    server="https://platform.ringcentral.com",
)

platform = sdk.platform()
platform.login(jwt="YOUR_JWT_TOKEN") # (3)!
```

1.  Import the official RingCentral Python SDK.
    Install it with `pip install ringcentral`.
2.  Never hard-code credentials in source files.
    Use environment variables or a secrets manager:
    ```python
    import os
    client_id = os.environ["RC_CLIENT_ID"]
    ```
3.  JWT auth is the recommended flow for server-to-server integrations.
    See the [Auth guide](../getting-started.md) for the full token lifecycle.

!!! note "Enabling annotations"
    Annotations require `content.code.annotate` in your `mkdocs.yml` feature list.
    Once enabled, every code block on every page supports them — no per-block attribute needed.

    ```yaml
    theme:
      features:
        - content.code.annotate
    ```

    Annotation content is full Markdown — inline code, bold, links, and nested fenced blocks all render inside the pop-up.

---

## Copy button

A copy-to-clipboard button appears on hover for every code block automatically when `content.code.copy` is enabled in `mkdocs.yml`:

```yaml
theme:
  features:
    - content.code.copy
```

To disable it on a specific block, add the `nocopy` class:

````markdown
```text class="nocopy"
This block has no copy button.
```
````

---

## Required extensions

All features on this page require the following in `mkdocs.yml`:

```yaml
markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.superfences
```

`anchor_linenums: true` makes each line number a permalink anchor — useful for linking colleagues directly to a specific line in a doc.
