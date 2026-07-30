# v0.2.17
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

import urllib.request
from genlayer import *

class CryptoPortfolioBuilder(gl.Contract):
    last_capital: str
    last_risk: str
    last_portfolio: str
    total_requests: u256

    def __init__(self):
        self.last_capital = ""
        self.last_risk = ""
        self.last_portfolio = "NONE"
        self.total_requests = u256(0)

    @gl.public.write
    def build_portfolio(self, capital: str, risk_tolerance: str) -> str:
        # Fetching crypto context nondeterministically from the web to ensure consensus validation
        source_url = "https://en.wikipedia.org/wiki/Cryptocurrency"
        req = urllib.request.Request(source_url, headers={'User-Agent': 'GenLayer-Validator/1.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                market_context = response.read().decode('utf-8')[:2500]
        except Exception as e:
            market_context = "Standard crypto market context: Bitcoin, Ethereum, and major altcoins."

        prompt = f"""
        You are an expert crypto portfolio manager. Build a diversified spot crypto portfolio based on the user's parameters.
        
        User Capital: {capital}
        Risk Tolerance: {risk_tolerance} (Options: Low, Medium, High)
        
        Market Context Reference:
        {market_context}

        Respond strictly in valid JSON format with the following keys:
        - "risk_profile": string
        - "allocation": a list of objects, each containing "asset" (e.g. BTC, ETH, SOL), "percentage" (number), "amount" (calculated based on capital), and "reason" (short sentence).
        - "summary": a brief 1-sentence strategy overview.
        """
        
        res = gl.eq_principle.prompt_non_comparative(
            lambda: prompt,
            task="Build a customized spot crypto portfolio based on capital and risk tolerance",
            criteria="The output must be a valid JSON containing risk_profile, allocation list, and summary."
        )
        
        self.last_capital = capital
        self.last_risk = risk_tolerance
        self.last_portfolio = str(res)
        self.total_requests = self.total_requests + u256(1)
        
        return str(res)

    @gl.public.view
    def get_last_portfolio(self) -> str:
        return self.last_portfolio

    @gl.public.view
    def get_stats(self) -> u256:
        return self.total_requests
