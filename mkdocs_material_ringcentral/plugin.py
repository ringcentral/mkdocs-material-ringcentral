"""
mkdocs-ringcentral plugin
=========================
Self-contained RingCentral 2026 brand layer for MkDocs Material.

Bundles everything the site needs so nothing has to live outside this package:
  - templates/main.html  — Jinja2 override (announce banner + RC Labs footer)
  - assets/ringcentral.css — full brand CSS (header gradient, sidebar, dark mode…)
  - assets/ringcentral.js  — ticker + footer JS
  - assets/extra.js        — GitHub Pages → appconnect.labs.ringcentral.com redirect
  - assets/RingCentral_logo_color.png — site logo

What each hook does
-------------------
on_config      Prepends _rc/ringcentral.css and _rc/extra.js to extra_css /
               extra_javascript.  Sets theme.logo to the bundled PNG so
               mkdocs.yml does not need a logo entry.

on_env         Inserts this package's templates/ directory at the front of the
               Jinja2 loader chain, so main.html overrides Material's default
               without requiring custom_dir: overrides in mkdocs.yml.

on_post_build  Copies all bundled assets into <site_dir>/_rc/ and also writes
               the logo to <site_dir>/img/ (the path mkdocs.yml previously used)
               so existing bookmarks / cached HTML keep working.
"""

import os
import shutil

from jinja2 import ChoiceLoader, FileSystemLoader
from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

PLUGIN_DIR    = os.path.dirname(__file__)
ASSETS_DIR    = os.path.join(PLUGIN_DIR, "assets")
TEMPLATES_DIR = os.path.join(PLUGIN_DIR, "templates")

# Assets copied to <site_dir>/_rc/
_RC_ASSETS = [
    "ringcentral.css",
    "ringcentral.js",
    "extra.js",
    "RingCentral_logo_color.png",
]

# Map site_url hostnames → canonical project keys.
# Checked in order; first match wins.
_SITE_URL_MAP = [
    ("appconnect.labs.ringcentral.com",                  "app-connect"),
    ("ringcentral.github.io/ringcentral-embeddable",     "rc-embeddable"),
]


class RingCentralPlugin(BasePlugin):
    """MkDocs plugin that applies the RingCentral brand layer."""

    config_scheme = (
        # Explicit project key — set this in mkdocs.yml under `plugins:
        #   - material-ringcentral:
        #       labs_project: design-system`
        # If omitted the plugin falls back to extra.labs_project, then
        # auto-detects from site_url.
        ("labs_project", config_options.Type(str, default="")),
    )

    # ------------------------------------------------------------------
    # 1. Inject CSS / JS, set the logo, resolve the active Labs project
    # ------------------------------------------------------------------
    def on_config(self, config):
        # Prepend brand CSS (ringcentral.css is the full stylesheet)
        config["extra_css"] = ["_rc/ringcentral.css"] + list(
            config.get("extra_css") or []
        )
        # Prepend both JS files: brand interactions first, redirect second
        config["extra_javascript"] = [
            "_rc/ringcentral.js",
            "_rc/extra.js",
        ] + list(config.get("extra_javascript") or [])

        # Override the logo to use the bundled asset.
        # MkDocs Material's | url filter resolves this relative to each page.
        config["theme"]["logo"] = "_rc/RingCentral_logo_color.png"

        # ---- Resolve the active Labs project key ----------------------
        # Priority: plugin config → extra.labs_project → site_url hostname
        active = (self.config.get("labs_project") or "").strip()

        if not active:
            active = (
                (config.get("extra") or {}).get("labs_project") or ""
            ).strip()

        if not active:
            site_url = (config.get("site_url") or "").lower()
            for hint, key in _SITE_URL_MAP:
                if hint in site_url:
                    active = key
                    break

        # Inject into extra so the Jinja2 template can read it.
        if not config.get("extra"):
            config["extra"] = {}
        config["extra"]["_labs_active_project"] = active

        return config

    # ------------------------------------------------------------------
    # 2. Inject our templates into the Jinja2 loader chain
    # ------------------------------------------------------------------
    def on_env(self, env, config, files):
        """Prepend our templates/ dir so main.html overrides Material's."""
        env.loader = ChoiceLoader([
            FileSystemLoader(TEMPLATES_DIR),
            env.loader,
        ])
        return env

    # ------------------------------------------------------------------
    # 3. Copy all assets into the built site
    # ------------------------------------------------------------------
    def on_post_build(self, config):
        site_dir = config["site_dir"]

        # Primary destination: _rc/
        rc_dest = os.path.join(site_dir, "_rc")
        os.makedirs(rc_dest, exist_ok=True)
        for filename in _RC_ASSETS:
            src = os.path.join(ASSETS_DIR, filename)
            if os.path.isfile(src):
                shutil.copy(src, os.path.join(rc_dest, filename))

        # Also copy the logo to img/ so any hardcoded img/RingCentral_logo_color.png
        # references in existing HTML or cached pages keep resolving.
        img_dest = os.path.join(site_dir, "img")
        os.makedirs(img_dest, exist_ok=True)
        logo_src = os.path.join(ASSETS_DIR, "RingCentral_logo_color.png")
        if os.path.isfile(logo_src):
            shutil.copy(logo_src, os.path.join(img_dest, "RingCentral_logo_color.png"))
