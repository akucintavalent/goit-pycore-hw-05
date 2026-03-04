from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Returns a Fibonacci function that caches previously computed results."""
    
    cache = { 0: 0, 1: 1 }

    def fibonacci(n: int) -> int:
        """Calculates the nth Fibonacci number using caching."""

        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer.")
        if n in cache:
            return cache[n]
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result

        return result
    
    return fibonacci
