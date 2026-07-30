# GenLayer AI Crypto Portfolio Builder

A decentralized, AI-powered spot crypto portfolio builder built on top of **GenLayer** intelligent contracts. This application evaluates a user's capital and risk tolerance, fetches live market context from the web, and leverages multi-validator LLM consensus to construct a diversified, customized crypto portfolio.

## 🚀 Features

- **Nondeterministic Web Data Fetching:** Uses Python's `urllib` inside the smart contract to fetch live web sources, ensuring multi-validator consensus verification.
- **AI Consensus Validation:** Employs GenLayer's multi-node LLM evaluation to generate robust, professional spot asset allocations.
- **Structured JSON Output:** Returns clean, parsed asset allocations (Asset, Percentage, Amount, and Reasoning) rendered dynamically on a modern frontend.
- **Modern UI / UX:** Built with Tailwind CSS and integrated directly with `genlayer-js` for seamless on-chain execution (`writeContract` & `readContract`).

## 📦 Smart Contract Details

- **Network:** GenLayer Simulator
- **Contract Address:** `0x0c8714997fF63b7775F71825B26cF4d091146bb9`
- **Main Functions:**
  - `build_portfolio(capital: str, risk_tolerance: str) -> str`: Fetches web data, runs LLM consensus, and returns a JSON portfolio.
  - `get_last_portfolio() -> str`: Retrieves the last generated portfolio state.
  - `get_stats() -> u256`: Returns the total number of requests processed.

## 🛠️ Tech Stack

- **Smart Contract:** Python (GenLayer SDK)
- **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6 Modules)
- **Blockchain Integration:** `genlayer-js`

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/genlayer-crypto-portfolio-builder.git](https://github.com/your-username/genlayer-crypto-portfolio-builder.git)
