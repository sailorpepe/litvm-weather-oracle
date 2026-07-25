<div align="center">
  <h1>🌩️ LitVM Weather Oracle & Alpha Engine</h1>

  <p><strong>Immutable Oracle Infrastructure for Parametric DeFi & the M2M Economy.</strong></p>

  <p>
    <a href="https://the-undesirables.com/weather"><strong>Live Dashboard</strong></a> ·
    <a href="https://liteforge.explorer.caldera.xyz/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696"><strong>Verified Contract</strong></a>
  </p>
</div>

---

## 🏛️ Overview: The Oracle Problem

## 🔌 Connect over MCP — one URL, no install

```
https://mcp.the-undesirables.com
```

Paste into any MCP client (Claude, Cursor, ChatGPT) — free card search & forecasts, paid calls via x402.


Smart contracts are mathematically locked out of the real world. A DeFi protocol cannot make an API call to check if it rained in Chicago today—it only knows what is explicitly pushed to it on-chain. 

This creates a massive bottleneck for global risk hedging. How can a decentralized insurance protocol execute an automated payout for crop failure if the smart contract can't verify the weather?

**The LitVM Weather Oracle solves this.** We bridge live National Weather Service (NWS) ASOS data and High-Resolution Rapid Refresh (HRRR) models directly on-chain. By hashing this data into a Merkle root and publishing it to the `WeatherEdgeOracle` contract on LiteForge every hour, we create an **immutable, cryptographically verified ledger of weather history** that smart contracts can trust.

---

## 🚀 Use Cases & Consumers

This infrastructure is not just for predicting the weather. It is the critical "Truth Layer" designed for:

1. **Parametric DeFi Protocols**: 
   Smart contracts can now execute purely code-enforced automation (if-so-then logic). 
   *Example: A solar farm hedges its revenue. `IF [Oracle reports > 15 cloudy days] THEN [Instant USDC Payout].` No human claims adjusters, no delays.*
2. **Decentralized Prediction Markets (e.g., Polymarket)**: 
   Decentralized markets need an unbiased, code-driven resolution layer. Our smart contracts allow external prediction markets to resolve their weather outcomes trustlessly without relying on centralized committees.
3. **Autonomous Quants (AI Agents)**: 
   In the M2M (Machine-to-Machine) economy, autonomous trading bots can query our edge models to execute high-frequency trades on synthetic commodities or Web2 markets like Kalshi based on verified weather shifts.

---

## 🧠 Architecture: Truth vs. Alpha

Our ecosystem operates in two distinct layers:

### 1. The Truth Layer (Oracle Infrastructure)
The foundation. This layer acts as a strict cryptographic mirror of the National Weather Service. It pulls raw 1-minute ASOS sensor observations, verifies them via LitVM, and publishes the Merkle Root to the blockchain. 
* **Value:** It prevents Web2 data providers from silently revising historical forecasts, establishing a permanent source of truth for DeFi applications.

### 2. The Alpha Layer (The Edge Engine)
Our proprietary off-chain application layer built on top of the Truth Layer. The "Shroomy Simulator" ingests the verified NWS data and cross-references it against live Kalshi orderbooks.
* Calculates probability distributions using Student's t-distribution.
* Detects actionable market edges using the **Kelly Criterion** for bet sizing.
* Identifies **Ghost Traps** (temporary heat anomalies that trick retail traders) to protect algorithmic deployments.

---

## ⚖️ Disclaimer & Liability

**This software is provided "AS-IS" for informational and historical documentation purposes only.**

The Undesirables LLC operates this Oracle as an immutable data conduit reflecting public National Weather Service (NWS) APIs. We are **not** a financial institution, a registered investment advisor, or a hedge fund. We do not facilitate trades or manage funds. 

If third-party developers, DeFi protocols, or autonomous AI agents choose to consume this data feed to build Parametric Insurance protocols, Prediction Markets, or automated trading strategies, they do so entirely at their own risk. The Undesirables LLC explicitly disclaims all liability for financial losses, liquidations, or faulty smart contract executions resulting from API downtime, data inaccuracies, or force majeure events.

---

## 🔗 Links

- **Live Site**: [the-undesirables.com/weather](https://the-undesirables.com/weather)
- **Contract**: [LiteForge Explorer](https://liteforge.explorer.caldera.xyz/address/0x9955afC8AE25405ed9FcE66c23fa8E02eB3b6696)
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
