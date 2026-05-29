---
description: "Riggg's open-source OBS Studio scene collection template for real-time podcast, webinar, and livestream production. 157 scenes, 5-participant capacity, simultaneous horizontal + vertical output."
---

# OBS Scene Collection Template

**Stage:** Produce  
**Score:** 5  
**Evidence:** Internal production data (500+ sessions produced)

<a href="../../assets/downloads/riggg-obs-scene-collection-v1.json" download class="md-button">Download Template (JSON)</a>

## What It Is

A production-ready OBS Studio scene collection built for real-time podcast, webinar, and livestream production. This is the template Riggg uses to produce broadcast-quality shows with lower thirds, transitions, multi-camera layouts, simultaneous horizontal + vertical output, ad breaks, deliverable generation, and up to 5 participants — all in real time during the recording session.

This is not a basic OBS layout. It is a complete production system.

## Why It Matters

Traditional podcast production is post-production heavy: record raw, send to an editor, wait days, get assets back. This template enables **real-time production** — the show is produced live with broadcast-quality graphics, transitions, and layouts during the recording session itself. That is the core of Riggg's production speed advantage.

## Template Architecture

### Resolution & Output

| Output | Resolution | Purpose |
|---|---|---|
| **Horizontal (primary)** | 1920×1080 | Main 16:9 output for YouTube, website, podcast video |
| **Vertical (Aitum canvas)** | 1080×1920 | Simultaneous 9:16 output for Reels, Shorts, TikTok, vertical livestream |

Both outputs render simultaneously during the session. No post-production reformatting needed.

### Scene Categories (157 scenes)

The template organizes scenes into functional categories using a `zzz` prefix separator system for clean navigation in OBS.

#### Show Flow Scenes

| Category | Scenes | Purpose |
|---|---|---|
| **Intro** | 4 | Countdown timer, intro video, participant introduction with animated camera box, example/template |
| **1-Up** | 5 | Full-screen single speaker — one scene per participant slot |
| **2-Up** | 1 | Side-by-side equal layout for host + guest |
| **3-Up** | 3 | Three speakers with active speaker emphasis (active speaker gets larger frame) |
| **4-Up** | 5 | Four speakers — equal grid + active speaker variants per participant |
| **5-Up** | 5 | Five speakers with active speaker emphasis per participant |
| **Screen Share** | 4 | Screen share layouts for 2, 3, 4, or 5 participants with shared screen |
| **Outro** | 1 | End card with branding, listen-on logos, and call to action |
| **Ads** | 3 | Top roll, mid roll, post roll — with waveform visualizers and branded cards |

#### Participant Asset Scenes

Each participant (up to 5) gets a full set of individually configurable assets:

| Category | Per Participant | Total | Purpose |
|---|---|---|---|
| **Names** | 1 | 5 | Participant name text (white, styled) |
| **Titles** | 1 | 5 | Job title / credential text |
| **Logos** | 1 | 5 | Company/personal logo image |
| **Lower Thirds** | 1 | 5 | Branded name + title overlay with gradient accent |
| **Headshots** | 1 | 5 | Static headshot image |
| **Headshot Designs** | 1 | 5 | Circle-cropped headshot with styling |
| **Camera Backgrounds** | 1 | 5 | Per-participant camera box background customization |

#### Camera Box System

The template includes **6 camera box shape variants**, each with raw (`#`) and production (`!`) versions per participant:

| Shape | Scenes | Use Case |
|---|---|---|
| **Circle** | 10 | Headshot-style framing, intro sequences |
| **Rectangle (horizontal)** | 10 | Standard 16:9 camera framing |
| **Rectangle (vertical)** | 10 | Portrait/vertical camera framing |
| **Square (true)** | 10 | 1:1 framing for social-ready output |
| **Square (wide)** | 10 | Slightly wider square for 2-up vertical layouts |
| **Square (4-up)** | 10 | Sized specifically for 4-participant grid layouts |

Each camera box has:

- Raw version (`#CamBox_...`) — unprocessed camera feed for reference
- Production version (`!CamBox_..._Production`) — styled with masks, strokes, shadows, and move transitions

#### Deliverable Scenes

| Scene | Purpose |
|---|---|
| **Quote Graphic** | Generate quote graphics during the session using live text + design elements |
| **Quote Toggler** | Switch between multiple quote text slots |
| **Episode Thumbnail (Horizontal)** | 16:9 thumbnail with participant headshots and branding |
| **Episode Thumbnail (Square)** | 1:1 thumbnail for podcast apps |

#### Global Design Setup

21 scenes for configuring the show's visual identity:

