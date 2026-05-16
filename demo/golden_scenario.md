# Golden Demo Scenario

## Scenario

A bystander near IIT Madras sees a road accident and needs reliable emergency help fast.

## Demo beats

1. Open RoadSoS on a phone-sized viewport.
2. Use current location or the IIT Madras test coordinates.
3. Show ranked nearby emergency contacts.
4. Expand a contact to show source, verification date, confidence score, and ranking reasons.
5. Generate the ambulance-ready incident packet.
6. Switch to offline mode or simulate network failure.
7. Show the offline rescue pack still has useful fallback guidance.
8. Ask the assistant for an unavailable contact.
9. Show that the assistant refuses to invent data.

## Pass criteria

- Location to ranked help is under 10 seconds in the polished demo.
- Offline path still returns fallback guidance.
- Trust metadata is visible.
- No invented emergency contact appears.
- The demo can be repeated without manual database edits.

