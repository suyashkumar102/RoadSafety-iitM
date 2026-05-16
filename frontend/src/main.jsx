import React from "react";
import { createRoot } from "react-dom/client";
import { Activity, MapPin, Phone, ShieldCheck, WifiOff } from "lucide-react";
import "./styles.css";

const mockContacts = [
  {
    id: "bootstrap-fallback",
    name: "Official emergency fallback",
    type: "fallback_emergency",
    phone: "112",
    distance: "National",
    confidence: "Official",
    source: "ERSS",
    verified: "2026-05-16",
  },
];

function App() {
  return (
    <main className="app-shell">
      <section className="emergency-panel" aria-labelledby="app-title">
        <div className="status-row">
          <span className="status-pill">
            <ShieldCheck size={16} aria-hidden="true" />
            Source-backed mode
          </span>
          <span className="status-pill">
            <WifiOff size={16} aria-hidden="true" />
            Offline-ready scaffold
          </span>
        </div>

        <div className="hero-copy">
          <p className="eyebrow">RoadSoS</p>
          <h1 id="app-title">Find trusted accident help fast.</h1>
          <p>
            Emergency-first PWA scaffold for location, ranked contacts, source trust,
            and incident handoff.
          </p>
        </div>

        <div className="action-grid" aria-label="Emergency actions">
          <button className="primary-action" type="button">
            <MapPin size={22} aria-hidden="true" />
            Use my location
          </button>
          <button className="secondary-action" type="button">
            <Activity size={22} aria-hidden="true" />
            Enter location
          </button>
        </div>

        <section className="contact-list" aria-label="Emergency contacts">
          {mockContacts.map((contact) => (
            <article className="contact-card" key={contact.id}>
              <div>
                <p className="contact-type">{contact.type.replace("_", " ")}</p>
                <h2>{contact.name}</h2>
                <p className="contact-meta">
                  {contact.distance} | {contact.source} | verified {contact.verified}
                </p>
              </div>
              <a className="call-button" href={`tel:${contact.phone}`}>
                <Phone size={18} aria-hidden="true" />
                Call {contact.phone}
              </a>
            </article>
          ))}
        </section>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);

