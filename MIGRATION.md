# Migration Guide: pythonlover2023 → IrsanAI/LRP-v1.3

## Ziel
Finale Überführung dieses Repositories in die neue Ziel-Organisation:
- **Target:** `https://github.com/IrsanAI/LRP-v1.3`

## Empfohlene Vorgehensweise

### Option A (bevorzugt): Repository Transfer
Wenn das Quellrepo im alten Account liegt und du Owner-Rechte hast:
1. In GitHub zum Quellrepo gehen → **Settings** → **General**.
2. Ganz unten **Transfer ownership** auswählen.
3. Im Feld **New owner** nur den Owner eintragen (`IrsanAI`) — **nicht** `IrsanAI/LRP-v1.3`.
4. Im separaten Feld **New repository name** den Zielnamen eintragen (`LRP-v1.3`).
5. Transfer bestätigen.

**Wichtig zur UI-Verwirrung:**
- Bei „Select one of my organizations“ wird nur angezeigt, was im aktuell angemeldeten Account verfügbar/zulässig ist.
- Falls `IrsanAI` nicht per Autovervollständigung erscheint, nutze „Specify an organization or username“ und trage dort **nur** `IrsanAI` ein.
- Die Zuordnung zum Zielrepo passiert über das zweite Feld (**New repository name**), nicht über `owner/repo` im Owner-Feld.
- Falls das Zielrepo `IrsanAI/LRP-v1.3` bereits existiert, kann der Transfer mit genau diesem Namen fehlschlagen. Dann entweder Zielrepo vorab löschen/umbenennen oder Option B verwenden.

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
