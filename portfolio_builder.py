# v0.2.17
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

import json
import urllib.request
from genlayer import *

class CryptoPortfolioBuilder(gl.Contract):
    last_capital: str
    last_risk: str
    last_risk_profile: str
    last_summary: str
    last_portfolio_json: str
    total_requests: u256

    def __init__(self):
        self.last_capital = ""
        self.last_risk = ""
        self.last_risk_profile = "Balanced"
        self.last_summary = ""
        self.last_portfolio_json = "{}"
        self.total_requests = u256(0)

    @gl.public.write
    def build_portfolio(self, capital: str, risk_tolerance: str) -> str:
        # Fetching timely macro crypto context from live sources instead of static Wikipedia
        source_url = "https://www.coingecko.com/en/categories/layer-1"
        req = urllib.request.Request(source_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                market_context = response.read().decode('utf-8')[:3500]
        except Exception:
            market_context = "Live crypto macro context: Bitcoin, Ethereum, Solana, and major Web3 market sectors."

        prompt = f"""
        You are an expert crypto portfolio manager. Build a diversified spot crypto portfolio based on the user's parameters and live context.
        
        User Capital: {capital}
        Risk Tolerance: {risk_tolerance} (Options: Low, Medium, High)
        
        Live Market Context:
        {market_context}

        Rules for Consensus:
        - "risk_profile": string reflecting the chosen strategy.
        - "allocation": a list of objects, each containing "asset" (string), "percentage" (number), "amount" (string based on capital), and "reason" (short sentence).
        - "summary": a brief 1-sentence strategy overview.

        Respond strictly in valid JSON format with keys: "risk_profile", "allocation", and "summary".
        """
        
        res = gl.eq_principle.prompt_non_comparative(
            lambda: prompt,
            task="Build a customized spot crypto portfolio based on capital, risk tolerance, and live consensus",
            criteria="Validators must independently agree on the valid JSON structure containing risk_profile, allocation list, and summary derived from actual market parameters."
        )
        
        try:
            parsed = json.loads(str(res))
            risk_prof = str(parsed.get("risk_profile", risk_tolerance))
            summary_val = str(parsed.get("summary", ""))
        except Exception:
            risk_prof = risk_tolerance
            summary_val = str(res)

        self.last_capital = capital
        self.last_risk = risk_tolerance
        self.last_risk_profile = risk_prof
        self.last_summary = summary_val
        self.last_portfolio_json = str(res)
        self.total_requests = self.total_requests + u256(1)
        
        return str(res)

    @gl.public.view
    def get_last_portfolio(self) -> str:
        return self.last_portfolio_json

    @gl.public.view
    def get_stats(self) -> u256:
        return self.total_requests
