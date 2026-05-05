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
Firmware contains specialised and highly compressed Linux file systems. Theoretically, this tool will find the offset, or exact memory address of the file system, determine the size, and unpack it. Unpacking the file system will give a more clear directory structure.

## Entropy Analysis
<h3>Shannon Entropy</h3>
Shannon entropy is a mathematical calculation that measures the randomness of data.
 * Low Entropy -> Very structured and predictable data
 * High Entropy -> Compressed or encrypted data
This tool uses entropy to map out the binary and highlight which parts are compressed or encrypted and which parts are readable.