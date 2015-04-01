# Tanach to SQLite
An attempt to parse Tanach into a SQLite database

Pasukim Table was created with the following columns:

```SQL
CREATE TABLE pasukim
(Id INTEGER PRIMARY KEY, sefer_title TEXT, perek_letter TEXT, perek_index INTEGER, pasuk_letter TEXT, pasuk_index INTEGER, pasuk_text TEXT)
```

Each Pasuk is a row in the Pasukim table
