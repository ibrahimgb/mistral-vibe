---
title: "vibe.core.auth.crypto"
tldr: "Module vibe.core.auth.crypto"
tags: [reference, api]
---

# [**vibe.core.auth.crypto**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/crypto.py)

This module defines the constants `_AES_KEY_SIZE`, `_NONCE_SIZE`, `_MIN_RSA_KEY_SIZE`, `_MAX_ENCRYPTED_KEY_SIZE`, `_MAX_CIPHERTEXT_SIZE`, `_PAYLOAD_VERSION`, `_ALG`, `_ENC`.

## [**EncryptedPayload**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/crypto.py#L24)

The [**EncryptedPayload**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/crypto.py#L24) dataclass. Key fields include `encrypted_key`, `nonce`, `ciphertext`, `version`, `alg`, `enc`, `kid`, `purpose`.

## [**encrypt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/crypto.py#L68)

```python
def encrypt(plaintext: str, public_key_pem: bytes) -> EncryptedPayload
```

## [**decrypt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/crypto.py#L110)

```python
def decrypt(payload: EncryptedPayload, private_key_pem: bytes) -> str
```

