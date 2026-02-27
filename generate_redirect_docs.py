#!/usr/bin/env -S uv run --script

import string
import sys
from pathlib import Path

_TEMPLATE = string.Template(
    """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0; url=${real_dest}">
    <link rel="canonical" href="${real_dest}">
    <title>Redirecting to https://ormar-orm.github.io/ormar/</title>
</head>
<body>
    <h1>Redirecting https://ormar-orm.github.io/ormar/ 🌈</h1>

    <p>
        You're seeing this because you have an old link to ormar's docs.
        Update your bookmarks to the redirected URL!
    </p>
    <p>
        If you are not redirected automatically, follow the
        <a id="dest" href="${real_dest}">link</a>.
    </p>

    <script>
        let fragment = window.location.hash;
        let redirectUrl = `${real_dest}$${fragment}`;
        setTimeout(function() {
            window.location=redirectUrl
        }, 5000);
        document.getElementById("dest").setAttribute("href", redirectUrl);
    </script>
</html>
""".strip()
)


_PAGES = [
    "",  # web root (can't use / because of path joining)
    "install/",
    # Models
    "models/",
    "models/inheritance/",
    "models/methods/",
    "models/migrations/",
    "models/internals/",
    # Fields
    "fields/common-parameters/",
    "fields/field-types/",
    "fields/pydantic-fields/",
    "fields/encryption/",
    # Relations
    "relations/",
    "relations/foreign-key/",
    "relations/many-to-many/",
    "relations/postponed-annotations/",
    "relations/queryset-proxy/",
    # Queries
    "queries/",
    "queries/create/",
    "queries/read/",
    "queries/update/",
    "queries/delete/",
    "queries/joins-and-subqueries/",
    "queries/filter-and-sort/",
    "queries/select-columns/",
    "queries/pagination-and-rows-number/",
    "queries/aggregations/",
    "queries/raw-data/",
    # Other pages
    "signals/",
    "transactions/",
    "fastapi/",
    "fastapi/response/",
    "fastapi/requests/",
    "mypy/",
    "migration/",
    "plugin/",
    "contributing/",
    "releases/",
    "api/",
]

_OUT = Path(__file__).parent / "ormar"
assert _OUT.is_dir(), f"Output directory {_OUT} does not exist"

for page in _PAGES:
    dir_ = _OUT / page
    dir_.mkdir(exist_ok=True, parents=True)

    index = dir_ / "index.html"
    with index.open("w") as io:
        real_dest = f"https://ormar-orm.github.io/{page}"
        io.write(_TEMPLATE.substitute(real_dest=real_dest))

    print(f"[+] wrote {index}", file=sys.stderr)