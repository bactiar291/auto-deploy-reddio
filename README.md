# auto-deploy-reddio
auto deploy smart contract /contract creation reddio testnet
## Tracking Deploy Di explorer Cek 👇 :

   reddio-devnet.l2scan.co

## Cara Menggunakan
1. Clone repositori ini ke mesin lokal Anda:
    ```bash
    git clone https://github.com/bactiar291/auto-deploy-reddio.git
    ```

2. Salin perintah di bawah ini untuk masuk ke folder:
    ```bash
    cd auto-deploy-reddio
    ```

3. Untuk meng-install dependencies secara manual (jika diperlukan), jalankan perintah berikut:
    ```bash
    pip install -r requirements.txt
    ```

4. Jangan lupa untuk mengganti variabel di file `.env`:
    ```bash
    nano .env
    ```
    Isi **Alamat Address** dan **Private Key** seperti ini:

    ```
    ACCOUNT_ADDRESS=PASTE_ALAMAT_ADDRESS_KAMU_DISINI
    PRIVATE_KEY=PASTE_PRIVATE_KEY_KAMU_DISINI
    ```

6. Untuk menjalankan dependencies:
    ```bash
    python3 deploy.py
    ```

    license "MIT" bactiar291
