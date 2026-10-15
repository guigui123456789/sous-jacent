// Démarre la connexion GitHub pour l'éditeur /admin.
import crypto from 'node:crypto';

export default function handler(req, res) {
  const clientId = process.env.GITHUB_CLIENT_ID;
  if (!clientId) {
    res.status(500).send("GITHUB_CLIENT_ID n'est pas configuré dans Vercel.");
    return;
  }
  const state = crypto.randomBytes(16).toString('hex');
  const host = req.headers['x-forwarded-host'] || req.headers.host;
  const redirectUri = `https://${host}/api/callback`;

  res.setHeader('Set-Cookie', `sj_oauth_state=${state}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=600`);
  res.redirect(
    302,
    'https://github.com/login/oauth/authorize?' +
      new URLSearchParams({ client_id: clientId, redirect_uri: redirectUri, scope: 'repo,user', state })
  );
}
