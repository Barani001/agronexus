# AGRONEXUS — Firebase + OTP application

This version turns the static starter into a functional Firebase-backed web application.

## Included
- Firebase Phone OTP authentication with reCAPTCHA
- Farmer / Buyer / FPO profiles
- Role-aware dashboard
- Realtime Database market intelligence
- Buyer reverse marketplace
- Digital crop lots
- Buyer offers and farmer acceptance
- Order + payment-status tracking (status ledger only; no money movement)
- Transparent rules-based selling advisor using market records + estimated logistics
- Admin console for market-data seeding
- Production-oriented Realtime Database Security Rules
- GitHub Pages-friendly static frontend

## 1. Create Firebase project

Open the Firebase Console and create a project. Register a Web app and copy its web configuration.

Enable:
1. Authentication → Sign-in method → Phone
2. Realtime Database → create a database

For Phone Auth on web, Firebase uses reCAPTCHA and requires your deployed domain to be authorized.

## 2. Configure the frontend

Open `frontend/firebase-config.js` and replace the placeholder values with the Web app configuration from Firebase Console.

The Firebase web configuration is client-side configuration, not a database password. Database protection comes from `database.rules.json`.

## 3. Add authorized domains

In Firebase Authentication settings, add:
- `localhost` for local testing if needed
- `barani001.github.io` for the GitHub Pages deployment
- your custom domain if you add one later

## 4. Apply Realtime Database rules

In Firebase Console → Realtime Database → Rules, paste the contents of `database.rules.json` and publish.

Do not use public read/write rules in production.

## 5. First admin

The application intentionally does not let a new client-side user promote itself to admin.

1. Sign in once using OTP.
2. Open Realtime Database → `users`.
3. Find your UID.
4. Change only that user's `role` from `farmer` to `admin`.
5. Refresh AGRONEXUS.

After that, the Admin page can seed the small Maharashtra demo market dataset.

## 6. GitHub Pages layout

For GitHub Pages, publish the repository root. The root `index.html` is the same app as `frontend/index.html` and loads `assets/agronexus-logo.png`.

Recommended root layout:

```
index.html
assets/agronexus-logo.png
firebase-config.js
backend/
frontend/
database.rules.json
firebase.json
README.md
```

## 7. Production data

The included seed data is illustrative. Replace it with validated mandi/market data before presenting live prices as official data. The selling advisor is a transparent rules-based prototype, not a guaranteed price forecast.

## Security notes

- Keep Firebase Realtime Database rules enabled.
- Do not put service-account JSON or Firebase Admin credentials in the frontend repository.
- Consider Firebase App Check and monitoring/rate controls before public launch.
- Phone Auth SMS has Firebase usage limits and abuse protection.

## Firebase configuration

This repository is preconfigured for the AGRONEXUS Firebase Web App. Before production use, enable Phone Authentication, create Realtime Database, publish `database.rules.json`, and add the deployed domain under Firebase Authentication > Settings > Authorized domains.

## GitHub Pages

The deployable frontend entry point is the repository-root `index.html`. In GitHub: Settings > Pages > Deploy from a branch > `main` > `/ (root)`.
