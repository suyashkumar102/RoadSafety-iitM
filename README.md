# RoadSoS

Offline-first accident response assistant for the Road Safety Hackathon 2026 by CoERS, RBG Labs, IIT Madras.

RoadSoS helps a bystander move from location to trusted emergency contacts quickly, even when the network is weak. The product is designed around source-backed contacts, deterministic ranking, offline rescue cache, and a guarded assistant that refuses to invent emergency information.

## Chosen problem statement

RoadSoS: a location-based emergency support tool for accidents.

## Repository map

- `plan.md` - team execution plan, merge points, task ownership, and review gates.
- `info.md` - hackathon information and original problem statement summary.
- `contracts/` - shared schemas and API examples all branches must follow.
- `data/` - source-backed emergency data, fallbacks, and data notes.
- `backend/` - FastAPI service scaffold.
- `frontend/` - React/Vite PWA scaffold.
- `docs/` - submission, review, and assumptions documents.
- `demo/` - golden scenario and live judging script.

## Branches

- `codex/roopal-product-submission`
- `codex/suyash-data-geo-backend`
- `codex/sidhesh-frontend-offline-ai`
- `codex/final-roadsos-submission`

All implementation branches should start from the same bootstrap `main`.

## Safety rules

- Do not generate emergency phone numbers, addresses, or service names with AI.
- Production contacts must be source-backed and include verification metadata.
- Assistant responses must cite curated data or approved templates.
- If the app cannot verify something, it should say so and show official fallback guidance.

## Current scaffold

This repository intentionally starts with contracts, docs, and small app skeletons. Suyash and Sidhesh can build their streams without changing ownership boundaries, while Roopal can review PRs against `plan.md` and `docs/pr_review_checklist.md`.

