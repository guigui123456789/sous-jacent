// Reçoit le retour de GitHub, échange le code contre un jeton,
// et le transmet à l'éditeur ouvert dans la fenêtre parente.
function page(status, payload) {
  const message = `authorization:github:${status}:${JSON.stringify(payload)}`;
  return `<!doctype html><meta charset="utf-8"><title>Connexion…</title>
<body style="font-family:system-ui;padding:2rem">Connexion en cours…
<script>
(function () {
  function envoyer(e) {
    if (!window.opener) return;
    window.opener.postMessage(${JSON.stringify(message)}, e && e.origin ? e.origin : '*');
  }
  window.addEventListener('message', envoyer, false);
  if (window.opener) {
    window.opener.postMessage('authorizing:github', '*');
  } else {
    document.body.textContent = "Ouvre cette page depuis l'éditeur /admin.";
  }
})();
</script></body>`;
}

export default async function handler(req, res) {
  const url = new URL(req.url, 'https://localhost');
  const code = url.searchParams.get('code');
  const state = url.searchParams.get('state');
  const attendu = (req.headers.cookie || '')
    .split(';')
    .map((c) => c.trim())
    .find((c) => c.startsWith('sj_oauth_state='));

  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Set-Cookie', 'sj_oauth_state=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0');

  if (!code || !state || !attendu || attendu.split('=')[1] !== state) {
    res.status(400).send(page('error', { message: "Requête de connexion invalide. Réessaie depuis /admin." }));
    return;
  }

  try {
    const r = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({
        client_id: process.env.GITHUB_CLIENT_ID,
        client_secret: process.env.GITHUB_CLIENT_SECRET,
        code,
      }),
    });
    const data = await r.json();
    if (!data.access_token) {
      res.status(401).send(page('error', { message: data.error_description || 'GitHub a refusé la connexion.' }));
      return;
    }
    res.status(200).send(page('success', { token: data.access_token, provider: 'github' }));
  } catch (e) {
    res.status(500).send(page('error', { message: 'Échec du dialogue avec GitHub.' }));
  }
}
