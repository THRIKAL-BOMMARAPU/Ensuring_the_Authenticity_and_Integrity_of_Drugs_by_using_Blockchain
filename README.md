# 💊 Ensuring the Authenticity and Integrity of Drugs by Using Blockchain

A **full-stack blockchain-based web application** to trace the production, authenticity, and distribution of pharmaceutical drugs using **Ethereum smart contracts**, ensuring **transparency**, **integrity**, and prevention of **counterfeit drugs** in the medical supply chain.

---

## 🚀 Project Objective

To develop a **secure** and **transparent** system that:

- 🔍 Tracks drugs from **manufacturer to retailer**
- ❌ Prevents **counterfeit drugs**
- ✅ Verifies authenticity via **smart contracts and QR codes**
- 🧾 Logs all operations **immutably** on the blockchain

---

## 🧩 Key Features

- ✅ Ethereum Smart Contract for drug lifecycle tracking (`Drug.sol`)
- ✅ Local Ethereum Blockchain using **Ganache**
- ✅ **Django backend** for admin panel and record storage
- ✅ **HTML/CSS/JavaScript** frontend for role-based dashboards
- ✅ Integration with **Web3.js** and **MetaMask** for blockchain interaction

---

## 🛠️ Tech Stack

| Layer           | Technology                        |
|----------------|------------------------------------|
| Smart Contract  | Solidity (Ethereum)               |
| Blockchain      | Ganache (Local Ethereum Node)     |
| Backend         | Django (Python) + SQLite          |
| Frontend        | HTML, CSS, JavaScript             |
| Others          | Web3.js, Merkle Tree              |

---

## 📁 Project Structure

```

.
├── DrugTracing/               # Django backend (models, views, templates, etc.)
├── hello-eth/                 # Node.js interface for smart contract
│   ├── node\_modules/
│   ├── package.json
│   └── ...
├── Drug.sol                   # Ethereum smart contract
├── .gitignore
├── README.md
└── requirements.txt           # Python dependencies

````

---

## 📸 Functional Flow

1. 👨‍💼 Admin registers a manufacturer and creates a drug batch.
2. 🔐 Drug details are stored on the blockchain (`Drug.sol`) with **Merkle hash** integrity.
3. 🔁 Distributor and Retailer **scan** and **update** drug status in real-time.
4. ✅ Customer scans the QR code to **verify authenticity** before use.

---

## 💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/THRIKAL-BOMMARAPU/Ensuring_the_Authenticity_and_Integrity_of_Drugs_by_using_Blockchain.git
cd Ensuring_the_Authenticity_and_Integrity_of_Drugs_by_using_Blockchain
````

---

### 2. Set up the Django Backend (`DrugTracing`)

```bash
cd DrugTracing
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver
```

---

### 3. Run the Smart Contract (`Drug.sol`)

* Open [Remix IDE](https://remix.ethereum.org/)
* Create a new file `Drug.sol` and paste your smart contract code
* Compile the contract
* Deploy using **Injected Web3** (with MetaMask connected to Ganache)

---

### 4. Run the Node.js Interface (`hello-eth`)

```bash
cd hello-eth
npm install
node app.js  # or use the appropriate entry point
```

---

## 🔐 Smart Contract Details

* **Contract Name:** `Drug.sol`
* **Key Functions:**

  * `addDrug()`: Add new drug batch
  * `transferDrug()`: Move drug to the next level in the supply chain
  * `verifyDrug()`: Authenticate batch using Merkle hash
  * `getDrugDetails()`: Fetch on-chain drug metadata

All records are **secure**, **verifiable**, and **immutable** on the blockchain.

---

## 📦 Future Scope

* 🌐 Integration with **IPFS** for decentralized file storage
* 🚀 Deployment to Ethereum **Testnet** (Goerli or Sepolia)
* 📡 **IoT integration** for temperature, humidity, and location tracking
* 📱 Launch of a **mobile app** for field agents to scan and verify drugs

---

## 🙌 Acknowledgements

* [Ganache](https://trufflesuite.com/ganache/)
* [Remix IDE](https://remix.ethereum.org/)
* [Web3.js Documentation](https://web3js.readthedocs.io/)
* [Django](https://www.djangoproject.com/)

---


