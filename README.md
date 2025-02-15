# Phrase Generator

A Python-Based Tool For Generating Secure Mnemonic Seed Phrases. This Repository Allows Users To Create 12 Or 24-Word Mnemonic Phrases For Cryptographic Wallets Or Other Applications Requiring Random, Secure Seed Phrases

## Table Of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)

## Introduction

The Mnemonic Phrase Generator Is A Simple Python Script That Helps Users Generate Secure Seed Phrases. These Seed Phrases Can Be Used For Cryptocurrencies Or Other Applications That Require Secure, Random, And Reproducible Seed Phrases. This Tool Supports Generating Mnemonic Phrases With Either 12 Or 24 Words

**Mnemonic Phrases** Are Essential For Backing Up And Restoring Cryptographic Wallets, Making This Tool A Valuable Asset For Anyone Working With Blockchain Or Cryptographic Applications

## Features

- Generate 12 Or 24-Word Mnemonic Phrases
- Randomly Generated Phrases Based On Cryptographic Strength
- Option To Specify The Number Of Mnemonic Phrases To Generate
- Save Generated Phrases To A Text File
- Simple And Easy-To-Use Command-Line Interface

## Installation

To Use The Mnemonic Phrase Generator, You Need To Have Python Installed On Your System

### Step 1: Clone The Repository

Clone The Repository To Your Local Machine Using Git:

```bash
git clone https://github.com/theakorg/phrase-generator.git
```

### Step 2: Install Dependencies

Once You Have Cloned The Repository, Navigate To The Project Directory And Install The Required Dependencies Using pip:

```bash
pip install -r requirements.txt
```

This Will Install All The Dependencies Listed In The requirements.txt File, Including The mnemonic Library

## Usage

After Cloning The Repository And Installing The Dependencies, You Can Run The Script To Generate Mnemonic Phrases

## Step 1: Run The Script

Navigate To The Directory Where The Script Is Located, And Run The Script Using Python:

```bash
python generator.py
```

## Step 2: Input Parameters

You Will Be Prompted To Enter The Number Of Words For The Seed Phrase (12 Or 24) And The Number Of Mnemonic Phrases You Want To Generate.

## Example Interaction:

```bash
Please Enter The Number Of Words For The Seed Phrase (12 Or 24): 12
Please Enter The Number Of Mnemonic Phrases To Generate: 11
```

The Script Will Generate The Mnemonic Phrases And Save Them To A Text File In A Directory Named combo.

## How It Works

The Script Uses The Mnemonic Library To Generate Secure Mnemonic Phrases. It Takes The Following Steps:

1. User Input: The User Specifies The Number Of Words (12 Or 24) And The Number Of Phrases To Generate
2. Phrase Generation: Using The Mnemonic Library, The Script Generates The Seed Phrases Based On The Specified Parameters
3. Saving To File: The Generated Phrases Are Saved To A Text File In The combo Directory, With A Random Filename For Each Run

The Generated Mnemonic Phrases Are Based On A Strong Cryptographic Random Number Generator, Ensuring That They Are Secure And Cannot Be Easily Predicted

## Examples

Here Is An Example Of What The Output Might Look Like After Running The Script:

```bash
Please Enter The Number Of Words For The Seed Phrase (12 Or 24): 12
Please Enter The Number Of Mnemonic Phrases To Generate: 11

[====================] 11/11 (100%)
3 Mnemonic Phrases Have Been Written To 'combo/12/abc12345_mnemonic_phrases.txt'
```

Each Mnemonic Phrase Will Be Saved In A File Like The Following:

```bash
phrase1 mnemonic phrase example goes here
phrase2 mnemonic phrase example goes here
phrase3 mnemonic phrase example goes here
```

You Can Then Use These Phrases For Cryptographic Purposes, Such As Wallet Backup And Recovery

## License

This Project Is Licensed Under The MIT License - See The LICENSE File For Details

## Contributing

Contributions Are Welcome! If You Have Ideas To Improve The Script, Feel Free To Fork The Repository, Create A New Branch, And Submit A Pull Request

1. Fork The Repository
2. Create A New Branch (git checkout -b feature-branch)
3. Commit Your Changes (git commit -am 'Add new feature')
4. Push To The Branch (git push origin feature-branch)
5. Create A New Pull Request

Thank You For Using The Mnemonic Phrase Generator! If You Have Any Issues Or Suggestions, Please Open An Issue On GitHub
