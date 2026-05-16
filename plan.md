# RoadSoS Hackathon Execution Plan

## Agreed upon points-
- We will build for the **RoadSoS** problem statement from the Road Safety Hackathon 2026.
- Product direction: **offline-first accident response orchestrator**, not a generic chatbot.
- Core demo promise: **a bystander can get the right emergency help in under 10 seconds, even with weak or no network**.
- Golden demo region: **IIT Madras / Chennai**.
- Portability proof: add one compact second-region sample to prove the schema can support other cities or countries.
- First screen of the app must be the emergency action screen. No marketing landing page.
- No AI-generated phone numbers, addresses, hospital names, police stations, ambulance contacts, towing contacts, or official claims.
- Every displayed service must come from curated data and show source, last verified date, confidence, and why it was ranked.
- The assistant can summarize, translate, and guide, but it cannot invent contacts, medical advice, legal advice, or dispatch status.
- Offline mode is a first-class requirement. The Chennai rescue cache must work when the browser is offline.
- The final submission must include code, 7-slide deck, package/assumption document, data-source notes, and a repeatable demo script.
- Roopal reviews PRs into `main`; Suyash and Sidhesh should keep PRs small enough to review but substantial enough to show progress.
- Branches should start from the same bootstrap `main` after this plan and base scaffold are merged.

## Problem statement summary-
- Organizer: Centre of Excellence for Road Safety, RBG Labs, IIT Madras.
- Theme: AI in Road Safety, with focus on AI-powered chatbots.
- Chosen track: RoadSoS.
- RoadSoS asks for a location-based emergency support tool for accidents.
- Required capability areas:
  - Nearby police stations, hospitals, and ambulance services.
  - Nearby towing, puncture shops, and showrooms.
  - Global applicability.
  - Offline support for low-network conditions.
- Evaluation criteria from the hackathon information:
  - Reliability and data accuracy.
  - Number and quality of fetched contacts.
  - Offline functionality.
  - Innovation and extra features.
  - Cross-region information integration.

## Internal scoring proxy-
- Reliability and data accuracy: 30 points.
- Number, quality, and ranking of contacts: 20 points.
- Offline functionality: 20 points.
- Innovation and extra features: 15 points.
- Cross-region architecture: 10 points.
- UI clarity and accessibility: 5 points.

## Working model-
- Shared repository trunk: `main`.
- Roopal branch: `codex/roopal-product-submission`.
- Suyash branch: `codex/suyash-data-geo-backend`.
- Sidhesh branch: `codex/sidhesh-frontend-offline-ai`.
- Final integration branch: `codex/final-roadsos-submission`.
- PR base for all work: `main`.
- Each PR must include:
  - What changed.
  - Screenshots or API examples when applicable.
  - Tests or manual verification performed.
  - Known limitations.
  - Files or contracts other branches must react to.

## Shared product architecture-
- Frontend: React + Vite PWA.
- Backend: Python FastAPI.
- Data store: SQLite generated from curated JSON seed files.
- Offline layer: service worker plus static/IndexedDB cache package.
- AI layer: guarded assistant with retrieval-only contacts and approved safety templates.
- Ranking layer: deterministic scoring before any assistant response.
- Submission docs: Markdown source now, converted into required deck/document later.

## Shared contracts-
- Contact record fields:
  - `id`
  - `name`
  - `type`
  - `lat`
  - `lon`
  - `phone`
  - `address`
  - `locality`
  - `region`
  - `country`
  - `source_url`
  - `source_name`
  - `verified_at`
  - `availability`
  - `confidence_score`
  - `confidence_reasons`
  - `notes`
- Service types:
  - `hospital`
  - `trauma_center`
  - `ambulance`
  - `police`
  - `tow`
  - `repair`
  - `fallback_emergency`
- Required API endpoints:
  - `GET /health`
  - `POST /api/nearby-services`
  - `GET /api/cache-package`
  - `POST /api/incident-summary`
  - `POST /api/assistant`

