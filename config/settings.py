from pathlib import Path

# Default Coin Denominations
DEFAULT_COINS = [50, 25, 10, 5, 2, 1]

# Monte Carlo Defaults
DEFAULT_MC_SAMPLES = 100_000
DEFAULT_SEED = 42
DEFAULT_MC_INTERVAL = (0.0, 2.0)

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DEFAULT_PLOT_PATH = PROCESSED_DATA_DIR / "integral_plot.png"

# Benchmarking
BENCHMARK_AMOUNTS = [113, 1000, 10000]
