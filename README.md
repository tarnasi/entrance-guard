# Make Enterence

## Packages

```toml
"bcrypt>=5.0.0",
"cryptography>=49.0.0",
"fastapi[standard]>=0.138.1",
"mysql-connector-python>=9.7.0",
"python-jose>=3.5.0"
```
## Install UV package manager

MAC / Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

*_Consider restart your terminal_*

## Enviroment

Install Packages:

```sh
# Optional: add venv with command below
uv venv
# activate the enviroment to have isolated enviroment
source .venv/bin/activate  # MAC / Linux
.venv/Scripts/activate     # Windows

# Will install packages
uv sync
```

## Add RSA files

Should create two private and public pem in storage/rsa folder

```sh
# Private Key
openssl genrsa -out storage/rsa/private.pem 2048

# Public Key
openssl rsa -in storage/rsa/private.pem -pubout -out storage/rsa/public.pem
```

The **public key** encrypts passwords on the client. The **private key** stays on the server and decrypts them in `app/utils/rsa.py`.

## Login and register payloads

Passwords must be **RSA-encrypted** before you send them. Do not send plain text like `"shahriyar"` in the `password` field.

### 1. Encrypt your password

From the project root, run:

```sh
uv run python -c "from app.utils.rsa import encrypt_password; print(encrypt_password('shahriyar'))"
```

Replace `shahriyar` with your real password. The output is a long base64 string (~344 characters).

### 2. Build the JSON body

**Register** (`POST /api/auth/register`):

```json
{
  "name": "shahriyar tarnasi",
  "email": "shahryar.tarnasi@gmail.com",
  "password": "<paste the encrypted base64 string here>"
}
```

**Login** (`POST /api/auth/login`):

```json
{
  "email": "shahryar.tarnasi@gmail.com",
  "password": "<paste the encrypted base64 string here>"
}
```

Use the **same plain password** for register and login. Encrypt it again each time you send a request (RSA output is different every time, and that is normal).

### 3. Send the request

```sh
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"shahriyar tarnasi","email":"shahryar.tarnasi@gmail.com","password":"YOUR_ENCRYPTED_PASSWORD"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"shahryar.tarnasi@gmail.com","password":"YOUR_ENCRYPTED_PASSWORD"}'
```

### Flow summary

1. Client encrypts plain password with `storage/rsa/public.pem` (PKCS1v15), then base64-encodes it.
2. Server decrypts with the private key, then bcrypt-hashes (register) or bcrypt-checks (login).
3. On successful login, the server returns a JWT signed with **HS256** and your `JWT_SECRET`.

If you registered earlier with a plain-text password, register again using an encrypted password so login can work.

## For your information

**JWT tokens in this project use `HS256` with `JWT_SECRET` from `.env`. RSA keys are used for password encryption only.**

<table>
  <thead>
    <tr>
      <th>Algorithm Value</th>
      <th>Digital Signature or MAC Algorithm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>HS256</code></td>
      <td>HMAC using SHA-256 hash algorithm</td>
    </tr>
    <tr>
      <td><code>HS384</code></td>
      <td>HMAC using SHA-384 hash algorithm</td>
    </tr>
    <tr>
      <td><code>HS512</code></td>
      <td>HMAC using SHA-512 hash algorithm</td>
    </tr>
    <tr>
      <td><code>RS256</code></td>
      <td>RSASSA using SHA-256 hash algorithm</td>
    </tr>
    <tr>
      <td><code>RS384</code></td>
      <td>RSASSA using SHA-384 hash algorithm</td>
    </tr>
    <tr>
      <td><code>RS512</code></td>
      <td>RSASSA using SHA-512 hash algorithm</td>
    </tr>
    <tr>
      <td><code>ES256</code></td>
      <td>ECDSA using SHA-256 hash algorithm</td>
    </tr>
    <tr>
      <td><code>ES384</code></td>
      <td>ECDSA using SHA-384 hash algorithm</td>
    </tr>
    <tr>
      <td><code>ES512</code></td>
      <td>ECDSA using SHA-512 hash algorithm</td>
    </tr>
  </tbody>
</table>

## Run Project

fro development

```sh
uv run fastapi dev
```