## Judge-dopamine features to build-
- **10-second rescue drill:** the demo includes a visible internal stopwatch proving that location to ranked help can be completed in under 10 seconds.
- **Offline rescue pack:** Chennai contacts, official emergency fallback, source metadata, and approved safety templates remain available in airplane mode.
- **Trust ledger:** each contact has a visible source badge, last verified date, confidence score, and ranking reasons.
- **No-hallucination flight recorder:** assistant responses show whether they came from curated data, approved templates, or refusal logic.
- **Ambulance-ready incident packet:** one tap creates a short shareable summary with location, landmark, injury count, hazards, callback number placeholder, timestamp, and nearest contacts.
- **Bystander mode:** the app gives non-medical role cards: caller, traffic spotter, note taker, location sharer. It keeps people useful without pretending to diagnose.
- **Location confidence ribbon:** shows GPS/manual/cached location status so judges see the app is honest about uncertainty.
- **Panic-friendly UI:** large hit targets, calm copy, low-light contrast, manual location fallback, and no buried emergency button.
- **Cross-region adapter:** a small second region proves that contacts, fallbacks, labels, and emergency numbers are data-driven instead of Chennai-hardcoded.
- **Chaos-mode demo:** final dry run intentionally covers offline, GPS denied, no nearby contacts, and assistant asked for unavailable information.

## Merge 1: Foundation freeze and first branch PRs-

### Goal-
Create a shared base so all three branches can work for a long stretch without breaking contracts.

### Roopal tasks-
- Create or refine product-level docs:
  - `README.md`
  - `plan.md`
  - `docs/pr_review_checklist.md`
  - `docs/submission_requirements.md`
  - `demo/golden_scenario.md`
- Freeze first version of shared contracts:
  - `contracts/contact.schema.json`
  - `contracts/api.examples.json`
- Define the review checklist Roopal will use for all PRs:
  - Does the PR preserve the RoadSoS scope?
  - Does it avoid invented emergency data?
  - Does it respect API and data contracts?
  - Does it include tests or manual verification?
  - Does it improve the golden demo?
- Prepare PR review labels:
  - `contract-change`
  - `data-risk`
  - `offline-risk`
  - `demo-critical`
  - `submission-docs`
- Create PR when:
  - Base docs and contracts are committed.
  - Each teammate can branch without needing private instructions.
  - `main` has a clear README and folder map.
- Suggested PR title:
  - `Bootstrap RoadSoS planning and shared contracts`

### Suyash tasks-
- Read:
  - `info.md`
  - `plan.md`
  - `contracts/contact.schema.json`
  - `contracts/api.examples.json`
  - `data/README.md`
- Create branch:
  - `codex/suyash-data-geo-backend`
- Implement first data/geo foundation:
  - Validate the contact schema locally.
  - Add data validation script plan or implementation.
  - Create deterministic distance-ranking utility.
  - Create confidence scoring rules.
  - Create dedupe rules by normalized name, phone, and nearby coordinates.
  - Prepare fixture contacts for tests only; mark fixtures clearly as non-production.
  - Keep source-backed production data separate from test fixtures.
- Backend foundation:
  - Confirm FastAPI app starts.
  - Add request and response models that match `contracts/api.examples.json`.
  - Add endpoint stubs or first implementation for `/api/nearby-services`.
- Create PR when:
  - Ranking utility works with fixture data.
  - Contact schema validation passes.
  - First backend route can return deterministic fixture results.
  - No production contact is unsourced.
- Suggested PR title:
  - `Add data schema validation and geo ranking foundation`

### Sidhesh tasks-
- Read:
  - `info.md`
  - `plan.md`
  - `contracts/api.examples.json`
  - `frontend/README.md`
  - `demo/golden_scenario.md`
- Create branch:
  - `codex/sidhesh-frontend-offline-ai`
