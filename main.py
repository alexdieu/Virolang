import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import sys
import threading
import queue
import re # ADDED: For parsing progress from text

# --- Matplotlib for plotting ---
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Import existing Virolang logic ---
from antlr4 import FileStream, CommonTokenStream
from parser.VirolangLexer import VirolangLexer
from parser.VirolangParser import VirolangParser
from parser.visitors import ExecutionVisitor


class QueueIO:
    def __init__(self, q):
        self.queue = q
    def write(self, text):
        self.queue.put(text)
    def flush(self):
        pass

def run_simulation_worker(file_path: str, email: str, q: queue.Queue):
    stdout_redirect = QueueIO(q)
    sys.stdout = stdout_redirect
    sys.stderr = stdout_redirect

    try:
        if not file_path: raise ValueError("Virolang script file not selected.")
        if not email: raise ValueError("NCBI Email is required.")
            
        input_stream = FileStream(file_path)
        lexer = VirolangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = VirolangParser(stream)
        tree = parser.prog()
        
        env = {'email': email}
        visitor = ExecutionVisitor(env=env)
        visitor.visit(tree)

        if visitor.plot_data and isinstance(visitor.plot_data, list):
            q.put({'type': 'plot_data', 'data': visitor.plot_data})

        print("\n--- Simulation Finished ---")

    except Exception as e:
        print(f"\n--- AN ERROR OCCURRED ---\n{type(e).__name__}: {e}")
    finally:
        q.put(None)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virolang Simulator")
        self.geometry("900x700")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        controls_frame.pack(fill=tk.X, expand=False, pady=5)
        controls_frame.columnconfigure(1, weight=1)

        ttk.Label(controls_frame, text="Virolang Script:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.file_path_var = tk.StringVar()
        ttk.Entry(controls_frame, textvariable=self.file_path_var, state="readonly").grid(row=0, column=1, sticky="ew", padx=5)
        self.browse_button = ttk.Button(controls_frame, text="Browse...", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5)

        ttk.Label(controls_frame, text="NCBI Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_var = tk.StringVar()
        ttk.Entry(controls_frame, textvariable=self.email_var).grid(row=1, column=1, columnspan=2, sticky="ew", padx=5)
        
        self.run_button = ttk.Button(main_frame, text="Run Simulation", command=self.start_simulation)
        self.run_button.pack(fill=tk.X, pady=(10, 0))

        # --- ADDED: Progress Bar ---
        self.progressbar = ttk.Progressbar(main_frame, orient='horizontal', mode='determinate')
        # This will be packed into the view when the simulation starts

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(10,0))
        console_frame = ttk.Frame(self.notebook, padding="5")
        self.notebook.add(console_frame, text="Console Output")
        self.output_console = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, bg="#2E2E2E", fg="#DCDCDC", insertbackground="white")
        self.output_console.pack(fill=tk.BOTH, expand=True)
        self.output_console.configure(state='disabled')
        plot_frame = ttk.Frame(self.notebook, padding="5")
        self.notebook.add(plot_frame, text="Results Plot")
        self.fig = Figure(figsize=(5, 4), dpi=100, facecolor="#F0F0F0")
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.ax.set_facecolor("#EAEAEA")
        
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w").pack(side=tk.BOTTOM, fill=tk.X)

        self.simulation_thread = None
        self.io_queue = queue.Queue()
        # Pre-compile regex for performance
        self.cycle_regex = re.compile(r"--- Running Population Cycle (\d+)/(\d+) ---")

    def update_plot(self, history: list):
        self.ax.clear()
        if not history or not isinstance(history[0], dict): return
        cycles = range(len(history))
        categories = ['susceptible', 'infected', 'recovered', 'dead']
        colors = {'susceptible': 'blue', 'infected': 'red', 'recovered': 'green', 'dead': 'black'}
        data = {cat: [h.get(cat, 0) for h in history] for cat in categories}
        for cat in categories:
            if any(data[cat]): # Only plot if there's data
                self.ax.plot(cycles, data[cat], label=cat.capitalize(), color=colors[cat])
        self.ax.set_title("Epidemic Progression")
        self.ax.set_xlabel("Simulation Cycles")
        self.ax.set_ylabel("Number of Agents")
        self.ax.legend()
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.fig.tight_layout()
        self.canvas.draw()
        print("--- Plot updated with simulation results. ---")

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select a Virolang Script", filetypes=(("Virolang Files", "*.vl"),))
        if file_path: self.file_path_var.set(file_path)

    def start_simulation(self):
        if not self.file_path_var.get() or not self.email_var.get():
            self.status_var.set("Error: Please select a script and enter your email.")
            return

        self.run_button.config(state="disabled")
        self.status_var.set("Running simulation...")
        
        self.output_console.configure(state='normal')
        self.output_console.delete('1.0', tk.END)
        self.output_console.configure(state='disabled')
        self.ax.clear()
        self.canvas.draw()
        
        # --- ADDED: Show and reset the progress bar ---
        self.progressbar.pack(fill=tk.X, pady=5)
        self.progressbar['value'] = 0

        self.simulation_thread = threading.Thread(
            target=run_simulation_worker,
            args=(self.file_path_var.get(), self.email_var.get(), self.io_queue)
        )
        self.simulation_thread.start()
        self.after(100, self.process_queue)

    def process_queue(self):
        try:
            while True:
                msg = self.io_queue.get_nowait()
                if msg is None:
                    self.run_button.config(state="normal")
                    self.status_var.set("Ready")
                    self.progressbar.pack_forget() # Hide progress bar on completion
                    sys.stdout = sys.__stdout__
                    return
                
                # --- ADDED: Logic to update progress bar from console text ---
                if isinstance(msg, str):
                    match = self.cycle_regex.search(msg)
                    if match:
                        current_cycle, total_cycles = map(int, match.groups())
                        self.progressbar['maximum'] = total_cycles
                        self.progressbar['value'] = current_cycle
                
                if isinstance(msg, dict) and msg.get('type') == 'plot_data':
                    self.update_plot(msg['data'])
                else:
                    self.output_console.configure(state='normal')
                    self.output_console.insert(tk.END, str(msg))
                    self.output_console.yview(tk.END)
                    self.output_console.configure(state='disabled')
        except queue.Empty:
            pass

        self.after(100, self.process_queue)


if __name__ == "__main__":
    app = App()
    app.mainloop()
