# Hidden Cache & MDM Capabilities

## Hidden Deleted-Photo / Face Unlock Caches

- iOS: PhotoData/Thumbnails Spotlight cache of previously deleted photos.
- Android: Face Unlock / front-camera system caches outside Gallery.

Read-only. Grade moderate/weak. Never claim an app read the cache.

## Hidden MDM / Rogue Certificate / VPN

- Configuration profiles with MDM payloads (especially pre-activation).
- Rogue root certificates.
- Always-on / hidden VPN tunnels to unexpected domains.

Grade strong for MDM + rogue cert + always-on VPN. Never resolve indicator domains.