- Implement first frontend/PWA foundation:
  - Create emergency-first screen.
  - Add manual location entry state.
  - Add GPS permission state.
  - Add contact card component using mock contract data.
  - Add offline status indicator.
  - Add responsive mobile layout.
  - Add design tokens for colors, spacing, and focus states.
  - Add placeholder route for incident packet.
- Create PR when:
  - The PWA shell runs locally.
  - Emergency screen is first viewport.
  - Mock contact card matches API contract.
  - Offline indicator reacts to browser network state.
  - Mobile viewport is usable.
- Suggested PR title:
  - `Build emergency-first PWA shell`

### Merge 1 PR order-
1. Roopal PR: contracts and docs.
2. Suyash PR: data/geo/backend foundation.
3. Sidhesh PR: frontend shell.

### Merge 1 acceptance gate-
- `main` contains stable contracts.
- `main` has visible ownership boundaries.
- `main` can support three parallel streams.
- Any contract change after this point must be called out in PR description.

## Merge 2: Reliable core product-

### Goal-
Build the working RoadSoS vertical slice: location in, ranked emergency help out, with backend and frontend connected.

### Roopal tasks-
- Review Suyash PR for:
  - Data provenance.
  - No generated contacts.
  - Ranking explainability.
  - Bad-coordinate behavior.
  - Test coverage.
- Review Sidhesh PR for:
  - First-screen emergency flow.
  - Mobile usability.
  - Offline states.
  - Accessibility.
  - Contract compatibility.
- Update `docs/submission_requirements.md` with any package or assumption changes.
- Keep `demo/golden_scenario.md` aligned with the actual app.
- Create PR when:
  - Review-driven documentation changes are needed.
  - Demo script changes based on working behavior.
  - Submission assumptions need to be recorded.
- Suggested PR title:
  - `Update demo and submission notes after core integration`

### Suyash tasks-
- Curate Chennai/IIT Madras source-backed contacts:
  - Hospitals and trauma-capable facilities.
  - Police stations.
  - Ambulance or official emergency fallbacks.
  - Tow or roadside support contacts only if source-backed.
  - Repair/puncture contacts only if reliable and useful.
- For every contact, capture:
  - Source name.
  - Source URL.
  - Verification date.
  - Coordinates.
  - Phone.
  - Service type.
  - Confidence reasons.
- Build SQLite generation:
  - Seed JSON to SQLite.
  - Repeatable command.
  - Versioned cache package output.
- Implement backend routes:
  - `POST /api/nearby-services`
  - `GET /api/cache-package`
  - `POST /api/incident-summary`
- Implement fallback behavior:
  - National emergency fallback when local results are weak.
  - Expand-radius guidance when no nearby service is found.
  - Clear response when coordinates are invalid.
- Add tests:
  - Schema validation.
  - Distance sorting.
  - Confidence scoring.
  - Dedupe.
  - Empty dataset fallback.
  - Invalid coordinates.
- Create PR when:
  - Chennai data returns useful ranked results for IIT Madras coordinates.
  - Backend endpoints satisfy the API examples.
  - Tests pass.
  - Data-source notes are complete.
- Suggested PR title:
  - `Implement source-backed Chennai rescue data and core APIs`

### Sidhesh tasks-
- Connect frontend to backend:
  - Call `/api/nearby-services`.
  - Render ranked contacts.
  - Render fallback contacts separately.
  - Show loading, error, offline, and empty states.
- Build emergency interaction flow:
  - Detect location.
  - Manual location fallback.
  - Service filters for hospital, ambulance, police, tow, repair.
  - One-tap call links.
  - Copy/share incident packet.
  - Show nearest landmark field.
- Build offline layer:
  - Cache package fetch.
  - Local fallback when backend is unavailable.
  - Stale cache indicator.
  - Offline mode test instructions.
- Build trust UI:
  - Source badge.
  - Confidence score.
  - Last verified date.
  - Ranking reasons.
  - Location confidence ribbon.
