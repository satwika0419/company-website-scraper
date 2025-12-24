# TASK 2 — Company Profiling (Probiotics)

## Objective
To determine whether a company is genuinely involved in the probiotics space
using observable website signals.

This module demonstrates how a basic, explainable system could automate
that assessment without machine learning.

## Approach
The framework evaluates five signal categories:
1. Probiotics Product Presence
2. Scientific & R&D Orientation
3. Regulatory & Quality Signals
4. Application Areas
5. Commercial Intent

Each category is scored based on keyword detection.

## Scoring Logic
- 2 = Strong signal
- 1 = Weak / moderate signal
- 0 = No signal

Total score determines classification:
- 8+ → Strong Probiotics Player
- 4–7 → Moderate / Adjacent Player
- <4 → Weak or Non-core Player

## How This Fits the Pipeline
- Task 1: Scrapes and structures website data
- Task 2: Interprets that data into business-relevant signals

## Note
This is a conceptual implementation to demonstrate structured thinking,
not a production classifier.
