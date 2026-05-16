# PR Review Checklist

Use this checklist before merging any RoadSoS branch into `main`.

## Scope

- The PR supports the RoadSoS accident emergency workflow.
- The PR does not drift into DriveLegal or RoadWatch features.
- The first screen remains emergency-first.

## Safety

- No AI-generated emergency contacts are added to production data.
- Every production contact has source URL, source name, verification date, and confidence reasons.
- The assistant does not invent contacts, dispatch status, medical advice, or legal claims.
- Fallback guidance is clearly marked as fallback guidance.

## Contracts

- Contract changes are documented in the PR description.
- API examples still match frontend expectations.
- Data fields still match `contracts/contact.schema.json`.

## Offline

- Offline behavior is preserved or improved.
- Cached data has a visible version or freshness indicator.
- Stale or missing cache states are handled clearly.

## Verification

- Tests or manual checks are listed in the PR.
- Mobile viewport is checked for frontend changes.
- Backend endpoint examples are included for backend changes.
- Data validation is included for data changes.

## Demo value

- The change strengthens the golden demo.
- The change can be explained to judges in one sentence.
- Any limitation is documented honestly.

