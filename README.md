<div align="center">
  <h1>⛽ FuelFinder Mali</h1>
  <p>
    <strong>Account-Free Crowdsourced Crisis-Response Platform for Real-Time Fuel Availability</strong>
  </p>
  <p>
    Privacy-first web platform built during Mali's national fuel shortage—combining <strong>Redis rate limiting</strong>, <strong>12-hour automatic record expiry</strong>, <strong>phonetic + Levenshtein station matching</strong>, and a <strong>heuristic consensus validation rule</strong>.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Backend-Django_5.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django 5.2" />
    <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Cache_%26_Rate_Limit-Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
    <img src="https://img.shields.io/badge/Deployment-Docker_%7C_Railway-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/Research-Peer--Reviewed_(BUSINTA)-0A66C2?style=for-the-badge" alt="Research" />
  </p>
</div>

---

## 📖 Overview

**FuelFinder Mali** is an account-free crowdsourced reporting platform designed to help residents locate active fuel stations during acute supply shortages without requiring user registration, personal identifiers, or manual human moderation.

Built and deployed in production for a 90-day crisis window, the system balances **low-friction public participation** and **user privacy** against **spam, stale data, and false reporting**.

> 📄 **Academic Reference:** Based on *"Heuristic Consensus for Anonymous Data Validation in Crisis Systems"* — Cheick Tidiani Diawara & Didik Dwi Prasetya, Universitas Negeri Malang & USTTB Bamako.

---

## ✨ Key Engineering & Algorithmic Features

- 🕵️ **Zero-Account Privacy-First Reporting** — Citizens submit station status (`disponible` or `indisponible`) without creating accounts; no names, phone numbers, or persistent user IDs are stored in PostgreSQL
- ⏳ **12-Hour Automatic Record Expiry** — Station reports automatically expire and purge after **12 hours** to prevent stale availability data from misleading drivers
- 🚦 **Redis IP Rate Limiting** — Fixed-window rate limiter (`5 submissions / 900s`) backed by `django-redis` using transient client IP keys that auto-expire within 15 minutes
- 🔤 **Two-Stage Station Name Matching** — Normalizes multilingual French/Bambara spelling variants (lowercasing, accent stripping, phonetic mapping such as `ou` → `u`) and groups reports using length-adaptive Levenshtein distance (`Threshold = max(2, ceil(len / 5))`) and similarity (`>= 0.85`)
- ✅ **Heuristic Consensus Validation (`K = 5`)** — Marks a station status `x` as **Verified** only when at least `K = 5` distinct reporters agree and confirmations strictly outnumber contradictions (`c_x >= 5` and `c_x > c_y`); otherwise holds the station as **Pending**
- 🗺️ **Interactive Geolocation Map** — Mobile-friendly map interface powered by the **Google Maps API** and browser geolocation

---

## 🏗️ System Architecture

```text
┌─────────────────────────────┐
│   Citizens (Mobile / Web)   │
│  Browser Geolocation + Map  │
└──────────────┬──────────────┘
               │ HTTPS (CSRF & Secure Session Cookies)
               ▼
┌──────────────────────────────────────────────────────────┐
│                 Django 5.2 Application                   │
│                                                          │
│  ┌────────────────────┐   ┌───────────────────────────┐  │
│  │ Validation & Purge │   │ Consensus & Matching      │  │
│  │ • Field checks     │   │ • Phonetic + Levenshtein  │  │
│  │ • 12h TTL cleanup  │   │ • Heuristic rule (K = 5)  │  │
│  └─────────┬──────────┘   └─────────────┬─────────────┘  │
└────────────┼────────────────────────────┼────────────────┘
             │                            │
             ▼                            ▼
┌─────────────────────────┐  ┌─────────────────────────────┐
│       PostgreSQL        │  │            Redis            │
│ (Ephemeral 12h Reports) │  │ (5 req / 15m Rate Limiter)  │
└─────────────────────────┘  └─────────────────────────────┘
