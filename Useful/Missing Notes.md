
```dataview
TABLE WITHOUT ID out AS "Missing Note", file.link AS "Mentioned In"
FLATTEN file.outlinks as out
WHERE !(out.file) AND !contains(meta(out).path, "/")
```



