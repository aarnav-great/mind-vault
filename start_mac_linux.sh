#!/usr/bin/env bash
set -e

echo ""
echo " ============================================="
echo "   MindVault — Personal Knowledge Base AI"
echo "   by Aarnav Kejriwal <aarnkej@gmail.com>"
echo " ============================================="
echo ""

# Load .env if it exists
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Prompt if key still not set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo " [!] ANTHROPIC_API_KEY is not set."
    echo "     Get your key at: https://console.anthropic.com"
    echo ""
    read -rp "  Paste your key (sk-ant-...): " ANTHROPIC_API_KEY
    export ANTHROPIC_API_KEY
    echo ""
fi

echo " [*] Installing / verifying dependencies..."
pip install -r requirements.txt -q
echo " [*] Dependencies OK."
echo ""
echo " [*] Starting MindVault..."
echo ""
echo " -----------------------------------------------"
echo "  Open in your browser: http://localhost:5000"
echo " -----------------------------------------------"
echo ""

python app.py
