<div align="center">
  <h1>🍄 Weather Alpha Dashboard</h1>

  <p><strong>An entirely new breed of on-chain oracle running on LitecoinVM (LitVM).</strong></p>

  <p>
    <a href="https://the-undesirables.com/weather"><strong>Live Dashboard</strong></a> ·
    <a href="https://litescan.info/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696"><strong>Verified Contract</strong></a>
  </p>
</div>

---

## 🌩️ Overview

The Weather Alpha Dashboard is a verifiable on-chain oracle that cross-references live National Weather Service (NWS) forecasts against Kalshi prediction markets to detect real-time pricing edges.

Every hour, the full scan is Merkle-hashed and published on-chain via the `WeatherEdgeOracle` contract on LiteForge, creating an immutable, timestamped proof of the scanner's detection model.

---

## 🏛️ Architecture

This project is built using a hybrid architecture to ensure both on-chain transparency and off-chain execution speed.

### ⛓️ 1. The Smart Contract (Open Source)
The `WeatherEdgeOracle` is deployed natively on LiteForge. It accepts an hourly Merkle root of the detected edges, allowing anyone to cryptographically verify historical pricing models without exposing the proprietary algorithms that produced them.

- **Network:** LiteForge Testnet (Chain ID 4441)
- **Contract Address:** [`0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696`](https://litescan.info/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696)

### 🖥️ 2. The Dashboard (Open Source)
The dashboard interface is fully open-source. It provides a real-time UI to view the Kalshi vs. NWS data, Kelly bet sizing, and HRRR divergence metrics.
- **UI Repository:** [github.com/sailorpepe/the-undesirables](https://github.com/sailorpepe/the-undesirables)

### 🧠 3. The Shroomy Simulator Engine (Closed Source)
The off-chain data-fetching, prediction modeling, and Merkle tree generation is handled by our proprietary backend engine. 
- **Data Ingestion:** Pulls NWS forecasts across 10 major cities, ASOS 1-minute sensor observations, HRRR model divergence, and live Kalshi orderbooks.
- **Edge Detection:** Calculates probability distributions using a Student's t-distribution. If the market price significantly disagrees with the modeled forecast, it flags an actionable edge and uses the **Kelly Criterion** for entry sizing.
- **Ghost Trap Detection:** Identifies markets where temporary heat peaks (caught by 1-minute sensors) look like edges but are actually traps, saving users from getting burned.

*Note: The core strategy code remains closed-source to protect the proprietary alpha models, but all data outputs are immutably verified on LiteForge.*

---

## 🔗 Links

- **Live Site**: [the-undesirables.com/weather](https://the-undesirables.com/weather)
- **Contract**: [LiteForge Explorer](https://litescan.info/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696)
- **Frontend Source**: [the-undesirables](https://github.com/sailorpepe/the-undesirables)
- **X / Twitter**: [@undesirables_ai](https://x.com/undesirables_ai)

---

## 📝 License & Commercial Use

This project is licensed under the **[Business Source License 1.1 (BUSL-1.1)](LICENSE)**.

**Licensor:** The Undesirables LLC  
**Change Date:** 2030-06-06  
**Change License:** Apache License, Version 2.0  

We build in public and support the developer ecosystem — but we also protect the infrastructure and IP of **The Undesirables LLC**.

<div align="center">

⭐ **If this project helped you, please star this repo** — it helps others find it.

</div>
