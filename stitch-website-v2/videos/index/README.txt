FOLDER: videos/index/
PURPOSE: Background video loop for the homepage hero section.
         Plays silently behind the headline — adds life without distraction.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT YOU NEED TO DROP IN HERE (1 file):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  hero-loop.mp4
  → Factory b-roll — sewing machines running, hands on material,
    bags being assembled, or a slow walk through the production floor.
  → Plays on loop, muted, no controls visible.
  → The headline text sits on top — avoid fast cuts or bright flashes.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPECS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Format:       MP4 (H.264)
  Resolution:   1920×1080 minimum (3840×2160 / 4K is fine too)
  Duration:     10–30 seconds (it loops, so shorter is better for load time)
  File size:    Keep under 15MB if possible — compress before dropping in
  Audio:        Remove or mute — it will never play sound on the site
  Colour:       Dark or moody preferred — the hero text is light-coloured
                and needs legible contrast. I'll add a dark overlay in CSS
                if needed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT I CAN DO AUTOMATICALLY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Once hero-loop.mp4 is in this folder, tell me and I'll:
  - Wire it into the hero section as a background <video> element
  - Add a dark overlay so headline text stays readable
  - Set it to autoplay, loop, muted, playsinline (standard for background video)
  - Keep the ripstop pattern as fallback for slow connections

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPRESSION TIP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  If the raw file is large, drop it in anyway and I can run FFmpeg
  to compress it to a web-safe size without needing any additional software.
  Just say "compress the hero video" and I'll handle it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OPTIONAL — WEBM VERSION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A hero-loop.webm alongside the .mp4 improves loading on Chrome.
  Don't worry about creating this manually — I can convert it for you
  using FFmpeg once you have the MP4.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CURRENT STATE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  The hero currently uses the ripstop grid pattern as a static background.
  The video is optional but high-impact — it's the first thing visitors see.
  Priority: medium — do the work card images first.
