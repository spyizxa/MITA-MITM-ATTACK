# MITA-MITM-ATTACK
mita is a tool written in Python that can make arp poison.

# Mita

Mita is a Python script for performing ARP spoofing (ARP poisoning) attacks and conducting Man-in-the-Middle (MitM) attacks on network traffic.

## Overview

Mita is a Python script designed to execute ARP spoofing attacks by sending false ARP messages over a network. This tool can be used to intercept, modify, or redirect network traffic between two devices. It includes functionality for resetting ARP tables to their original state.

## Features

- Performing ARP poisoning attacks.
- Redirecting network traffic between a target and gateway.
- Resetting ARP tables to their original state.
- Providing clear feedback on packet transmission status.

## Platforms

This script is designed to run on Unix-based systems:
- Linux
- macOS
- Termux

**Operation on Windows systems is not guaranteed.**

## Setup

To use Mita, you need Python 3 and the `scapy`, `optparse`, `sys`, `time`, and `colorama` modules. You can install the required modules with pip

## Usage

To use Mita, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/mita.git
    ```

2. Navigate into the cloned directory:

    ```bash
    cd mita
    ```

3. Run the script using the following command:

    ```bash
    python3 run.py
    
    python3 mita.py -t <target_ip> -g <gateway_ip>
    ```

**Explanation:**

- `-t, --target` : Target IP address
- `-g, --gateway` : Gateway IP address

  **Note:** For intercepting HTTPS traffic, consider using [SSLstrip](https://www.owasp.org/index.php/Category:OWASP_SSLStrip). SSLstrip can downgrade HTTPS connections to HTTP, which allows capturing sensitive data that would otherwise be encrypted.

https://github.com/singe/dns2proxy



**Example:**

```bash
python mita.py -t 192.168.1.5 -g 192.168.1.1## Usage

To use Mita, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/mita.git
    ```

2. Navigate into the cloned directory:

    ```bash
    cd mita
    ```

3. Run the script using the following command:

    ```bash
    python mita.py -t <target_ip> -g <gateway_ip>
    ```

**Explanation:**

- `-t, --target` : Target IP address
- `-g, --gateway` : Gateway IP address

**Example:**

```bash
python mita.py -t 192.168.1.5 -g 192.168.1.1
