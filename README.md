# Ensuring the Authenticity and Integrity of Drugs by Using Blockchain

A full-stack blockchain-based web application to trace the **production, authenticity, and distribution of pharmaceutical drugs** using **Ethereum smart contracts**, ensuring transparency, integrity, and prevention of counterfeit drugs in the medical supply chain.

---

## 🚀 Project Objective

To develop a secure and transparent system that:
- Tracks drugs from manufacturer to retailer
- Prevents counterfeit drugs
- Verifies authenticity via smart contracts and QR codes
- Logs all operations immutably on the blockchain

---

## 🧩 Key Features

- ✅ Ethereum smart contract for drug lifecycle tracking (`Drug.sol`)
- ✅ Local Ethereum blockchain (Ganache) for development
- ✅ Django backend for record storage and admin operations
- ✅ Html,css,javascript frontend for role-based dashboards
- ✅ Web3.js + MetaMask for blockchain interaction

---

## 🛠️ Tech Stack

| Layer        | Technology                           |
|--------------|---------------------------------------|
| Smart Contract | Solidity (Ethereum)                |
| Blockchain   | Ganache (Local Ethereum Node)         |
| Backend      | Django (Python) + SQLite              |
| Frontend     | Html, Css , JavaScript                 |
| Others       | Web3.js , Merkle Tree |

---

## 📁 Project Structure

├── DrugTracing/                
│   └── [models, views, urls, templates, etc.]                                                                                                                                                                       
├── hello-eth/                                                                                                                                                                                                       
│   ├── node_modules/                                                                                                                                                                                                
│   ├── package.json                                                                                                                                                                                                 
│   └── ...                                                                                                                                                                                                          
├── Drug.sol                                                                                                                                                                                                         
├── .gitignore                 
├── README.md                 
└── requirements.txt            

## 📸 Functional Flow

1. **Admin** registers a drug manufacturer and creates a drug batch.
2. **Drug** details are written on the blockchain (`Drug.sol`) with hash integrity.
3. **Distributor** and **Retailer** scan and update drug status.
4. **Customer** verifies the drug's authenticity before use.

---

## 💻 Setup Instructions

 1. Clone the repository
git clone https://github.com/THRIKAL-BOMMARAPU/Ensuring_the_Authenticity_and_Integrity_of_Drugs_by_using_Blockchain.git
cd Ensuring_the_Authenticity_and_Integrity_of_Drugs_by_using_Blockchain
2. Set up the Django Backend (DrugTracing)
cd DrugTracing
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver
3. Run the Smart Contract (Drug.sol)
Open Remix IDE
Create a new file Drug.sol and paste your smart contract code
Compile and deploy it using Injected Web3 (connected to Ganache or MetaMask)
4. Run the Node.js interface (hello-eth)

cd hello-eth
npm install
node app.js     # or the main interaction file

## 🔐 Smart Contract Details

Contract Name: Drug.sol
Key Functions:
addDrug(): Add new drug batch
transferDrug(): Move drug to next supply chain level
verifyDrug(): Authenticate batch via hash
getDrugDetails(): Fetch on-chain info
All drug records are secure, verifiable, and immutable.

## 📦 Future Scope
Integration with IPFS for decentralized data storage
Deployment to Ethereum Testnet (Goerli/Sepolia)
IoT integration for real-time environment sensing
Mobile app for field agents
