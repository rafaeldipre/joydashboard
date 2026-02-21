import base64
import sys
import tkinter as tk
from tkinter import ttk

import pygame

VERSION = "1.1.0"

# ── Icono embebido (PNG 64×64, CC0 – uxwing.com) ────────────────────────────
_ICON_B64 = (
    "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"
)

# ── Paletas de colores ───────────────────────────────────────────────────────
THEMES = {
    "dark": {
        "bg":           "#1e1e1e",
        "fg":           "#e0e0e0",
        "frame_bg":     "#2b2b2b",
        "btn_off":      "#2b2b2b",
        "btn_on":       "#1f8a3b",
        "btn_fg":       "#ffffff",
        "bar_trough":   "#3a3a3a",
        "label_bg":     "#1e1e1e",
        "status_bg":    "#2b2b2b",
    },
    "light": {
        "bg":           "#f0f0f0",
        "fg":           "#1a1a1a",
        "frame_bg":     "#ffffff",
        "btn_off":      "#d0d0d0",
        "btn_on":       "#2ecc71",
        "btn_fg":       "#000000",
        "bar_trough":   "#c0c0c0",
        "label_bg":     "#f0f0f0",
        "status_bg":    "#e0e0e0",
    },
}


class JoyTesterApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"JoyDashboard v{VERSION}")

        # ── Icono de ventana ─────────────────────────────────────────────────
        try:
            icon_img = tk.PhotoImage(data=_ICON_B64)
            self.root.iconphoto(True, icon_img)
        except Exception:
            pass

        # ── Pygame ───────────────────────────────────────────────────────────
        pygame.init()
        pygame.joystick.init()

        self.joy = None
        self.joy_instance_id = None
        self.num_axes = 0
        self.num_buttons = 0
        self.num_hats = 0

        self.axis_vals = []
        self.axis_bars = []
        self.hat_vals = []
        self.btn_labels = []

        # ── Tema ─────────────────────────────────────────────────────────────
        self.theme_name = tk.StringVar(value="dark")
        self._apply_theme("dark")

        self._build_header()

        main = ttk.Frame(root, padding=10)
        main.pack(fill="both", expand=True)

        self.left = ttk.Frame(main)
        self.left.pack(side="left", fill="y")

        self.right = ttk.Frame(main)
        self.right.pack(side="left", fill="both", expand=True, padx=(12, 0))

        self.status = tk.StringVar(value="Esperando dispositivo...")
        self.status_bar = tk.Label(
            root, textvariable=self.status, anchor="w",
            padx=10, pady=6,
        )
        self.status_bar.pack(fill="x")

        # Conectar al primer joystick si ya hay uno, o mostrar espera
        if pygame.joystick.get_count() > 0:
            self._select_joystick(0)
        else:
            self._show_waiting_state()

        self._refresh_colors()
        self.root.after(16, self.update_loop)

    # ── Tema ─────────────────────────────────────────────────────────────────

    def _apply_theme(self, name: str):
        self.theme = THEMES[name]
        style = ttk.Style()
        style.theme_use("clam")
        bg  = self.theme["bg"]
        fg  = self.theme["fg"]
        fbg = self.theme["frame_bg"]

        style.configure(".",            background=bg,  foreground=fg)
        style.configure("TFrame",       background=bg)
        style.configure("TLabel",       background=bg,  foreground=fg)
        style.configure("TLabelframe",  background=bg,  foreground=fg)
        style.configure("TLabelframe.Label", background=bg, foreground=fg)
        style.configure("TCombobox",    fieldbackground=fbg, foreground=fg)
        style.configure("TScrollbar",   background=fbg)
        style.configure("Horizontal.TProgressbar",
                        troughcolor=self.theme["bar_trough"],
                        background="#4caf50")
        self.root.configure(bg=bg)

    def _toggle_theme(self):
        new = "light" if self.theme_name.get() == "dark" else "dark"
        self.theme_name.set(new)
        self._apply_theme(new)
        self._refresh_colors()
        lbl = "☀ Modo claro" if new == "light" else "🌙 Modo oscuro"
        self.theme_btn.configure(text=lbl)

    def _refresh_colors(self):
        """Actualiza colores de widgets clásicos (tk.Label de botones, canvas)."""
        bg  = self.theme["btn_off"]
        fg  = self.theme["btn_fg"]
        for lbl in self.btn_labels:
            if lbl.cget("bg") != self.theme["btn_on"]:
                lbl.configure(bg=bg, fg=fg)
        self.status_bar.configure(
            bg=self.theme["status_bg"], fg=self.theme["fg"]
        )
        if hasattr(self, "buttons_canvas"):
            self.buttons_canvas.configure(bg=self.theme["bg"])

    # ── Construcción de UI ───────────────────────────────────────────────────

    def _build_header(self):
        header = ttk.Frame(self.root, padding=10)
        header.pack(fill="x")

        # Fila 1: selector + deadzone + botón de tema
        sel_row = ttk.Frame(header)
        sel_row.pack(fill="x", pady=(0, 4))

        ttk.Label(sel_row, text="Joystick:").pack(side="left")
        joy_names = [
            pygame.joystick.Joystick(i).get_name()
            for i in range(pygame.joystick.get_count())
        ]
        self.joy_selector = ttk.Combobox(
            sel_row, values=joy_names, state="readonly", width=44
        )
        if joy_names:
            self.joy_selector.current(0)
        self.joy_selector.pack(side="left", padx=(6, 20))
        self.joy_selector.bind(
            "<<ComboboxSelected>>",
            lambda e: self._select_joystick(self.joy_selector.current()),
        )

        ttk.Label(sel_row, text="Deadzone:").pack(side="left")
        self.deadzone_var = tk.DoubleVar(value=0.05)
        self.dz_label_var = tk.StringVar(value="0.05")
        ttk.Scale(
            sel_row,
            from_=0.0,
            to=0.25,
            variable=self.deadzone_var,
            orient="horizontal",
            length=110,
            command=lambda v: self.dz_label_var.set(f"{float(v):.2f}"),
        ).pack(side="left", padx=(4, 2))
        ttk.Label(sel_row, textvariable=self.dz_label_var, width=4).pack(side="left")

        # Botón modo oscuro / claro
        self.theme_btn = tk.Button(
            sel_row,
            text="☀ Modo claro",
            command=self._toggle_theme,
            relief="flat",
            padx=8, pady=2,
            cursor="hand2",
        )
        self.theme_btn.pack(side="right", padx=(8, 0))

        # Fila 2: info del dispositivo
        self.lbl_name = ttk.Label(header, text="", font=("Segoe UI", 12, "bold"))
        self.lbl_name.pack(anchor="w")
        self.lbl_info = ttk.Label(header, text="")
        self.lbl_info.pack(anchor="w")

    # ── Hot-plug ─────────────────────────────────────────────────────────────

    def _refresh_joy_selector(self):
        """Actualiza la lista de joysticks en el combobox."""
        joy_names = [
            pygame.joystick.Joystick(i).get_name()
            for i in range(pygame.joystick.get_count())
        ]
        self.joy_selector["values"] = joy_names
        if not joy_names:
            self.joy_selector.set("")

    def _on_joystick_added(self, device_index: int):
        """Llamado cuando se conecta un nuevo joystick."""
        self._refresh_joy_selector()
        if self.joy is None:
            self._select_joystick(device_index)
            count = pygame.joystick.get_count()
            if 0 <= device_index < count:
                self.joy_selector.current(device_index)

    def _on_joystick_removed(self, instance_id: int):
        """Llamado cuando se desconecta un joystick."""
        self._refresh_joy_selector()
        if self.joy_instance_id == instance_id:
            try:
                self.joy.quit()
            except Exception:
                pass
            self.joy = None
            self.joy_instance_id = None

            if pygame.joystick.get_count() > 0:
                self._select_joystick(0)
                self.joy_selector.current(0)
            else:
                self._show_waiting_state()

    def _show_waiting_state(self):
        """Muestra pantalla de espera cuando no hay joystick conectado."""
        for w in self.left.winfo_children():
            w.destroy()
        for w in self.right.winfo_children():
            w.destroy()

        self.axis_vals.clear()
        self.axis_bars.clear()
        self.hat_vals.clear()
        self.btn_labels.clear()

        self.lbl_name.config(text="Sin dispositivo conectado")
        self.lbl_info.config(text="")
        self.status.set("Esperando joystick/gamepad...")

        waiting_frm = ttk.Frame(self.right)
        waiting_frm.pack(expand=True, fill="both")
        ttk.Label(
            waiting_frm,
            text="Conecta un joystick o gamepad para comenzar",
            font=("Segoe UI", 13),
        ).pack(expand=True)

    # ── Lógica de joystick ───────────────────────────────────────────────────

    def _select_joystick(self, idx: int):
        if self.joy is not None:
            try:
                self.joy.quit()
            except Exception:
                pass

        self.joy = pygame.joystick.Joystick(idx)
        self.joy.init()
        self.joy_instance_id = self.joy.get_instance_id()

        self.num_axes    = self.joy.get_numaxes()
        self.num_buttons = self.joy.get_numbuttons()
        self.num_hats    = self.joy.get_numhats()

        name = self.joy.get_name()
        try:
            guid = self.joy.get_guid()
        except AttributeError:
            guid = "N/A"

        self.lbl_name.config(text=f"Dispositivo: {name}")
        self.lbl_info.config(
            text=(
                f"Axes: {self.num_axes}   "
                f"Buttons: {self.num_buttons}   "
                f"Hats: {self.num_hats}   "
                f"GUID: {guid}"
            )
        )
        self._rebuild_panels()

    def _rebuild_panels(self):
        for w in self.left.winfo_children():
            w.destroy()
        for w in self.right.winfo_children():
            w.destroy()

        self.axis_vals.clear()
        self.axis_bars.clear()
        self.hat_vals.clear()
        self.btn_labels.clear()

        self._build_axes_panel(self.left)
        self._build_hats_panel(self.left)
        self._build_buttons_panel(self.right)

    def _build_axes_panel(self, parent: ttk.Frame):
        frm = ttk.LabelFrame(parent, text="Axes", padding=10)
        frm.pack(fill="x", pady=(0, 10))

        for i in range(self.num_axes):
            row = ttk.Frame(frm)
            row.pack(fill="x", pady=2)

            ttk.Label(row, text=f"A{i}", width=4).pack(side="left")
            val = tk.StringVar(value="0.000")
            ttk.Label(row, textvariable=val, width=8).pack(side="left", padx=(0, 6))

            bar = ttk.Progressbar(
                row, orient="horizontal", length=220,
                mode="determinate", maximum=2000,
            )
            bar.pack(side="left", fill="x", expand=True)

            self.axis_vals.append(val)
            self.axis_bars.append(bar)

    def _build_hats_panel(self, parent: ttk.Frame):
        frm = ttk.LabelFrame(parent, text="Hats (D-Pad)", padding=10)
        frm.pack(fill="x")

        for i in range(self.num_hats):
            row = ttk.Frame(frm)
            row.pack(fill="x", pady=2)
            ttk.Label(row, text=f"H{i}", width=4).pack(side="left")
            val = tk.StringVar(value="(0, 0)")
            ttk.Label(row, textvariable=val).pack(side="left")
            self.hat_vals.append(val)

        if self.num_hats == 0:
            ttk.Label(frm, text="(No hats detectados)").pack(anchor="w")

    def _build_buttons_panel(self, parent: ttk.Frame):
        frm = ttk.LabelFrame(parent, text="Buttons", padding=10)
        frm.pack(fill="both", expand=True)

        self.buttons_canvas = tk.Canvas(
            frm, highlightthickness=0, bg=self.theme["bg"]
        )
        self.buttons_canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frm, orient="vertical", command=self.buttons_canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.buttons_canvas.configure(yscrollcommand=scrollbar.set)

        self.buttons_container = ttk.Frame(self.buttons_canvas)
        self.buttons_canvas.create_window((0, 0), window=self.buttons_container, anchor="nw")
        self.buttons_container.bind(
            "<Configure>",
            lambda e: self.buttons_canvas.configure(scrollregion=self.buttons_canvas.bbox("all")),
        )

        cols = 10
        for idx in range(self.num_buttons):
            r, c = divmod(idx, cols)
            cell = ttk.Frame(self.buttons_container, padding=2)
            cell.grid(row=r, column=c, sticky="nsew")

            lbl = tk.Label(
                cell,
                text=str(idx),
                width=5,
                relief="ridge",
                borderwidth=2,
                bg=self.theme["btn_off"],
                fg=self.theme["btn_fg"],
                font=("Segoe UI", 9, "bold"),
            )
            lbl.pack(fill="both", expand=True)
            self.btn_labels.append(lbl)

        for c in range(cols):
            self.buttons_container.grid_columnconfigure(c, weight=1)

        if self.num_buttons == 0:
            ttk.Label(
                self.buttons_container, text="(No buttons detectados)"
            ).grid(row=0, column=0, sticky="w")

    # ── Loop principal ───────────────────────────────────────────────────────

    def update_loop(self):
        # Procesar eventos pygame para detectar conexión/desconexión
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                self._on_joystick_added(event.device_index)
            elif event.type == pygame.JOYDEVICEREMOVED:
                self._on_joystick_removed(event.instance_id)

        # Si no hay joystick activo, solo esperar
        if self.joy is None:
            self.root.after(16, self.update_loop)
            return

        deadzone = self.deadzone_var.get()

        try:
            for i in range(self.num_axes):
                v = float(self.joy.get_axis(i))
                if abs(v) < deadzone:
                    v = 0.0
                self.axis_vals[i].set(f"{v:+.3f}")
                self.axis_bars[i]["value"] = int((v + 1.0) * 1000)

            for i in range(self.num_hats):
                self.hat_vals[i].set(str(self.joy.get_hat(i)))

            pressed_count = 0
            btn_on  = self.theme["btn_on"]
            btn_off = self.theme["btn_off"]
            btn_fg  = self.theme["btn_fg"]
            for i in range(self.num_buttons):
                if self.joy.get_button(i):
                    pressed_count += 1
                    self.btn_labels[i].configure(bg=btn_on,  fg="#ffffff")
                else:
                    self.btn_labels[i].configure(bg=btn_off, fg=btn_fg)

            self.status.set(f"Botones presionados: {pressed_count} / {self.num_buttons}")
        except Exception:
            # El joystick puede haberse desconectado; el evento JOYDEVICEREMOVED lo manejará
            pass

        self.root.after(16, self.update_loop)


def main():
    root = tk.Tk()
    app = JoyTesterApp(root)
    root.minsize(900, 520)
    root.mainloop()


if __name__ == "__main__":
    main()
