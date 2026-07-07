# Make Enterence

### Packages

```toml
"bcrypt>=5.0.0",
"cryptography>=49.0.0",
"fastapi[standard]>=0.138.1",
"mysql-connector-python>=9.7.0",
"python-jose>=3.5.0"
```

### Enviroment

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

### Add RSA files

Should create two private and public pem in storage/rsa folder

```sh
# Private Key
openssl genrsa -out storage/rsa/private.pem 2048

# Public Key
openssl rsa -in storage/rsa/private.pem -pubout -out storage/rsa/public.pem
```


### For your information

**<u>You most use this in jwt encoder and decoder</u>**

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


