

# 🔐 XShifter Encryption System  

## 📌 Overview  
XShifter is a custom encryption algorithm developed by **Mohammad Danish** that combines **XOR encryption** with a **key-based binary swapping mechanism**. It provides a lightweight encryption method for encoding textual data with a user-defined key.  

🔹 This repository contains two scripts:  
- 🔒 `xShifter_encrypt.py` - For encryption  
- 🔓 `xShifter_decrypt.py` - For decryption  

---

## 🔢 Encryption Technique  
XShifter encrypts data using the following steps:  

1️⃣ **Convert text to binary** - The plaintext is converted into an 8-bit binary representation.  
2️⃣ **Perform XOR encryption** - A bitwise XOR operation is performed between the binary data and the binary representation of the key (repeated as needed).  
3️⃣ **Key-based binary swapping** - Each character of the key determines a split index for the encrypted binary, and sections of the binary string are swapped accordingly to add extra scrambling.  

---

## 🔄 Decryption Process  
To decrypt the encrypted data, XShifter follows these steps:  

1️⃣ **Reverse binary swapping** - The binary sections are swapped back in the reverse order using the key.  
2️⃣ **XOR decryption** - The XOR operation is applied again with the same key to retrieve the original binary data.  
3️⃣ **Convert binary back to text** - The binary string is converted back into human-readable text.  

---

## ✅ Strengths  
✔️ **Lightweight & Simple** - Does not require heavy computation.  
✔️ **Symmetric Encryption** - Uses the same key for encryption & decryption.  
✔️ **Custom Key-Based Swapping** - Provides extra obfuscation beyond XOR encryption alone.  

---

## ❌ Vulnerabilities & Weaknesses  
⚠️ **Not Cryptographically Secure** - Not recommended for sensitive data.  
⚠️ **XOR Encryption is Reversible** - Can be broken easily using known-plaintext attacks.  
⚠️ **Predictable Swapping** - Swaps can be reversed if the key is guessed.  
⚠️ **Brute Force Attacks** - Short keys can be cracked quickly.  
⚠️ **No Randomization** - Repeated encryptions produce predictable patterns.  

---

## ⚠️ Cautions: Where to Use & Where Not to Use  

### ✅ Suitable For:  
✔️ **Basic Data Obfuscation** - Prevent casual users from reading text.  
✔️ **Encoding Non-Critical Data** - Where encryption is not the main security concern.  
✔️ **Learning & Experimentation** - Helps understand encryption concepts.  

### ❌ Not Suitable For:  
🚫 **High-Security Applications** - Avoid for passwords, banking, or personal data.  
🚫 **Secure Communication** - No confidentiality, integrity, or authentication.  
🚫 **Long-Term Encryption** - Weak security makes it easy to break over time.  

---

## 🚀 Usage  
You can run XShifter using the individual scripts **or** via `xShifter.py` which combines both.  

### 🔒 Encryption  
```bash
python xShifter_encrypt.py
```
➡️ Enter the **data** and **key** when prompted.  
➡️ The encrypted binary output will be displayed.  

### 🔓 Decryption  
```bash
python xShifter_decrypt.py
```
➡️ Enter the **encrypted binary data** and **key**.  
➡️ The original plaintext will be restored.  

### 🔄 Alternative: Run Directly  
You can also run it using:  
```bash
python xShifter.py
```
➡️ Enter the **data** and **key** for encryption or decryption.  

---

## 🛠️ Code Example  

### 🔐 Encrypting a Message  
```python
from xShifter_encrypt import xshifter_encrypt

plain_text = "Hello, World!"
key = "SecureKey"
encrypted_text = xshifter_encrypt(plain_text, key)
print("🔒 Encrypted:", encrypted_text)
```

### 🔓 Decrypting a Message  
```python
from xShifter_decrypt import xshifter_decrypt

decrypted_text = xshifter_decrypt(encrypted_text, key)
print("🔓 Decrypted:", decrypted_text)  # Output: Hello, World!
```

---

## 📌 Conclusion  
XShifter is a **fun and educational encryption algorithm**, but **⚠️ DO NOT** use it for serious security needs. For secure encryption, use industry-standard methods like **AES or RSA**.  

---

## 👤 Creator  
Made with ❤️ by **Mohammad Danish**  

📌 **LinkedIn:** [Mohammad Danish](https://www.linkedin.com/in/mohammad-danish-76570a24a/)  
📷 **Instagram:** [@\_Itz\_danish\_](https://www.instagram.com/_itz_danish_/)  

