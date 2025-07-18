// centrex-graphql/frontend/src/utils/auth.ts
const TOKEN_KEY = 'centrex_token';

export async function login(username: string, password: string): Promise<string | null> {
  const query = `mutation Login($username: String!, $password: String!) {\n  login(username: $username, password: $password)\n}`;
  const res = await fetch('http://localhost:8000/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables: { username, password } }),
  });
  const json = await res.json();
  const token = json.data?.login as string | null;
  if (token) {
    localStorage.setItem(TOKEN_KEY, token);
  }
  return token;
}

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

export function clearToken() {
  localStorage.removeItem(TOKEN_KEY);
}