- Add frontend tests or documented manual checks:
  - GPS allowed.
  - GPS denied.
  - Offline after first load.
  - No nearby services.
  - Mobile viewport.
- Create PR when:
  - The emergency flow works against backend or a contract-compatible mock.
  - Offline Chennai cache can render contacts.
  - UI remains usable on phone-sized screens.
  - Trust metadata is visible on each contact.
- Suggested PR title:
  - `Connect PWA emergency flow to RoadSoS APIs`

### Merge 2 PR order-
1. Suyash PR: data and backend APIs.
2. Sidhesh PR: connected PWA and offline flow.
3. Roopal PR if docs/demo assumptions changed.

### Merge 2 acceptance gate-
- Online IIT Madras demo works.
- Offline cached demo works after first load or bundled cache.
- Incident packet can be generated.
- Contacts show trust metadata.
- Assistant is still allowed to be minimal, but must not hallucinate.

## Merge 3: Judge-dopamine differentiators-

### Goal-
Add the memorable features that make judges feel this is a serious emergency system, not a chatbot wrapper.

### Roopal tasks-
- Turn the demo into a staged 30-60 second judge sequence:
  - Start at IIT Madras coordinates.
  - Trigger accident scenario.
  - Show ranked contacts.
  - Switch offline.
  - Show cache still works.
  - Generate incident packet.
  - Ask assistant for an unavailable contact and show refusal.
- Draft the 7-slide story:
  - Welcome.
  - Golden-hour pain.
  - RoadSoS flow.
  - Architecture.
  - Reliability proof.
  - Innovation and scalability.
  - Thank you.
- Write final PR review criteria:
  - Does this impress without making unsafe claims?
  - Can it be demoed repeatedly?
  - Is the feature explainable in one sentence?
  - Does it improve the official evaluation criteria?
- Create PR when:
  - The deck outline and demo script match actual implemented features.
  - Review checklist includes final hackathon scoring proxy.
  - Submission assumptions are up to date.
- Suggested PR title:
  - `Prepare judge demo narrative and submission draft`

### Suyash tasks-
- Add second-region portability sample:
  - Use the same schema.
  - Add local emergency fallback.
  - Include at least 3-5 source-backed sample contacts if feasible.
  - If full contacts are not reliable, include fallback-only region profile and document limitation.
- Add trust ledger data:
  - `confidence_reasons`.
  - `ranking_reasons`.
  - `source_type`.
  - `data_freshness_days`.
- Improve ranking:
  - Distance score.
  - Service-priority score.
  - Confidence score.
  - Freshness score.
  - Availability score.
- Add chaos-case tests:
  - Local contacts missing.
  - Duplicate phone numbers.
  - Stale contact.
  - Contact with missing coordinates.
  - Country fallback only.
- Create PR when:
  - Second-region proof is data-driven.
  - Ranking reasons are returned by API.
  - Chaos-case tests pass.
  - Data-source docs clearly separate production data, fixtures, and assumptions.
- Suggested PR title:
  - `Add trust ledger ranking and portability sample`

### Sidhesh tasks-
- Implement judge-dopamine product features:
  - 10-second rescue drill timer.
  - Offline rescue pack screen.
  - Trust ledger expandable contact details.
  - No-hallucination flight recorder in assistant panel.
  - Ambulance-ready incident packet preview.
  - Bystander mode cards.
  - Location confidence ribbon.
  - Chaos-mode demo toggle for rehearsals.
- Assistant UI:
  - Show retrieved source IDs.
  - Show template IDs.
  - Show refusal reason for unsupported requests.
  - Keep emergency contacts outside the generative layer.
- Polish:
  - Large touch targets.
  - Strong focus states.
  - Accessible contrast.
  - Clear empty states.
  - No overlapping text at mobile widths.
