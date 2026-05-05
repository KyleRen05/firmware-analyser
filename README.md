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

<hr/>

# Core Concepts

## 1. Anatomy of Firmware
Firmware files are (or even blobs of firmware) are essentially mini Linux-based operating systems that are packed into a single binary file.<br/>
* This tool examins binary and blocks of hexadecimal data in order to hunt for Magic Numbers (file signatures).
* File Signatures (or Magic Numbers) are specific sequences of bytes that identify file types.

## 2. Embedded File Systems and Extraction
Firmware contains specialised and highly compressed Linux file systems. Theoretically, this tool will find the offset, the exact memory address of the file system, determine the size, and unpack it. Unpacking the file system will give a more clear directory structure.

## 3. Entropy Analysis
<h3>Shannon Entropy</h3>
Shannon entropy is a mathematical calculation that measures the randomness of data.<br/>

* Low Entropy -> Very structured and predictable data
* High Entropy -> Compressed or encrypted data<br/>

This tool uses entropy to map out the binary and highlight which parts are compressed or encrypted and which parts are readable.

## 4. Static Analysis and String Extraction
Even in compiled C/C++ binaries, readable ASCII or Unicode text often survives the compilation process. The theory here relies on Pattern Matching (often using Regular Expressions). This tool will scan the raw binary structures for strings of text that match the patterns of private cryptographic keys, hardcoded admin passwords, developer comments, or exposed API tokens.

## 5. Architecture and Endianness
Hardware varies immensely in IoT. Different processors read binary differently (this concept is known as Endianness).<br/>
* "Big-Endian" processors read the most significant byte first
* "Little-Endian" processors read the least significant byte first<br/>

This tool will understand how the target hardware reads the data so that it does not read the memory structures backwards.
