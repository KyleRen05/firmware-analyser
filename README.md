# FirmwareScout

A command-line tool designed to dissect and analyze device firmware binaries to identify file structures and embedded secrets.

## Minimum Viable Product (v1.0)
A CLI script that can:
1. Ingest a raw `.bin` file.
2. Read and print the first 16 bytes in hexadecimal format (to verify file I/O).
3. Calculate the Shannon entropy of those bytes.

## Tech Stack
* Language: C++ / Python / Bash
* Environment: Linux (WSL)

<hr>

# Core Concepts

## Anatomy of Firmware
Firmware files are (or even blobs of firmware) are essentially mini Linux-based operating systems that are packed into a single binary file.

 * This tool examins binary and blocks of hexadecimal data in order to hunt for Magic Numbers (file signatures).
 * File Signatures (or Magic Numbers) are specific sequences of bytes that identify file types.

## Embedded File Systems and Extraction
Firmware contains specialised 