- Create PR when:
  - At least 4 judge-dopamine features are implemented and demoable.
  - Offline, GPS denied, and no-result cases are visually polished.
  - Assistant UI proves it is guarded.
  - Screenshots or a short screen recording are attached to PR.
- Suggested PR title:
  - `Add offline rescue pack and trust-first demo features`

### Merge 3 PR order-
1. Suyash PR: trust/ranking/portability data.
2. Sidhesh PR: judge-dopamine UX.
3. Roopal PR: demo script and deck draft.

### Merge 3 acceptance gate-
- Judges can see innovation within 30 seconds.
- The app works in at least one realistic failure mode.
- Trust metadata is visible without reading source code.
- Cross-region claim is backed by data structure and sample data.
- No feature creates a medical, legal, or dispatch guarantee.

## Merge 4: Final integration and submission freeze-

### Goal-
Stop feature work, stabilize the demo, and produce the Stage 1 submission assets.

### Roopal tasks-
- Create final branch:
  - `codex/final-roadsos-submission`
- Pull latest `main`.
- Run final review across:
  - App behavior.
  - Backend responses.
  - Data-source notes.
  - README.
  - 7-slide deck.
  - Package/assumptions document.
  - Demo script.
- Check final submission list:
  - Code.
  - 7-slide presentation with Welcome and Thank You.
  - Complete code details.
  - Software packages.
  - Assumptions document.
  - Dataset/source documentation.
- Create PR when:
  - Online demo passes.
  - Offline demo passes.
  - GPS denied path passes.
  - No nearby contact path passes.
  - Assistant refusal path passes.
  - Submission docs are complete.
- Suggested PR title:
  - `Finalize RoadSoS hackathon submission`

### Suyash tasks-
- Final reliability pass:
  - Re-run data validation.
  - Re-run backend tests.
  - Verify source URLs open.
  - Verify no fixture data leaks into production cache.
  - Verify fallback contacts are official and documented.
  - Freeze dataset version.
- Support final PR by commenting:
  - Dataset version.
  - Number of production contacts.
  - Number of fallback contacts.
  - Test command output.
  - Known data limitations.

### Sidhesh tasks-
- Final UX pass:
  - Run desktop and mobile viewport checks.
  - Run offline browser check.
  - Capture screenshots for deck.
  - Verify no text overlaps.
  - Verify call/share buttons are discoverable.
  - Verify the 10-second flow is realistic.
  - Freeze UI feature set.
- Support final PR by commenting:
  - Frontend test/manual check results.
  - Screenshots.
  - Offline verification.
  - Known UI limitations.

### Merge 4 PR order-
1. Suyash final reliability comment or patch PR if needed.
2. Sidhesh final UX comment or patch PR if needed.
3. Roopal final integration PR.

### Merge 4 acceptance gate-
- Feature freeze is respected.
- Submission assets are complete.
- Demo is repeatable.
- README explains setup without hidden knowledge.
- Known limitations are honest and not disqualifying.

## Review checklist for Roopal-
- Does the PR improve RoadSoS evaluation criteria?
- Is any emergency contact invented, unsourced, stale, or unclear?
- Are source URLs and verification dates present?
- Are contracts updated when request/response shapes change?
- Does the backend fail safely?
- Does the frontend still work in mobile viewport?
- Does offline mode still work?
- Are screenshots/API examples included where useful?
- Are tests or manual checks included?
- Is the PR small enough to merge without blocking the other branch?
- Does the change make the judge demo stronger?

## Definition of done-
- A first-time user can open the app and understand the emergency action within 3 seconds.
- A bystander can reach ranked help from IIT Madras coordinates in under 10 seconds.
- Offline mode returns useful cached emergency guidance.
- The app never fabricates contacts.
- The assistant refuses unsupported emergency/contact claims.
- Every contact has source and confidence metadata.
- At least one second-region sample proves portability.
- The final deck tells the story clearly.
- The assumptions document is honest about limits.
- The repository is ready for Unstop submission before May 31, 2026, 11:59 PM IST.

