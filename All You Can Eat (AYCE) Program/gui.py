from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from dijkstra import find_nearest_goal
from graph_data import (
    GOAL_DISPLAY_NAMES,
    GOAL_NODES,
    GRAPH,
    NODE_ORDER,
    STARTING_POINTS,
    START_NODE_BY_LABEL,
    format_neighbors,
)


GREEN = "#18D900"
GOLD = "#D4AF37"
_DARK = "#172117"


class AyceApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Pencarian Restoran AYCE Terdekat - Dijkstra")
        self.root.geometry("1280x760")
        self.root.minsize(980, 600)

        self._configure_styles()
        self._build_layout()
        self._populate_graph_table()

    def _configure_styles(self) -> None:
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Graph.Treeview",
            background="white",
            fieldbackground="white",
            foreground=_DARK,
            rowheight=27,
            font=("Segoe UI", 9),
        )
        style.configure(
            "Graph.Treeview.Heading",
            background=GREEN,
            foreground="black",
            font=("Segoe UI", 10, "bold"),
            padding=(8, 7),
        )
        style.map(
            "Graph.Treeview.Heading",
            background=[("active", "#14BD00")],
            foreground=[("active", "black")],
        )
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), foreground=_DARK)
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground="#4B574B")
        style.configure("Section.TLabel", font=("Segoe UI", 11, "bold"), foreground=_DARK)
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=(12, 9))

    def _build_layout(self) -> None:
        outer = ttk.Frame(self.root, padding=14)
        outer.pack(fill="both", expand=True)

        heading = ttk.Label(
            outer,
            text="Pencarian Rute Restoran All You Can Eat (AYCE)",
            style="Title.TLabel",
        )
        heading.pack(anchor="w")
        ttk.Label(
            outer,
            text="Graph berbobot yang sudah ditentukan · Algoritma Dijkstra · Jarak dalam kilometer",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(3, 12))

        content = ttk.Panedwindow(outer, orient="horizontal")
        content.pack(fill="both", expand=True)

        left = ttk.Frame(content, padding=(0, 0, 10, 0))
        right = ttk.Frame(content, padding=(10, 0, 0, 0), width=370)
        content.add(left, weight=3)
        content.add(right, weight=2)

        ttk.Label(left, text="Data graph (node dan tetangga berbobot)", style="Section.TLabel").pack(
            anchor="w", pady=(0, 8)
        )

        table_frame = ttk.Frame(left)
        table_frame.pack(fill="both", expand=True)

        columns = ("node", "neighbors")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Graph.Treeview",
            selectmode="browse",
        )
        self.tree.heading("node", text="Alamat/Tempat")
        self.tree.heading("neighbors", text="Tetangga (nama: jarak/km)")
        self.tree.column("node", width=190, minwidth=145, stretch=False, anchor="w")
        self.tree.column("neighbors", width=560, minwidth=330, stretch=True, anchor="w")

        y_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        ttk.Label(right, text="Cari AYCE terdekat", style="Section.TLabel").pack(anchor="w", pady=(0, 8))
        ttk.Label(
            right,
            text="Pilih salah satu titik awal yang sudah ditentukan.",
            wraplength=350,
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(right, text="Titik awal", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.start_var = tk.StringVar(value=STARTING_POINTS[0])
        self.start_combo = ttk.Combobox(
            right,
            textvariable=self.start_var,
            values=STARTING_POINTS,
            state="readonly",
            width=34,
        )
        self.start_combo.pack(fill="x", pady=(5, 12))

        self.search_button = ttk.Button(
            right,
            text="Cari jalur terpendek",
            style="Primary.TButton",
            command=self._search,
        )
        self.search_button.pack(fill="x")

        ttk.Separator(right, orient="horizontal").pack(fill="x", pady=16)
        ttk.Label(right, text="Hasil pencarian", style="Section.TLabel").pack(anchor="w", pady=(0, 8))

        self.goal_var = tk.StringVar(value="Restoran tujuan: -")
        ttk.Label(
            right,
            textvariable=self.goal_var,
            font=("Segoe UI", 11, "bold"),
            wraplength=350,
        ).pack(anchor="w", pady=(0, 4))

        self.distance_var = tk.StringVar(value="Total jarak: -")
        ttk.Label(
            right,
            textvariable=self.distance_var,
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(right, text="Susunan jalur", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        route_frame = ttk.Frame(right)
        route_frame.pack(fill="both", expand=True, pady=(5, 12))
        self.route_text = tk.Text(
            route_frame,
            height=12,
            wrap="word",
            font=("Consolas", 10),
            relief="solid",
            borderwidth=1,
            padx=9,
            pady=8,
            foreground=GOLD,
            state="disabled",
        )
        self.route_text.tag_configure("total", foreground=GOLD)
        route_scroll = ttk.Scrollbar(route_frame, orient="vertical", command=self.route_text.yview)
        self.route_text.configure(yscrollcommand=route_scroll.set)
        self.route_text.pack(side="left", fill="both", expand=True)
        route_scroll.pack(side="right", fill="y")

        ttk.Label(
            right,
            text="Goal state: Shabuhachi, Kaizen, Gyukaku, Akira Grill (Akira Dragon), Hae Don, Shaburi, dan AUCE Kongkow.",
            wraplength=350,
            justify="left",
        ).pack(anchor="w")

    def _populate_graph_table(self) -> None:
        for node in NODE_ORDER:
            self.tree.insert("", "end", values=(node, format_neighbors(node)))

    def _set_route_text(self, text: str) -> None:
        self.route_text.configure(state="normal")
        self.route_text.delete("1.0", "end")
        self.route_text.insert("1.0", text)
        self.route_text.configure(state="disabled")

    def _search(self) -> None:
        label = self.start_var.get().strip()
        start_node = START_NODE_BY_LABEL.get(label)
        if not start_node:
            messagebox.showerror("Titik awal tidak valid", "Pilih titik awal dari daftar yang tersedia.")
            return

        try:
            result = find_nearest_goal(start_node, GRAPH, GOAL_NODES)
        except (ValueError, KeyError) as exc:
            messagebox.showerror("Kesalahan data graph", str(exc))
            return

        if result is None:
            self.goal_var.set("Restoran tujuan: tidak ditemukan")
            self.distance_var.set("Total jarak: -")
            self._set_route_text(
                "Tidak ditemukan goal state yang dapat dicapai dari titik awal ini.\n\n"
                "Periksa kembali hubungan dan bobot pada graph_data.py."
            )
            return

        friendly_goal = GOAL_DISPLAY_NAMES.get(result.goal, result.goal)
        self.goal_var.set(f"Restoran tujuan: {friendly_goal}")
        self.distance_var.set(f"Total jarak: {result.distance_km:.2f} km")

        lines = []
        for index, node in enumerate(result.path, start=1):
            lines.append(f"{index}. {node}")
        lines.append("")
        lines.append("Detail segmen:")
        if not result.segments:
            lines.append("Titik awal sudah merupakan goal state.")
        else:
            for source, target, weight in result.segments:
                lines.append(f"{source} -> {target}: {weight:.2f} km")
        lines.append("")
        lines.append(f"Total: {result.distance_km:.2f} km")
        self._set_route_text("\n".join(lines))


def run_app() -> None:
    root = tk.Tk()
    AyceApp(root)
    root.mainloop()
