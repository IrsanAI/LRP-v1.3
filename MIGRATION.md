# Migration Guide: pythonlover2023 → IrsanAI/LRP-v1.3

## Ziel
Finale Überführung dieses Repositories in die neue Ziel-Organisation:
- **Target:** `https://github.com/IrsanAI/LRP-v1.3`

## Empfohlene Vorgehensweise

### Option A (bevorzugt): Repository Transfer
Wenn das Quellrepo im alten Account liegt und du Owner-Rechte hast:
1. In GitHub zum Quellrepo gehen → **Settings** → **General**.
2. Ganz unten **Transfer ownership** auswählen.
3. Ziel-Owner `IrsanAI` und Repo-Name `LRP-v1.3` eintragen.
4. Transfer bestätigen.

**Vorteile:**
- Issues, Stars, Watcher, PR-Historie bleiben erhalten.
- Alte URLs werden automatisch umgeleitet.

### Option B: Sauberer Neuaufbau + Push
Wenn du bewusst ein frisches Zielrepo nutzen willst:
```bash
# im lokalen Projekt

git remote rename origin legacy

git remote add origin https://github.com/IrsanAI/LRP-v1.3.git

git push -u origin --all

git push origin --tags
```

## Nach der Migration (Checkliste)
- README-Badges/Links auf neues Repo umstellen.
- GitHub Pages in neuem Repo aktivieren.
- Branch Protection & Collaborator-Rollen setzen.
- Legacy-Repo als Archiv/Redirect kennzeichnen.
