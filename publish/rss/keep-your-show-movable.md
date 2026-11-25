# Keep Your Show Movable

## What It Is

Keep control of your podcast's feed, accounts and episode identifiers so a change of host or production partner does not become a scramble to rebuild distribution. Start by finding the live RSS feed URL and confirming that someone on your team—not only your partner—can access its hosting account and redirect settings.

This is a readiness check and move runbook for a recorded show's public feed. It connects account access, stable episode identity, working media links and a verified redirect from the old feed to the new one.

## Best For

- Brand and B2B shows produced with an agency, network or outside production team.
- Podcasts preparing to change hosts or leave a bundled publishing service.
- Teams reviewing their publishing setup before renewing a service or handing it to a new producer.

## Why It Works

A feed URL tells apps where to look for episodes; a GUID is the stable identifier used to recognize an episode even when its title or media URL changes. Copying the audio files alone does not preserve that relationship. A redirect points followers toward the new feed, while unchanged identifiers help apps recognize the same episodes rather than treating them as new releases.

Account access matters too. Apple uses a token placed in the feed to verify eligible show claims. Spotify sends its claim-verification code to the email address in the feed; an already-claimed show needs access from its existing administrator. Keep those controls with the show owner rather than discovering an access gap during a move.

For example, a brand moving a 40-episode interview show to a new host should import all 40 episodes, compare their identifiers with the old feed, test playback and then redirect the old feed. It should not submit a second listing and ask existing followers to start again.

## Required Elements

1. **A known feed and exit route.** Record the current RSS URL, who manages it, how to set a 301 redirect and how long the old host will retain that redirect. Save the host's documented instructions. Terms differ: Transistor documents a permanent redirect after cancellation; Buzzsprout recommends keeping the account active for at least three weeks after redirecting. Do not assume cancellation preserves a redirect at every host.

2. **Stable show and episode identifiers.** Compare old and new feeds before switching. Preserve every episode GUID and the existing show-level podcast:guid where present. Do not generate replacement identifiers just because the hosting address changed. If the original feed has no episode GUIDs, ask both hosts how they will preserve identity: Apple may be using the enclosure URL instead, so a routine media-URL change needs special care.

3. **Owner-controlled access.** The show owner should control the hosting account, a monitored feed-contact email and its Apple Podcasts Connect and Spotify for Creators accounts. Give producers invited access where supported. Test access before a handover, including the account-recovery route. Check Apple's show-claiming setting deliberately; some shows, including subscription or channel configurations, need Apple's transfer support rather than the normal claim process.

4. **A short list of media-link dependencies.** An enclosure URL is the address an app uses to fetch an episode's audio. It can pass through third-party measurement prefixes before reaching the file. List each prefix, its purpose and its responsible service. With the host's help, remove obsolete services before their redirects stop working, then test playback. Mark the change in reporting: changing media URLs can trigger re-downloads and produce a temporary download spike, not necessarily new listeners.

5. **Reachable originals.** Keep masters, artwork and existing music licences in a library the show owner can access without the departing partner. Preserve the published episode metadata as well as the media files. The Content Memory Standard covers the wider library; this check confirms the materials needed for this move are actually available.

6. **An ordered move runbook.** Import first, compare the feeds, test the new feed, then have the old host redirect it. Follow the hosts' documented process for itunes:new-feed-url rather than manually editing a managed feed. For self-hosted feeds, Apple specifies a 301 redirect and that tag for at least four weeks. Plan to retain the old account and redirect for at least that four-week window, or longer where the host requires it; confirm what survives cancellation before closing anything. Verify the move before removing access.

7. **A separate route to the audience.** Keep the owned episode page and its listening links current. Know whether the provider hosting the feed also operates a directory: a hosting-account removal can affect distribution beyond that one app. Spotify for Creators documents that a removed show can also come down from external apps it distributed to. An owned page offers a place to explain a change; it does not replace a working feed redirect.

Use this handover note to make the check concrete:

