// Enregistre une adresse à la lettre de sous-jacent.
// L'adresse est transmise au service d'envoi ; elle n'est jamais stockée ici.
// Variable à renseigner dans Vercel : BUTTONDOWN_API_KEY.

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).json({ erreur: 'Méthode non autorisée.' });
    return;
  }

  const email = typeof req.body?.email === 'string' ? req.body.email.trim() : '';
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || email.length > 254) {
    res.status(400).json({ erreur: "Cette adresse ne semble pas valide." });
    return;
  }

  const cle = process.env.BUTTONDOWN_API_KEY;
  if (!cle) {
    res.status(503).json({
      erreur: "L'inscription n'est pas encore ouverte. Écrivez à contact@sousjacent.com.",
    });
    return;
  }

  try {
    const r = await fetch('https://api.buttondown.com/v1/subscribers', {
      method: 'POST',
      headers: { Authorization: `Token ${cle}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ email_address: email, type: 'regular' }),
    });

    if (r.ok || r.status === 201) {
      res.status(200).json({ ok: true });
      return;
    }
    if (r.status === 409 || r.status === 400) {
      // déjà inscrit : on ne révèle pas l'état d'une adresse
      res.status(200).json({ ok: true });
      return;
    }
    res.status(502).json({ erreur: "L'inscription n'a pas pu aboutir. Réessayez plus tard." });
  } catch {
    res.status(502).json({ erreur: "L'inscription n'a pas pu aboutir. Réessayez plus tard." });
  }
}
