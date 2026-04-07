# Power Agency — Landing Page

## Panoramica progetto
Power Agency è un'agenzia di 3 persone focalizzata su tre verticali di business:
- **E-Commerce**: costruzione e scaling di store online, software e automazioni per e-com
- **Prop Firm Hedging**: strategie di hedging su prop firm, software proprietario, formazione
- **AI**: sviluppo di siti web, automazioni e software custom con intelligenza artificiale

**Obiettivo della landing**: presentare i 3 business con 3 angle ciascuno:
1. Vendita del software proprietario legato a quel verticale
2. Consulenza e formazione (percorso 1:1 o corso)
3. Collaborazione diretta con il team Power Agency

---

## Stack tecnico
- **Singolo file** `index.html` — tutto il sito in un file
- **Tailwind CSS** via CDN (`https://cdn.tailwindcss.com`)
- **GSAP** + **ScrollTrigger** via CDN per animazioni avanzate
- **Vanilla JS** per: language switcher, tab business, accordion FAQ, hamburger menu
- **Google Fonts**: Inter (400, 600, 700)
- Hostabile su Netlify / Vercel / GitHub Pages senza build step

---

## Design System

| Token | Valore |
|-------|--------|
| Background principale | `#0a0a0a` |
| Background card | `#141414` / `#1a1a1a` |
| Bordi | `#2a2a2a` |
| Accento gold | `#f0b429` |
| Accento indigo (AI) | `#6366f1` |
| Accento verde (E-Com) | `#22c55e` |
| Accento viola (Prop) | `#a855f7` |
| Testo principale | `#f5f5f5` |
| Testo secondario | `#a3a3a3` |
| Font | Inter, sans-serif |

**Stile**: dark/tech, minimal, premium. Bordi sottili `#2a2a2a`, cards con backdrop leggermente più chiaro dello sfondo, accenti gold come colore brand principale.

---

## Lingua — Sistema Bilingue IT/EN

Ogni elemento di testo ha due attributi:
```html
<span data-it="Testo italiano" data-en="English text">Testo italiano</span>
```

Il language switcher JS legge l'attributo e sostituisce il contenuto:
```javascript
function setLang(lang) {
  document.querySelectorAll('[data-it]').forEach(el => {
    el.textContent = el.getAttribute(`data-${lang}`);
  });
  document.documentElement.setAttribute('data-lang', lang);
}
```

Bottone switcher in navbar: `IT | EN` — clic su EN → tutto il testo cambia, clic su IT → torna italiano.

---

## Struttura Sezioni (in ordine nel DOM)

### 1. `<nav>` — Navbar
- **Sinistra**: logo (`<img src="logo.svg" alt="Power Agency">` — placeholder)
- **Centro** (desktop): link ancore → Chi Siamo / Business / Software / Contatti
- **Destra**: language switcher `IT | EN` + CTA "Prenota Call" (link Calendly)
- **Mobile**: hamburger icon → menu slide-down con tutti i link
- Sfondo: `rgba(10,10,10,0.9)` con `backdrop-filter: blur(12px)` — sticky top
- Bordo bottom: `1px solid #2a2a2a`

### 2. `<section id="hero">` — Hero
- **Layout**: full viewport height (`min-h-screen`), flex center
- **Background**: griglia SVG sottile (`stroke="#2a2a2a"`) + gradiente radiale gold al centro
- **Headline** (animata GSAP):
  - IT: `"Costruiamo. Scaliliamo. Collaboriamo."`
  - EN: `"Build. Scale. Partner."`
  - Stile: font-size clamp(3rem, 8vw, 7rem), font-weight 700, colore bianco
  - Animazione: ogni parola entra con `y: 60, opacity: 0` → stagger 0.15s
- **Subheadline**: descrizione 2 righe `[DA_DEFINIRE]`, colore `#a3a3a3`
- **Badge pill**: 3 pill cliccabili → E-Commerce · Prop Firm · AI (bordo gold, sfondo trasparente)
- **CTA**: bottone "Scopri i Business ↓" con pulse animation CSS
- **Parallax**: hero content si muove leggermente allo scroll (GSAP, y: -50 su scroll full page)

