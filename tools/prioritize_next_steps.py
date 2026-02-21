#!/usr/bin/env python3
"""
Simple reproducible prioritization model for IrsanAI-LRP next steps.
Computes weighted utility and softmax probabilities.
"""
from math import exp

# Criteria weights sum to 1.0
W = {
    "intent_alignment": 0.35,
    "impact": 0.30,
    "feasibility": 0.20,
    "risk_reduction": 0.15,
}

# Scores in [0,1]
steps = {
    "P1: CI + Regression Prompt Suite + Snapshots": {
        "intent_alignment": 0.95,
        "impact": 0.92,
        "feasibility": 0.86,
        "risk_reduction": 0.96,
    },
    "P2: Explainable Analysis Trace in UI": {
        "intent_alignment": 0.90,
        "impact": 0.89,
        "feasibility": 0.72,
        "risk_reduction": 0.85,
    },
    "P3: Core Modularization (UI/Analysis/Template split)": {
        "intent_alignment": 0.88,
        "impact": 0.84,
        "feasibility": 0.60,
        "risk_reduction": 0.90,
    },
    "P4: Governance Pack (SECURITY/CODEOWNERS/Templates)": {
        "intent_alignment": 0.78,
        "impact": 0.70,
        "feasibility": 0.92,
        "risk_reduction": 0.80,
    },
    "P5: Export Pack (JSON/Markdown Prompt Pack)": {
        "intent_alignment": 0.76,
        "impact": 0.74,
        "feasibility": 0.75,
        "risk_reduction": 0.65,
    },
}


def utility(v):
    return sum(W[k] * v[k] for k in W)


scores = {k: utility(v) for k, v in steps.items()}
# temperature tau=0.10 sharpens ranking while retaining uncertainty
TAU = 0.10
den = sum(exp(s / TAU) for s in scores.values())
probs = {k: exp(s / TAU) / den for k, s in scores.items()}

ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Weights:", W)
print("\nRanked utilities + probabilities:")
for name, s in ranked:
    print(f"- {name}: utility={s:.4f}, p={probs[name]*100:.2f}%")
