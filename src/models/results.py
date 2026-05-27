from dataclasses import dataclass


@dataclass
class IntegrationResult:
    estimated_value: float
    analytical_value: float
    absolute_error: float
    relative_error: float
    scipy_value: float | None = None