### 3. `<section id="about">` — Chi Siamo
- **Titolo sezione**: `"Chi Siamo" / "About Us"`
- **Paragrafo**: descrizione Power Agency [DA_DEFINIRE] — 2-3 righe
- **Card fondatori** (3 card in grid 3-col desktop, 1-col mobile):
  - Avatar: cerchio con immagine placeholder (iniziali su sfondo gold)
  - Nome: [DA_DEFINIRE]
  - Ruolo: [DA_DEFINIRE]
- **Metrics bar** (3 numeri in riga):
  - `3` Verticali di Business
  - `X` Software Attivi → `[DA_DEFINIRE]`
  - `X` Clienti Seguiti → `[DA_DEFINIRE]`
  - Ogni numero: **counter animato** GSAP (0 → N in 2s quando entra in viewport)

### 4. `<section id="business">` — I 3 Business
Struttura ripetuta per E-Commerce, Prop Firm, AI:

```
[Icona + Nome Vertical]
[Tab: Il Software | Consulenza & Formazione | Collabora con Noi]
[Contenuto tab attivo]
```

**Tab content per ogni vertical:**

**E-Commerce** (accento verde `#22c55e`):
- Software: [DA_DEFINIRE] — descrizione + CTA "Acquista / Demo"
- Consulenza: percorso formativo [DA_DEFINIRE] + CTA "Prenota Call"
- Collabora: descrizione partnership [DA_DEFINIRE] + CTA "Parliamone"

**Prop Firm** (accento viola `#a855f7`):
- Software: [DA_DEFINIRE] — descrizione + CTA "Acquista / Demo"
- Consulenza: percorso formativo [DA_DEFINIRE] + CTA "Prenota Call"
- Collabora: descrizione partnership [DA_DEFINIRE] + CTA "Parliamone"

**AI** (accento indigo `#6366f1`):
- Software: [DA_DEFINIRE] — descrizione + CTA "Acquista / Demo"
- Consulenza: percorso formativo [DA_DEFINIRE] + CTA "Prenota Call"
- Collabora: descrizione partnership [DA_DEFINIRE] + CTA "Parliamone"

**Animazione entrata**: card verticale sinistra e destra alternata allo scroll (GSAP ScrollTrigger, `x: ±80, opacity: 0`).

**JS Tab switching**: click su tab → rimuovi `active` da tutti → aggiungi `active` al cliccato → mostra pannello corrispondente.

### 5. `<section id="software">` — I Nostri Software
- **Titolo**: `"I Nostri Strumenti" / "Our Tools"`
- **Sottotitolo**: breve descrizione [DA_DEFINIRE]
- **Grid**: 2 colonne desktop, 1 colonna mobile
- **Card software** (ripetere per ogni prodotto — minimo 3 placeholder):

```
┌─────────────────────────────────┐
│ [Badge: E-Com / Prop / AI]      │
│                                  │
│ [Screenshot / Mockup Placeholder]│
│                                  │
│ Nome Software [DA_DEFINIRE]      │
│ Descrizione 2-3 righe [DA_DEF]  │
│                                  │
│ [Scopri di più →]               │
└─────────────────────────────────┘
```

- **Bordo**: animato allo scroll — linea gold che si "disegna" intorno alla card (CSS clip-path o border animation con GSAP)
- **CTA "Scopri di più →"**: `href="[URL_SOFTWARE_DA_DEFINIRE]"` target `_blank`
- **Hover**: scale(1.02), box-shadow gold sottile

**Placeholder software (da sostituire con dati reali):**
1. Software E-Commerce — nome: `[SW_ECOM_1]` — url: `[URL_SW_ECOM_1]`
2. Software Prop Firm — nome: `[SW_PROP_1]` — url: `[URL_SW_PROP_1]`
3. Software AI — nome: `[SW_AI_1]` — url: `[URL_SW_AI_1]`
_(aggiungere ulteriori software seguendo la stessa struttura)_

### 6. `<section id="proof">` — Social Proof
- **Numeri chiave** (3-4 in riga, counter animato):
  - `[STAT_1]` — label [DA_DEFINIRE]
  - `[STAT_2]` — label [DA_DEFINIRE]
  - `[STAT_3]` — label [DA_DEFINIRE]
- **Testimonianze** (2-3 card):
  - Quote, nome cliente, vertical di riferimento [DA_DEFINIRE]

