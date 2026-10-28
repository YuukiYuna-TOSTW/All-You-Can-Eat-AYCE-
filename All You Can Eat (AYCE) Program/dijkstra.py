from __future__ import annotations

import heapq
from dataclasses import dataclass
from math import isfinite
from typing import Iterable

Graph = dict[str, list[tuple[str, float]]]


@dataclass(frozen=True)
class RouteResult:
    start: str
    goal: str
    path: list[str]
    distance_km: float
    # Setiap elemen memuat (asal, tujuan, bobot segmen).
    segments: list[tuple[str, str, float]]


def find_nearest_goal(
    start: str,
    graph: Graph,
    goal_nodes: Iterable[str],
) -> RouteResult | None:
    """Cari goal dengan jarak terkecil dari start menggunakan Dijkstra.

    Graph diproses sesuai arah edge yang disimpan. Fungsi berhenti saat goal
    pertama diambil dari priority queue, yang merupakan goal terdekat untuk
    bobot non-negatif.
    """
    if start not in graph:
        raise ValueError(f"Titik awal '{start}' tidak ada dalam graph.")

    goals = set(goal_nodes)
    unknown_goals = goals.difference(graph.keys())
    if unknown_goals:
        raise ValueError("Goal tidak ditemukan dalam graph: " + ", ".join(sorted(unknown_goals)))

    distances: dict[str, float] = {node: float("inf") for node in graph}
    previous: dict[str, str] = {}
    previous_weight: dict[str, float] = {}
    distances[start] = 0.0
    queue: list[tuple[float, str]] = [(0.0, start)]
    settled: set[str] = set()

    while queue:
        current_distance, current = heapq.heappop(queue)
        if current in settled:
            continue
        if current_distance > distances[current]:
            continue
        settled.add(current)

        if current in goals:
            path = [current]
            while path[-1] != start:
                parent = previous.get(path[-1])
                if parent is None:
                    # Defensive guard: normally impossible when predecessor data is valid.
                    return None
                path.append(parent)
            path.reverse()

            segments: list[tuple[str, str, float]] = []
            for left, right in zip(path, path[1:]):
                segments.append((left, right, previous_weight[right]))

            return RouteResult(
                start=start,
                goal=current,
                path=path,
                distance_km=current_distance,
                segments=segments,
            )

        for neighbor, weight in graph.get(current, []):
            if not isfinite(weight) or weight < 0:
                raise ValueError(
                    f"Bobot edge {current!r} -> {neighbor!r} harus berupa angka "
                    "finite dan tidak negatif."
                )
            if neighbor not in graph:
                raise ValueError(
                    f"Node tetangga '{neighbor}' dari '{current}' belum terdaftar sebagai node graph."
                )

            candidate = current_distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = current
                previous_weight[neighbor] = weight
                heapq.heappush(queue, (candidate, neighbor))

    return None
