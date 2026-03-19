"""
MindVault — Personal Knowledge Base AI
Author : Aarnav Kejriwal <aarnkej@gmail.com>
License: MIT
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import anthropic
import os

# ── Load .env if present (pip install python-dotenv) ──────────────────────────
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional; set env vars manually if not installed

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Serve the main UI."""
    return send_from_directory("templates", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Proxy requests to the Anthropic API.
    Accepts JSON body:
      {
        "system":     str,
        "messages":   [{"role": "user"|"assistant", "content": str}, ...],
        "model":      str  (optional, default: claude-sonnet-4-20250514),
        "max_tokens": int  (optional, default: 1000)
      }
    Returns:
      { "content": str }   on success
      { "error":   str }   on failure
    """
    # Allow key override from the browser (session-only, not stored)
    key = request.headers.get("X-Api-Key") or API_KEY
    if not key:
        return jsonify({
            "error": (
                "ANTHROPIC_API_KEY is not set. "
                "See README.md for setup instructions."
            )
        }), 500

    data = request.get_json(force=True)
    system     = data.get("system", "")
    messages   = data.get("messages", [])
    model      = data.get("model", "claude-sonnet-4-20250514")
    max_tokens = int(data.get("max_tokens", 1000))

    try:
        client   = anthropic.Anthropic(api_key=key)
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        text = "".join(
            block.text for block in response.content if hasattr(block, "text")
        )
        return jsonify({"content": text})

    except anthropic.AuthenticationError:
        return jsonify({"error": "Invalid API key — check your ANTHROPIC_API_KEY."}), 401
    except anthropic.RateLimitError:
        return jsonify({"error": "Rate limit reached — please wait a moment and retry."}), 429
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/health")
def health():
    """Simple health-check endpoint."""
    return jsonify({
        "status": "ok",
        "key_configured": bool(API_KEY),
    })


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    print(f"\n🧠  MindVault is running → http://localhost:{port}")
    print(f"    API key {'✅ loaded' if API_KEY else '⚠️  not set (use banner in browser)'}\n")
    app.run(debug=debug, port=port)