| Scene | Purpose |
|---|---|
| **Background Colors** | Green, blue, red, white background options |
| **Logo Overlay** | Show logo positioning |
| **Client Logos** | Light and dark variants of client/show logo |
| **Intro/Outro Video** | Video file sources for show open and close |
| **Audio Rolls** | Top, mid, post roll audio sources |
| **Color Palette** | 6 configurable brand color sources |
| **Stroke Gradients** | Per-participant gradient accents for camera box strokes |
| **Listen-On Logos** | Apple, Spotify, Amazon Music, YouTube Music |
| **Countdown Module** | Pre-show countdown timer |
| **Produced by Riggg** | Riggg branding module |
| **Guide Overlays** | Safe zone guides and subtitle positioning guides |

### Naming Convention

The template uses a prefix system for source organization:

| Prefix | Meaning | Example |
|---|---|---|
| `#` | Raw camera box (unprocessed) | `#CamBox_Square_1_Participant1` |
| `!` | Production camera box (styled) | `!CamBox_Square_1_Participant1_Production` |
| `*` | Participant asset (headshot, lower third, name) | `*LowerThirds_Participant2_White` |
| `@` | Setup/config source (design, toggler, browser) | `@Setup_Design_Colors` |
| `^` | Group (bundled sources) | `^ToggleGroup_2UP_Left` |
| `$` | Deliverable scene | `$Deliverables_Quote Graphic` |
| `zzz...` | Category separator (sorts to bottom in OBS) | `zzzzzz_R0S Intro` |

### Toggle Group System

Smart groups enable one-click switching between active participants:

| Group | Purpose | Slots |
|---|---|---|
| `^ToggleGroup_HostIntro` | Switch which participant appears in the intro camera box | 5 |
| `^ToggleGroup_2UP_Left` | Switch the left participant in 2-up layout | 5 |
| `^ToggleGroup_2UP_Right` | Switch the right participant in 2-up layout | 5 |
| `^ToggleGroup_Vertical2UP_Top` | Switch top participant in vertical 2-up | 5 |
| `^ToggleGroup_Vertical2UP_Bottom` | Switch bottom participant in vertical 2-up | 5 |
| `^ToggleGroup_WhoSaidIt_Headshots` | Switch which headshot shows in "who said it" overlay | 3 |
| `^ToggleGroup_WhoSaidIt_LowerThirds` | Switch which lower third shows | 3 |

### Subtitle System

Dual subtitle rendering for both horizontal and vertical output:

| Variant | Canvas | Components |
|---|---|---|
| **Horizontal Black** | 1920×1080 | Main text + highlight text overlay |
| **Horizontal White** | 1920×1080 | Main text + highlight text overlay |
| **Vertical Black** | 1080×1920 | Main text + highlight text + color pop background |
| **Vertical White** | 1080×1920 | Main text + highlight text + color pop background |

Each subtitle group includes a highlight text source for emphasizing key words with a different color — matching the style used by major shows like The Diary Of A CEO.

### Transition System

| Transition | Duration | Use |
|---|---|---|
| **Fade** (default) | 600ms | Scene-to-scene transitions |
| **Move Transition** | 600ms | Camera box show/hide animations (slide in/out) |
| **Slide** | Configurable | Available for directional transitions |

Production camera boxes use Move Transition on both show and hide, creating smooth animated entrances and exits when switching between participants.

## Required Plugins

All plugins must be installed before importing the scene collection.

