# FirmwareScout

A command-line tool designed to dissect and analyze device firmware binaries to identify file structures and embedded secrets.

## Minimum Viable Product (v1.0)
A CLI script that can:
1. Ingest a raw `.bin` file.
2. Read and print the first 16 bytes in hexadecimal format (to verify file I/O).
3. Calculate the Shannon entropy of those bytes.

## Tech Stack
* Language: C++ / Python
* Environment: Linux (WSL)