### 7. `<section id="faq">` — FAQ
- **Accordion**: click su domanda → risposta si espande (smooth con CSS max-height transition)
- **Domande generali** [DA_DEFINIRE]:
  - Come funziona la collaborazione?
  - Posso acquistare solo il software senza consulenza?
  - _(aggiungere domande reali)_
- **Domande per vertical** [DA_DEFINIRE]: 2-3 per E-Com, Prop, AI

### 8. `<section id="contact">` — Contatti
- **Titolo CTA**: `"Pronti a iniziare?" / "Ready to start?"`
- **3 blocchi affiancati** (grid 3-col desktop, stack mobile):

  **WhatsApp**
  - Icona WhatsApp SVG (verde)
  - Label: `"Scrivici su WhatsApp" / "Message us on WhatsApp"`
  - Link: `href="https://wa.me/[URL_WHATSAPP]"`

  **Calendly**
  - Icona calendario
  - Label: `"Prenota una Call" / "Book a Call"`
  - Link: `href="[URL_CALENDLY]"`

  **Form Email**
  - Campi: Nome, Email, Messaggio, Dropdown "Vertical di interesse" (E-Commerce / Prop Firm / AI / Generale)
  - Submit: `action="mailto:[EMAIL_DA_DEFINIRE]"` o integrazione Formspree

### 9. `<footer>` — Footer
- Logo + `© 2025 Power Agency. Tutti i diritti riservati.`
- Link social: Instagram `[URL]` · LinkedIn `[URL]` · _(altri) [DA_DEFINIRE]_
- Link: Privacy Policy (placeholder `href="#"`)

---

## Animazioni — Specifiche GSAP

```javascript
// Al load — Hero
gsap.from(".hero-word", { y: 60, opacity: 0, stagger: 0.15, duration: 0.8, ease: "power3.out" });
gsap.from("nav", { y: -60, opacity: 0, duration: 0.6, ease: "power2.out" });

// ScrollTrigger — pattern base per ogni sezione
gsap.from(".section-fade", {
  scrollTrigger: { trigger: el, start: "top 80%" },
  y: 40, opacity: 0, duration: 0.7, ease: "power2.out"
});

// Stagger cards
gsap.from(".card", {
  scrollTrigger: { trigger: ".cards-container", start: "top 75%" },
  y: 50, opacity: 0, stagger: 0.12, duration: 0.6
});

// Counter animato
gsap.to(counter, {
  scrollTrigger: { trigger: counter, start: "top 80%" },
  innerText: targetValue, duration: 2, snap: { innerText: 1 }
});

// Parallax hero
gsap.to(".hero-content", {
  scrollTrigger: { trigger: "#hero", scrub: true },
  y: -80
});

// Entrata alternata business cards
gsap.from(".business-left", { scrollTrigger: {...}, x: -80, opacity: 0 });
gsap.from(".business-right", { scrollTrigger: {...}, x: 80, opacity: 0 });
```

---

## Placeholder da sostituire (checklist)

- [ ] `[LOGO]` — inserire `logo.svg` o `logo.png` nella root
- [ ] `[NOME_FONDATORE_1/2/3]` — nomi reali dei 3 fondatori
- [ ] `[RUOLO_1/2/3]` — ruoli (es. CEO, CTO, CMO)
- [ ] `[FOTO_1/2/3]` — foto profilo o placeholder iniziali
- [ ] `[SW_ECOM_1..N]` — nomi software e-commerce
- [ ] `[SW_PROP_1..N]` — nomi software prop firm
- [ ] `[SW_AI_1..N]` — nomi software AI
- [ ] `[URL_SW_*]` — URL landing pages dei software
- [ ] `[URL_WHATSAPP]` — numero nel formato internazionale (es. 393331234567)
- [ ] `[URL_CALENDLY]` — link Calendly
- [ ] `[EMAIL_DA_DEFINIRE]` — email per il form contatti
- [ ] `[STAT_1/2/3]` — numeri reali per social proof
- [ ] `[SOCIAL_LINKS]` — URL Instagram, LinkedIn, ecc.
- [ ] `[FAQ_CONTENT]` — domande e risposte reali
- [ ] `[COPY_*]` — testi definitivi per ogni sezione
