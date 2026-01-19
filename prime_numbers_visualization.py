#!/usr/bin/env python3
"""
Prime Numbers Visualization Script

This script finds all prime numbers up to 100,000 using the Sieve of Eratosthenes
algorithm and creates multiple visualizations of the results.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit: The upper bound for finding prime numbers

    Returns:
        A list of all prime numbers up to and including the limit
    """
    if limit < 2:
        return []

    # Create a boolean array and initialize all entries as true
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = is_prime[1] = False

    # Start with the smallest prime number, 2
    for i in range(2, int(np.sqrt(limit)) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            is_prime[i*i:limit+1:i] = False

    # Return all numbers that are still marked as prime
    return np.where(is_prime)[0].tolist()


def visualize_primes(primes: List[int], limit: int):
    """
    Create multiple visualizations of prime numbers.

    Args:
        primes: List of prime numbers
        limit: The upper limit used for finding primes
    """
    fig = plt.figure(figsize=(16, 10))

    # Visualization 1: Prime number distribution
    ax1 = plt.subplot(2, 3, 1)
    ax1.plot(primes, 'b.', markersize=0.5, alpha=0.5)
    ax1.set_xlabel('Index')
    ax1.set_ylabel('Primzahl')
    ax1.set_title(f'Verteilung der Primzahlen bis {limit:,}')
    ax1.grid(True, alpha=0.3)

    # Visualization 2: Prime density (number of primes in intervals)
    ax2 = plt.subplot(2, 3, 2)
    interval_size = 1000
    intervals = range(0, limit + interval_size, interval_size)
    prime_counts = []

    for i in range(len(intervals) - 1):
        count = sum(1 for p in primes if intervals[i] <= p < intervals[i+1])
        prime_counts.append(count)

    ax2.bar(intervals[:-1], prime_counts, width=interval_size*0.9, alpha=0.7, color='green')
    ax2.set_xlabel('Zahlenbereich')
    ax2.set_ylabel('Anzahl Primzahlen')
    ax2.set_title(f'Primzahldichte (Intervalle von {interval_size:,})')
    ax2.grid(True, alpha=0.3)

    # Visualization 3: Prime gaps
    ax3 = plt.subplot(2, 3, 3)
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    ax3.plot(gaps, 'r-', linewidth=0.5, alpha=0.7)
    ax3.set_xlabel('Primzahl Index')
    ax3.set_ylabel('Abstand zur nächsten Primzahl')
    ax3.set_title('Abstände zwischen aufeinanderfolgenden Primzahlen')
    ax3.grid(True, alpha=0.3)

    # Visualization 4: Ulam Spiral (partial, up to 10000 for visibility)
    ax4 = plt.subplot(2, 3, 4)
    spiral_limit = min(10000, limit)
    spiral_primes = [p for p in primes if p <= spiral_limit]
    size = int(np.ceil(np.sqrt(spiral_limit)))

    # Create spiral coordinates
    spiral = np.zeros((size, size))
    x, y = size // 2, size // 2
    dx, dy = 0, -1

    for i in range(1, spiral_limit + 1):
        if -size//2 < x <= size//2 and -size//2 < y <= size//2:
            if i in spiral_primes:
                spiral[y + size//2, x + size//2] = 1

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    ax4.imshow(spiral, cmap='binary', interpolation='nearest')
    ax4.set_title(f'Ulam-Spirale (bis {spiral_limit:,})')
    ax4.axis('off')

    # Visualization 5: Cumulative count of primes
    ax5 = plt.subplot(2, 3, 5)
    sample_points = np.linspace(0, len(primes)-1, min(10000, len(primes)), dtype=int)
    ax5.plot([primes[i] for i in sample_points], sample_points, 'purple', linewidth=1)
    ax5.set_xlabel('Zahl')
    ax5.set_ylabel('Anzahl Primzahlen ≤ n')
    ax5.set_title('Kumulative Anzahl der Primzahlen')
    ax5.grid(True, alpha=0.3)

    # Visualization 6: Statistics
    ax6 = plt.subplot(2, 3, 6)
    ax6.axis('off')

    stats_text = f"""
    Statistiken der Primzahlen bis {limit:,}:

    Anzahl Primzahlen: {len(primes):,}
    Kleinste Primzahl: {primes[0]}
    Größte Primzahl: {primes[-1]:,}

    Durchschnittlicher Abstand: {np.mean(gaps):.2f}
    Maximaler Abstand: {max(gaps)}
    Minimaler Abstand: {min(gaps)}

    Primzahldichte: {len(primes)/limit*100:.2f}%

    Erste 10 Primzahlen:
    {', '.join(map(str, primes[:10]))}

    Letzte 10 Primzahlen:
    {', '.join(map(str, primes[-10:]))}
    """

    ax6.text(0.1, 0.95, stats_text, transform=ax6.transAxes,
             fontsize=10, verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.suptitle('Primzahlen-Visualisierung bis 100.000', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('prime_numbers_visualization.png', dpi=150, bbox_inches='tight')
    print(f"\nVisualisierung gespeichert als 'prime_numbers_visualization.png'")
    plt.show()


def main():
    """Main function to find and visualize prime numbers."""
    limit = 100000

    print(f"Berechne Primzahlen bis {limit:,}...")
    primes = sieve_of_eratosthenes(limit)

    print(f"✓ {len(primes):,} Primzahlen gefunden!")
    print(f"  Kleinste: {primes[0]}")
    print(f"  Größte: {primes[-1]:,}")
    print(f"\nErstelle Visualisierungen...")

    visualize_primes(primes, limit)

    print("\n✓ Fertig!")


if __name__ == "__main__":
    main()