> **Show:** ___; **Current feed:** ___; **Destination feed:** ___
>
> **Owner who tested account access:** ___; **Feed-contact mailbox checked:** ___
>
> **Episode count and GUID comparison:** ___; **Show GUID retained:** ___
>
> **Redirect instructions and retention terms:** ___; **Earliest account-closure date:** ___
>
> **Prefixes and responsible services:** ___; **Master/metadata library:** ___
>
> **Playback, listing and next-release checks assigned to:** ___

Have a person verify these entries against the actual accounts and feeds. A completed worksheet is not proof that the redirect works.

## Quality Bar

- The show owner can sign in to the hosting and directory accounts without the partner's help.
- All expected episodes are present in the new feed; their GUIDs match the old feed, and the show GUID is retained where used.
- The old feed URL redirects to the intended new feed—not to a website page or an error.
- The oldest, newest and a middle episode play from the new feed; the next published episode reaches the existing listings.
- The directory accounts show the intended feed, with no unexpected duplicate listings or episodes.
- Every remaining measurement prefix has a named service and purpose. Playback still works after any removal.
- The old account stays available until the checks pass and the required redirect-retention period is covered.

## When Not To Use

- Do not treat this public-RSS checklist as a complete migration plan for private feeds, paid subscriptions or platform-hosted video. Those need their own access and transfer checks.
- If another organization owns the show, agree who is authorized to move it before changing accounts or feeds.
- Do not switch to self-hosting simply to avoid dependency. Running the feed yourself adds maintenance and security work; a documented, tested exit path may be the better choice.
- If the old feed is already inaccessible, use each directory's recovery process. Updating Apple Podcasts Connect can help Apple followers, but does not establish a redirect for every other app.

## Riggg Score

3

Useful, repeatable preparation, with host-specific transfer rules and verification work. It is not a one-click guarantee of a lossless move.

## Evidence

Evidence level: external-research.

Platform and host documentation establish the mechanics below; they do not measure follower losses or the success rate of this checklist. Sources checked November 25, 2026.

- Apple: [Change the RSS feed URL](https://podcasters.apple.com/support/837-change-the-rss-feed-url) and [Changing hosting providers](https://podcasters.apple.com/support/3965-how-to-change-hosting-providers)—redirects, four-week guidance, consistent metadata and episode GUIDs, plus the fallback when the old feed cannot be accessed.
- Podcasting 2.0: [Show GUID specification](https://podcasting2.org/docs/podcast-namespace/tags/guid)—the show identifier follows the podcast across hosts.
- Apple: [Claim your show](https://podcasters.apple.com/support/5497-claim-your-show) and [Transfer podcast ownership](https://podcasters.apple.com/support/839-transfer-ownership-of-a-podcast); Spotify: [Claiming your podcast](https://support.spotify.com/us/creators/article/claiming-your-podcast-on-spotify-for-creators/)—feed-based verification, account access and exceptions.
- [Transistor redirect-out instructions](https://support.transistor.fm/en/article/how-to-forward-your-transistor-podcast-feed-301-redirect-1r1j8lj/) and [Buzzsprout transfer-away instructions](https://www.buzzsprout.com/help/9-transfer-away-from-buzzsprout)—import order and differing redirect/account-retention terms.
- Podnews: [Chartable's December 2024 switch-off](https://podnews.net/update/chartable-final-switchoff)—a dated warning about playback risk from obsolete prefixes and Spotify re-downloads after URL changes. [RSS.com confirms removing that prefix](https://help.rss.com/en/support/solutions/articles/44002552353-removing-the-chartable-prefix). This is a documented dependency example, not a count of shows that lost playback.
- Spotify: [Show removed or deleted](https://support.spotify.com/us/creators/article/show-removed-or-deleted/)—the connection between hosting-account removal and external distribution.

## Related Patterns

- [RSS Feed Metadata Standard](feed-metadata-standard.md)—the fields inside the feed.
- [Canonical Episode Page](../website/canonical-episode-page.md)—the stable owned page for each episode.
- [Content Memory Standard](../../preserve/vector-memory/content-memory-standard.md)—the wider library of reusable assets and context.
