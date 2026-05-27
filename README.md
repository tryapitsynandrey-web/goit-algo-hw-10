# Project Title

goit-algo-hw-10: Basic Algorithms and Data Structures

## Tech Stack

- Python 3.12+
- NumPy
- Matplotlib
- Pytest
- SciPy (Optional for verification)

## Description

This project implements solutions for two computational tasks:

1. Coin change algorithms using Greedy and Dynamic Programming approaches.
2. Definite integral estimation using the Monte Carlo method.

## Assignment Requirements

Task 1: Implement `find_coins_greedy` and `find_min_coins` for a given amount using a default set of coin denominations. Compare their execution time.

Task 2: Implement `monte_carlo_integral` to estimate the area under `f(x) = x^2` on the interval `[0, 2]`. Calculate errors compared to the exact analytical result.

## Architecture Overview

The project follows a modular structure separated into `core` algorithms, external `adapters`, data `models`, and `config`.

- `core/`: Contains the pure logic (coins, integration, benchmarking).
- `adapters/`: Contains integration with external tools (matplotlib for plotting).

## Project Structure

```text
goit-algo-hw-10/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── core/
│   ├── adapters/
│   ├── models/
│   ├── utils/
│   └── main.py
├── tests/
```

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the main script to see all results and generate the plot:

```bash
python -m src.main
```

## Task 1 — Coin Change Algorithms

- **Greedy Algorithm**: Repeatedly selects the largest coin denomination that is less than or equal to the remaining amount.
- **Dynamic Programming**: Builds an array representing the minimum number of coins for every amount up to the target, ensuring an optimal combination is found regardless of the denomination values.

## Task 1 — Complexity and Performance Analysis

- **Greedy Time Complexity**: O(k), where k is the number of denominations.
- **Greedy Space Complexity**: O(k) for the result dictionary.
- **Dynamic Programming Time Complexity**: O(amount * k).
- **Dynamic Programming Space Complexity**: O(amount) for storing the state array.

**Conclusion:** The Greedy approach is significantly faster and requires less memory, making it ideal for the default canonical coin system `[50, 25, 10, 5, 2, 1]`. However, Dynamic Programming is safer for arbitrary non-canonical coin systems (e.g. `[4, 3, 1]`) because the Greedy method can yield suboptimal results for certain target amounts.

## Task 2 — Monte Carlo Integration

The integral is estimated using the mean-value Monte Carlo method. Random points are evaluated, and their average is multiplied by the interval width.

## Task 2 — Accuracy Analysis

- **Exact Integral Value**: 8 / 3 ≈ 2.6666666667
- **Monte Carlo Approximation**: Depends on the sample size and random seed.
- As the sample size increases (e.g., from 1,000 to 100,000), the approximation generally converges towards the exact value, reducing both absolute and relative error.
- SciPy's `quad` function (if available) confirms the correctness of the analytical result.

## Test Strategy

Run tests using:

```bash
pytest -v
```

Tests cover edge cases (zero amount, negative values), verify algorithmic correctness for standard and non-canonical coin systems, and ensure Monte Carlo results remain within an acceptable error margin using a fixed seed.

## Development Notes

Project uses Python's typing system rigorously and isolates external dependencies.

## Limitations & Assumptions

- Monte Carlo estimations are statistically approximate.
- The default coin system assumes the Greedy algorithm is optimal.

## License

MIT