| Plugin | Required For | Download |
|---|---|---|
| **Move Transition** | Animated camera box transitions (core) | [GitHub](https://github.com/exeldro/obs-move-transition) |
| **Vertical Canvas** | Simultaneous 9:16 vertical output | [GitHub](https://github.com/Aitum/obs-vertical-canvas) |
| **advanced-scene-switcher** | Macro automation for production workflows | [GitHub](https://github.com/WarmUpTill/SceneSwitcher) |
| **Source Copy** | Efficient source duplication across scenes | [GitHub](https://github.com/exeldro/obs-source-copy) |
| **Source Dock** | Pin sources to docks for fast control | [GitHub](https://github.com/exeldro/obs-source-dock) |
| **Source Switcher** | Automated source switching | [GitHub](https://github.com/exeldro/obs-source-switcher) |
| **Gradient Source** | Gradient color sources for lower thirds/accents | [GitHub](https://github.com/exeldro/obs-gradient-source) |
| **obs-advanced-masks** | Circle/shape masks for camera boxes | [GitHub](https://github.com/FiniteSingularity/obs-advanced-masks) |
| **obs-stroke-glow-shadow** | Stroke, glow, and shadow effects on sources | [GitHub](https://github.com/FiniteSingularity/obs-stroke-glow-shadow) |
| **phandasm_waveform** | Audio waveform visualizers for ad breaks | [GitHub](https://github.com/phandasm/waveform) |
| **svg-source** | SVG rendering for scalable design elements | [GitHub](https://github.com/exeldro/obs-svg-source) |
| **markdown** | Markdown-rendered text sources | [GitHub](https://github.com/exeldro/obs-markdown) |
| **Stream Deck** | Hardware controller integration | [Elgato](https://www.elgato.com/stream-deck) |
| **Logitech G Plugin** | Logitech Stream Deck variant support | [Logitech](https://www.logitechg.com/) |
| **Quick Access Dock** | Quick access UI panels | [GitHub](https://github.com/exeldro/obs-quick-access-dock) |

### Required Script

| Script | Required For | Install Location |
|---|---|---|
| **source-toggler.lua** | Toggle group switching — enables one-click participant swapping in toggle groups. Without this script, the `^ToggleGroup_` system does not function. | OBS → Tools → Scripts → Add `source-toggler.lua` |

!!! warning "Critical Dependency"
    The template will not work correctly without `source-toggler.lua`. The toggle groups (`^ToggleGroup_HostIntro`, `^ToggleGroup_2UP_Left/Right`, `^ToggleGroup_Vertical2UP_Top/Bottom`, `^ToggleGroup_WhoSaidIt_*`) all depend on this script to ensure only one participant source is visible at a time within each group. Without it, you must manually show/hide sources — defeating the real-time production workflow.

### Install Order

1. Install all 15 plugins before importing the scene collection
2. Restart OBS after plugin installation
3. Add `source-toggler.lua` via Tools → Scripts → Add Script
4. Restart OBS again
5. Import the scene collection via Scene Collection → Import
6. Verify all sources load without errors (no yellow warning triangles)
7. Configure participant camera sources (browser sources for remote, or local capture devices)

## Setup Workflow

### Step 1: Import and Verify

1. Download the scene collection JSON
2. In OBS: Scene Collection → Import → select the JSON file
3. Verify no missing sources (yellow warning triangles)
4. If sources show warnings, confirm all plugins are installed and restart OBS

### Step 2: Configure Brand Identity

Update these Global Design Setup scenes for your show:

1. **@Setup_Design_Colors** — Set your 6 brand colors (Color 1-6)
2. **@Setup_Design_Logo_Client_Light / Dark** — Replace with your show logo
3. **@Setup_Video_Intro / Outro** — Replace with your intro/outro video files
4. **@Setup_Audio_TopRoll / MidRoll / PostRoll** — Replace with your ad break audio
5. **@Setup_Design_StrokeGradients** — Configure camera box gradient accents

### Step 3: Configure Participants

For each participant (1-5):

1. Set up their camera source (browser source URL for remote guests, or local capture)
2. Update `@Text_ParticipantX_White` with their name
3. Update `@Text_ParticipantX_Title` with their job title
4. Replace `@Logo_ParticipantX` with their company logo
5. Replace `*Headshot_ParticipantX` with their headshot image

### Step 4: Configure Vertical Output

1. Open the Aitum Vertical Canvas panel
2. Verify the vertical canvas is rendering at 1080×1920
3. Confirm subtitle groups are positioned correctly in the vertical canvas

### Step 5: Production

Use the show flow scenes in order:

1. **R0S_Intro_Start** — Countdown + pre-show hold
2. **R0S_Intro_Intro** — Show intro video
3. **R0S_Intro_ParticipantX** — Participant introduction with animated camera box
4. **R0S_Interview_1UP / 2UP / 3UP / 4UP / 5UP** — Main interview layouts
5. **R0S_Special_ScreenShare** — When participants share screens
6. **R0S_Ads_TopRoll / MidRoll / PostRoll** — Ad breaks
7. **R0S_Outro_End** — Show close

## Quality Bar

- All 5 participant slots should be configured even if not all are used (prevents scene errors)
- Camera box transitions should be verified before going live
- Subtitle positioning should be tested on both horizontal and vertical canvases
- Brand colors should be set before first use — they propagate through the entire template
- Test the full show flow (intro → interview → ads → outro) before the first live session

## When Not To Use

- Solo audio-only podcasts with no video component
- Shows with more than 5 simultaneous participants (template caps at 5)
- Productions that require 4K output (template is built for 1080p)

## Platform Constraints

| Constraint | Value |
|---|---|
| OBS Version | 30.0+ recommended |
| Primary Resolution | 1920×1080 (16:9) |
| Vertical Resolution | 1080×1920 (9:16) via Aitum Vertical Canvas |
| Max Participants | 5 simultaneous |
| Scene Count | 157 |
| Source Count | 317 |
| File Size | ~2.3 MB (JSON) |
| Plugin Dependencies | 15 plugins required |
