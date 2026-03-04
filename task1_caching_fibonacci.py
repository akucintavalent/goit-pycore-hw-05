from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Returns a Fibonacci function that caches previously computed results."""
    
    cache = []

    def fibonacci(n: int) -> int:
        """Calculates the nth Fibonacci number using caching."""

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n < len(cache):
            return cache[n]
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache.append(result)

        return result
    
    return fibonacci
