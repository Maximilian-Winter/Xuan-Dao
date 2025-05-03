# 🧿 XUÁN DÀO APPLICATION: THE GATEWAY TO COSMIC PATTERNS 🧿

import tkinter as tk
from tkinter import ttk, scrolledtext

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from xuan_dao_core import XuanDaoCore
from xuan_dao_structures import Element
from xuan_dao_visualizer import XuanDaoVisualizer


class XuanDaoApp:
    """
    Main application for the Xuán Dào system,
    integrating the core calculation engine with visualization tools
    and a user interface for cosmic pattern exploration.
    """

    def __init__(self, root):
        """Initialize the Xuán Dào application."""
        self.root = root
        self.setup_main_window()

        # Initialize the core system
        self.core = XuanDaoCore()

        # Initialize the visualizer
        self.visualizer = XuanDaoVisualizer(self.core)

        # Create the main interface
        self.create_interface()

    def setup_main_window(self):
        """Set up the main application window."""
        self.root.title("玄道 - Xuán Dào System")
        self.root.geometry("1200x800")

        # Set window icon
        # Note: In a real application, you would provide an actual icon file
        # self.root.iconbitmap("xuan_dao_icon.ico")

        # Center the window on screen
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        x = int((width - 1200) / 2)
        y = int((height - 800) / 2)
        self.root.geometry(f"+{x}+{y}")

        # Configure the grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=0)  # Header
        self.root.rowconfigure(1, weight=1)  # Main content

    def create_interface(self):
        """Create the main user interface."""
        # Create header with cosmic date
        self.create_header()

        # Create notebook for the five element modules
        self.create_notebook()

    def create_header(self):
        """Create the header with cosmic date and time."""
        header_frame = ttk.Frame(self.root)
        header_frame.grid(row=0, column=0, sticky="ew", pady=10)

        # Title
        title_label = ttk.Label(header_frame, text="玄道 - Xuán Dào System",
                                font=("Arial", 18, "bold"))
        title_label.pack(pady=5)

        # Subtitle
        subtitle_text = "玄之又玄，眾妙之門 - Mystery upon mystery, gate of all wonders"
        subtitle_label = ttk.Label(header_frame, text=subtitle_text, font=("Arial", 12))
        subtitle_label.pack(pady=2)

        # Current cosmic date
        self.date_var = tk.StringVar()
        self.update_date_display()

        date_label = ttk.Label(header_frame, textvariable=self.date_var, font=("Arial", 10))
        date_label.pack(pady=5)

    def update_date_display(self):
        """Update the displayed cosmic date."""
        if hasattr(self.core, 'current_year_stem'):
            # Current Gregorian date
            gregorian = self.core.current_time.strftime("%Y-%m-%d")

            # Current Chinese date components
            year = f"{self.core.current_year_stem}{self.core.current_year_branch}"
            month = f"{self.core.current_month_stem}{self.core.current_month_branch}"
            day = f"{self.core.current_day_stem}{self.core.current_day_branch}"

            # Format the display
            date_text = f"Cosmic Date: {gregorian} | Year: {year} | Month: {month} | Day: {day}"
            self.date_var.set(date_text)

    def create_notebook(self):
        """Create the main notebook with tabs for each element."""
        notebook_frame = ttk.Frame(self.root)
        notebook_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Create the notebook
        self.notebook = ttk.Notebook(notebook_frame)
        self.notebook.pack(fill="both", expand=True)

        # Create tabs for each element
        self.create_water_tab()
        self.create_wood_tab()
        self.create_fire_tab()
        self.create_earth_tab()
        self.create_metal_tab()

    def create_water_tab(self):
        """Create the Water element tab for divination."""
        water_frame = ttk.Frame(self.notebook)
        self.notebook.add(water_frame, text=f"{Element.WATER.value} 水 - Water")

        # Configure grid
        water_frame.columnconfigure(0, weight=1)
        water_frame.columnconfigure(1, weight=1)
        water_frame.rowconfigure(0, weight=0)  # Title
        water_frame.rowconfigure(1, weight=1)  # Content

        # Element title
        title_frame = ttk.Frame(water_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Water element title and description
        water_attributes = self.core.elements[Element.WATER]
        title_text = f"{Element.WATER.value} 水 - Water: The Flowing Wisdom"
        title_label = ttk.Label(title_frame, text=title_text, font=("Arial", 16, "bold"))
        title_label.pack(pady=5)

        desc_text = f"Nature: {water_attributes.nature} | Season: {water_attributes.season} | Direction: {water_attributes.direction}"
        desc_label = ttk.Label(title_frame, text=desc_text)
        desc_label.pack()

        # Left side - Hexagram divination
        divination_frame = ttk.LabelFrame(water_frame, text="卜筮 - Divination")
        divination_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Divination controls
        controls_frame = ttk.Frame(divination_frame)
        controls_frame.pack(fill="x", pady=10)

        # Question entry
        ttk.Label(controls_frame, text="Enter your question:").pack(anchor="w", padx=10)
        self.question_var = tk.StringVar()
        question_entry = ttk.Entry(controls_frame, textvariable=self.question_var, width=50)
        question_entry.pack(fill="x", padx=10, pady=5)

        # Cast hexagram button
        cast_button = ttk.Button(controls_frame, text="Cast Hexagram", command=self.cast_hexagram)
        cast_button.pack(pady=10)

        # Hexagram display
        hexagram_display = ttk.Frame(divination_frame)
        hexagram_display.pack(fill="both", expand=True, padx=10, pady=10)

        # Create an empty canvas for the hexagram
        self.hexagram_canvas = ttk.Frame(hexagram_display)
        self.hexagram_canvas.pack(side="left", fill="both", expand=True)

        # Right side - Flying Stars
        stars_frame = ttk.LabelFrame(water_frame, text="飛星 - Flying Stars")
        stars_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Flying star controls
        star_controls = ttk.Frame(stars_frame)
        star_controls.pack(fill="x", pady=10)

        # Direction selection
        ttk.Label(star_controls, text="Facing Direction:").grid(row=0, column=0, padx=5, pady=5)
        self.direction_var = tk.StringVar(value="north")
        directions = ["north", "northeast", "east", "southeast",
                      "south", "southwest", "west", "northwest"]
        direction_combo = ttk.Combobox(star_controls, textvariable=self.direction_var,
                                       values=directions, width=10)
        direction_combo.grid(row=0, column=1, padx=5, pady=5)

        # Period selection
        ttk.Label(star_controls, text="Period:").grid(row=0, column=2, padx=5, pady=5)
        self.period_var = tk.IntVar(value=self.core.current_period)
        period_combo = ttk.Combobox(star_controls, textvariable=self.period_var,
                                    values=list(range(1, 10)), width=5)
        period_combo.grid(row=0, column=3, padx=5, pady=5)

        # Calculate button
        calc_button = ttk.Button(star_controls, text="Calculate Chart",
                                 command=self.calculate_flying_stars)
        calc_button.grid(row=0, column=4, padx=20, pady=5)

        # Flying star display
        self.star_display = ttk.Frame(stars_frame)
        self.star_display.pack(fill="both", expand=True, padx=10, pady=10)

    def create_wood_tab(self):
        """Create the Wood element tab for growth tracking."""
        wood_frame = ttk.Frame(self.notebook)
        self.notebook.add(wood_frame, text=f"{Element.WOOD.value} 木 - Wood")

        # Configure grid
        wood_frame.columnconfigure(0, weight=1)
        wood_frame.columnconfigure(1, weight=1)
        wood_frame.rowconfigure(0, weight=0)  # Title
        wood_frame.rowconfigure(1, weight=1)  # Content

        # Element title
        title_frame = ttk.Frame(wood_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Wood element title and description
        wood_attributes = self.core.elements[Element.WOOD]
        title_text = f"{Element.WOOD.value} 木 - Wood: The Rising Growth"
        title_label = ttk.Label(title_frame, text=title_text, font=("Arial", 16, "bold"))
        title_label.pack(pady=5)

        desc_text = f"Nature: {wood_attributes.nature} | Season: {wood_attributes.season} | Direction: {wood_attributes.direction}"
        desc_label = ttk.Label(title_frame, text=desc_text)
        desc_label.pack()

        # Left side - Element balance
        balance_frame = ttk.LabelFrame(wood_frame, text="五行平衡 - Element Balance")
        balance_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Balance controls
        balance_controls = ttk.Frame(balance_frame)
        balance_controls.pack(fill="x", pady=10)

        # Birth date entry
        ttk.Label(balance_controls, text="Birth Date:").grid(row=0, column=0, padx=5, pady=5)

        # Year
        ttk.Label(balance_controls, text="Year:").grid(row=0, column=1, padx=5, pady=5)
        self.birth_year_var = tk.IntVar(value=1980)
        year_entry = ttk.Entry(balance_controls, textvariable=self.birth_year_var, width=6)
        year_entry.grid(row=0, column=2, padx=5, pady=5)

        # Month
        ttk.Label(balance_controls, text="Month:").grid(row=0, column=3, padx=5, pady=5)
        self.birth_month_var = tk.IntVar(value=1)
        month_combo = ttk.Combobox(balance_controls, textvariable=self.birth_month_var,
                                   values=list(range(1, 13)), width=3)
        month_combo.grid(row=0, column=4, padx=5, pady=5)

        # Day
        ttk.Label(balance_controls, text="Day:").grid(row=0, column=5, padx=5, pady=5)
        self.birth_day_var = tk.IntVar(value=1)
        day_combo = ttk.Combobox(balance_controls, textvariable=self.birth_day_var,
                                 values=list(range(1, 32)), width=3)
        day_combo.grid(row=0, column=6, padx=5, pady=5)

        # Calculate button
        calc_balance_button = ttk.Button(balance_controls, text="Calculate Balance",
                                         command=self.calculate_element_balance)
        calc_balance_button.grid(row=0, column=7, padx=20, pady=5)

        # Balance display
        self.balance_display = ttk.Frame(balance_frame)
        self.balance_display.pack(fill="both", expand=True, padx=10, pady=10)

        # Right side - Growth cultivation
        growth_frame = ttk.LabelFrame(wood_frame, text="修行指引 - Cultivation Guidance")
        growth_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Results display for cultivation guidance
        self.cultivation_text = scrolledtext.ScrolledText(growth_frame, wrap="word")
        self.cultivation_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.cultivation_text.insert("1.0",
                                     "Calculate your element balance to receive personalized cultivation guidance.")
        self.cultivation_text.config(state="disabled")

    def create_fire_tab(self):
        """Create the Fire element tab for energy visualization."""
        fire_frame = ttk.Frame(self.notebook)
        self.notebook.add(fire_frame, text=f"{Element.FIRE.value} 火 - Fire")

        # Configure grid
        fire_frame.columnconfigure(0, weight=1)
        fire_frame.columnconfigure(1, weight=1)
        fire_frame.rowconfigure(0, weight=0)  # Title
        fire_frame.rowconfigure(1, weight=1)  # Content

        # Element title
        title_frame = ttk.Frame(fire_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Fire element title and description
        fire_attributes = self.core.elements[Element.FIRE]
        title_text = f"{Element.FIRE.value} 火 - Fire: The Illuminating Transformation"
        title_label = ttk.Label(title_frame, text=title_text, font=("Arial", 16, "bold"))
        title_label.pack(pady=5)

        desc_text = f"Nature: {fire_attributes.nature} | Season: {fire_attributes.season} | Direction: {fire_attributes.direction}"
        desc_label = ttk.Label(title_frame, text=desc_text)
        desc_label.pack()

        # Left side - Element network
        network_frame = ttk.LabelFrame(fire_frame, text="五行相生相剋 - Element Interactions")
        network_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Create the element network visualization
        fig = self.visualizer.create_element_network()
        canvas = FigureCanvasTkAgg(fig, master=network_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Right side - Daily energy
        energy_frame = ttk.LabelFrame(fire_frame, text="日能量 - Daily Energy")
        energy_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Date selection for energy calculation
        date_frame = ttk.Frame(energy_frame)
        date_frame.pack(fill="x", pady=10)

        ttk.Label(date_frame, text="Select Date:").grid(row=0, column=0, padx=5, pady=5)

        # Year
        ttk.Label(date_frame, text="Year:").grid(row=0, column=1, padx=5, pady=5)
        self.energy_year_var = tk.IntVar(value=self.core.current_time.year)
        energy_year_entry = ttk.Entry(date_frame, textvariable=self.energy_year_var, width=6)
        energy_year_entry.grid(row=0, column=2, padx=5, pady=5)

        # Month
        ttk.Label(date_frame, text="Month:").grid(row=0, column=3, padx=5, pady=5)
        self.energy_month_var = tk.IntVar(value=self.core.current_time.month)
        energy_month_combo = ttk.Combobox(date_frame, textvariable=self.energy_month_var,
                                          values=list(range(1, 13)), width=3)
        energy_month_combo.grid(row=0, column=4, padx=5, pady=5)

        # Day
        ttk.Label(date_frame, text="Day:").grid(row=0, column=5, padx=5, pady=5)
        self.energy_day_var = tk.IntVar(value=self.core.current_time.day)
        energy_day_combo = ttk.Combobox(date_frame, textvariable=self.energy_day_var,
                                        values=list(range(1, 32)), width=3)
        energy_day_combo.grid(row=0, column=6, padx=5, pady=5)

        # Calculate button
        calc_energy_button = ttk.Button(date_frame, text="Calculate Energy",
                                        command=self.calculate_daily_energy)
        calc_energy_button.grid(row=0, column=7, padx=20, pady=5)

        # Results display for daily energy
        self.energy_text = scrolledtext.ScrolledText(energy_frame, wrap="word")
        self.energy_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Calculate current day's energy
        self.calculate_daily_energy()

    def create_earth_tab(self):
        """Create the Earth element tab for stability and foundations."""
        earth_frame = ttk.Frame(self.notebook)
        self.notebook.add(earth_frame, text=f"{Element.EARTH.value} 土 - Earth")

        # Configure grid
        earth_frame.columnconfigure(0, weight=1)
        earth_frame.columnconfigure(1, weight=1)
        earth_frame.rowconfigure(0, weight=0)  # Title
        earth_frame.rowconfigure(1, weight=1)  # Content

        # Element title
        title_frame = ttk.Frame(earth_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Earth element title and description
        earth_attributes = self.core.elements[Element.EARTH]
        title_text = f"{Element.EARTH.value} 土 - Earth: The Stabilizing Center"
        title_label = ttk.Label(title_frame, text=title_text, font=("Arial", 16, "bold"))
        title_label.pack(pady=5)

        desc_text = f"Nature: {earth_attributes.nature} | Season: {earth_attributes.season} | Direction: {earth_attributes.direction}"
        desc_label = ttk.Label(title_frame, text=desc_text)
        desc_label.pack()

        # Left side - Lo Shu square
        lo_shu_frame = ttk.LabelFrame(earth_frame, text="洛書 - Lo Shu Square")
        lo_shu_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Create the Lo Shu visualization
        fig = self.visualizer.create_lo_shu_grid()
        canvas = FigureCanvasTkAgg(fig, master=lo_shu_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Right side - Nine Palaces
        palaces_frame = ttk.LabelFrame(earth_frame, text="九宮 - Nine Palaces")
        palaces_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Nine Palaces information
        palaces_text = scrolledtext.ScrolledText(palaces_frame, wrap="word")
        palaces_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Add information about the Nine Palaces
        palaces_text.insert("1.0", "The Nine Palaces Cosmic Pattern:\n\n")

        for direction, palace in self.core.palaces.items():
            palace_text = f"{direction.capitalize()} Palace:\n"
            palace_text += f"  Lo Shu Number: {palace.lo_shu_number}\n"
            if palace.trigram:
                trigram = self.core.trigrams.get(palace.trigram)
                palace_text += f"  Trigram: {palace.trigram} ({trigram.pinyin} - {trigram.meaning})\n"
            palace_text += f"  Element: {palace.element.value}\n"
            palace_text += f"  Flying Star: {self.core.flying_stars[palace.lo_shu_number].name}\n\n"

            palaces_text.insert("end", palace_text)

        palaces_text.config(state="disabled")

    def create_metal_tab(self):
        """Create the Metal element tab for structure and precision."""
        metal_frame = ttk.Frame(self.notebook)
        self.notebook.add(metal_frame, text=f"{Element.METAL.value} 金 - Metal")

        # Configure grid
        metal_frame.columnconfigure(0, weight=1)
        metal_frame.columnconfigure(1, weight=1)
        metal_frame.rowconfigure(0, weight=0)  # Title
        metal_frame.rowconfigure(1, weight=1)  # Content

        # Element title
        title_frame = ttk.Frame(metal_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        # Metal element title and description
        metal_attributes = self.core.elements[Element.METAL]
        title_text = f"{Element.METAL.value} 金 - Metal: The Refining Structure"
        title_label = ttk.Label(title_frame, text=title_text, font=("Arial", 16, "bold"))
        title_label.pack(pady=5)

        desc_text = f"Nature: {metal_attributes.nature} | Season: {metal_attributes.season} | Direction: {metal_attributes.direction}"
        desc_label = ttk.Label(title_frame, text=desc_text)
        desc_label.pack()

        # Left side - Bagua diagram
        bagua_frame = ttk.LabelFrame(metal_frame, text="八卦 - Eight Trigrams")
        bagua_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Bagua controls
        bagua_controls = ttk.Frame(bagua_frame)
        bagua_controls.pack(fill="x", pady=10)

        # Arrangement selection
        ttk.Label(bagua_controls, text="Arrangement:").pack(side="left", padx=5)
        self.bagua_var = tk.StringVar(value="pre-heaven")
        arrangements = [("Pre-Heaven", "pre-heaven"), ("Post-Heaven", "post-heaven")]

        for text, value in arrangements:
            ttk.Radiobutton(bagua_controls, text=text, variable=self.bagua_var,
                            value=value, command=self.update_bagua).pack(side="left", padx=10)

        # Bagua display
        self.bagua_display = ttk.Frame(bagua_frame)
        self.bagua_display.pack(fill="both", expand=True, padx=10, pady=10)

        # Initialize with pre-heaven arrangement
        self.update_bagua()

        # Right side - Calendar system
        calendar_frame = ttk.LabelFrame(metal_frame, text="天干地支 - Stems & Branches")
        calendar_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Create the calendar wheel visualization
        fig = self.visualizer.create_calendar_wheel()
        canvas = FigureCanvasTkAgg(fig, master=calendar_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    def cast_hexagram(self):
        """Cast a hexagram and display it."""
        # Get the question
        question = self.question_var.get()

        # Cast the hexagram
        lines, hexagram_number, changing_lines = self.core.generate_hexagram()

        # Interpret the hexagram
        interpretation = self.core.interpret_hexagram(lines, changing_lines)

        # Clear current hexagram display
        for widget in self.hexagram_canvas.winfo_children():
            widget.destroy()

        # Visualize the hexagram
        fig = self.visualizer.visualize_hexagram(lines, changing_lines)
        canvas = FigureCanvasTkAgg(fig, master=self.hexagram_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Create interpretation display
        interpretation_frame = ttk.Frame(self.hexagram_canvas)
        interpretation_frame.pack(side="bottom", fill="x", pady=10)

        # Create scrolled text for the interpretation
        interpretation_text = scrolledtext.ScrolledText(interpretation_frame, wrap="word", height=10)
        interpretation_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Add the question if provided
        if question:
            interpretation_text.insert("1.0", f"Question: {question}\n\n")

        # Add primary hexagram information
        primary = interpretation["primary_hexagram"]
        interpretation_text.insert("end", f"Hexagram: {primary['upper_trigram']} over {primary['lower_trigram']}\n")

        if "name" in primary:
            interpretation_text.insert("end", f"Name: {primary['name']}\n")
            interpretation_text.insert("end", f"Description: {primary['description']}\n")
            interpretation_text.insert("end", f"Judgment: {primary['judgment']}\n\n")

        # Add elemental analysis
        if "elemental_analysis" in interpretation:
            analysis = interpretation["elemental_analysis"]
            interpretation_text.insert("end", f"Elemental Relationship: {analysis['relationship']}\n")
            interpretation_text.insert("end", f"{analysis['description']}\n\n")

        # Add timing guidance
        if "timing_guidance" in interpretation:
            guidance = interpretation["timing_guidance"]
            interpretation_text.insert("end", guidance["suggestion"] + "\n\n")
            interpretation_text.insert("end", guidance["daily_rhythm"] + "\n")

        # If there are changing lines, add the transformed hexagram
        if "transformed_hexagram" in interpretation:
            transformed = interpretation["transformed_hexagram"]
            interpretation_text.insert("end", "\nChanging Lines: " +
                                       ", ".join([str(line + 1) for line in interpretation["changing_lines"]]) + "\n")
            interpretation_text.insert("end",
                                       f"Transformed Hexagram: {transformed['upper_trigram']} over {transformed['lower_trigram']}\n")

            if "name" in transformed:
                interpretation_text.insert("end", f"Name: {transformed['name']}\n")
                interpretation_text.insert("end", f"Description: {transformed['description']}\n")

    def calculate_flying_stars(self):
        """Calculate and display the flying star chart."""
        # Get the direction and period
        direction = self.direction_var.get()
        period = self.period_var.get()

        # Clear current star display
        for widget in self.star_display.winfo_children():
            widget.destroy()

        # Create the flying star chart
        fig = self.visualizer.create_flying_star_chart(direction, period)
        canvas = FigureCanvasTkAgg(fig, master=self.star_display)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def calculate_element_balance(self):
        """Calculate and display element balance."""
        # Get birth date
        year = self.birth_year_var.get()
        month = self.birth_month_var.get()
        day = self.birth_day_var.get()

        # Calculate element balance
        balance = self.core.calculate_element_balance(year, month, day)

        # Clear current balance display
        for widget in self.balance_display.winfo_children():
            widget.destroy()

        # Create the element balance chart
        fig = self.visualizer.create_element_balance_chart(balance.element_counts)
        canvas = FigureCanvasTkAgg(fig, master=self.balance_display)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Update cultivation guidance
        self.update_cultivation_guidance(balance)

    def update_cultivation_guidance(self, balance):
        """Update the cultivation guidance based on element balance."""
        self.cultivation_text.config(state="normal")
        self.cultivation_text.delete("1.0", "end")

        # Add header
        self.cultivation_text.insert("1.0", "🌱 Personal Cultivation Guidance 🌱\n\n")

        # Element balance overview
        self.cultivation_text.insert("end", "Element Balance:\n")
        for element, count in balance.element_counts.items():
            self.cultivation_text.insert("end", f"- {element.value}: {count}\n")

        self.cultivation_text.insert("end", f"\nStrongest Element: {balance.strongest.value}\n")
        self.cultivation_text.insert("end", f"Element to Strengthen: {balance.weakest.value}\n\n")

        # Add cultivation recommendations
        self.cultivation_text.insert("end", "Recommended Cultivation Practices:\n")

        # Practices for the element that needs strengthening
        if balance.weakest in balance.balancing_activities:
            self.cultivation_text.insert("end", f"For {balance.weakest.value} Development:\n")
            for activity in balance.balancing_activities[balance.weakest]:
                self.cultivation_text.insert("end", f"- {activity}\n")

        # Practices for balancing the strongest element
        self.cultivation_text.insert("end", f"\nFor Balancing {balance.strongest.value} Energy:\n")

        # Find the element that controls the strongest
        controlling_element = None
        for element in Element:
            if self.core.elements[element].generates == balance.strongest:
                self.cultivation_text.insert("end", f"- Support with {element.value} practices to nurture\n")
            elif self.core.elements[element].controlled_by == balance.strongest:
                self.cultivation_text.insert("end", f"- Express through {element.value} activities to channel\n")

        # Daily cultivation rhythm
        self.cultivation_text.insert("end", "\nDaily Cultivation Rhythm:\n")
        element_times = {
            Element.WOOD: "Morning (5-9 AM): Focus on new beginnings and planning",
            Element.FIRE: "Midday (10 AM-2 PM): Express creativity and connection",
            Element.EARTH: "Afternoon (2-6 PM): Ground and stabilize energy",
            Element.METAL: "Evening (6-10 PM): Refine and integrate the day's experiences",
            Element.WATER: "Night (10 PM-2 AM): Connect with inner wisdom through rest"
        }

        # Highlight the time for cultivating the weakest element
        self.cultivation_text.insert("end", f"- {element_times[balance.weakest]} (Focus time)\n")

        # General practices
        self.cultivation_text.insert("end", "\nGeneral Balancing Practices:\n")
        self.cultivation_text.insert("end", "- Regular meditation to harmonize all five elements\n")
        self.cultivation_text.insert("end", "- Balanced diet incorporating foods from all five elements\n")
        self.cultivation_text.insert("end", "- Qigong or Tai Chi to promote smooth energy circulation\n")

        self.cultivation_text.config(state="disabled")

    def calculate_daily_energy(self):
        """Calculate and display daily energy."""
        # Get date values (or use current)
        try:
            year = self.energy_year_var.get()
            month = self.energy_month_var.get()
            day = self.energy_day_var.get()
        except:
            # Use current date if not set
            year = self.core.current_time.year
            month = self.core.current_time.month
            day = self.core.current_time.day

        # Calculate daily energy
        day_energy = self.core.calculate_daily_energy(year, month, day)

        # Update display
        self.energy_text.config(state="normal")
        self.energy_text.delete("1.0", "end")

        # Format date
        date_str = day_energy.date.strftime("%Y-%m-%d")

        # Add header
        self.energy_text.insert("1.0", f"🔥 Energy Analysis for {date_str} 🔥\n\n")

        # Day information
        stem_branch = day_energy.stem_branch
        self.energy_text.insert("end", f"Day Stem-Branch: {stem_branch.stem}{stem_branch.branch}\n")
        self.energy_text.insert("end", f"Stem Element: {stem_branch.stem_element.value}\n")
        self.energy_text.insert("end", f"Branch Element: {stem_branch.branch_element.value}\n")
        self.energy_text.insert("end", f"Combined Element: {stem_branch.combined_element.value}\n")
        self.energy_text.insert("end", f"Flying Star: {day_energy.flying_star}\n\n")

        # Energy qualities
        self.energy_text.insert("end", "Energy Qualities:\n")
        for quality in day_energy.quality:
            self.energy_text.insert("end", f"- {quality}\n")

        # Element flow
        self.energy_text.insert("end", "\nElement Flow Pattern:\n")
        self.energy_text.insert("end", " → ".join([e.value for e in day_energy.element_flow]))
        self.energy_text.insert("end", "\n\n")

        # Auspicious activities
        self.energy_text.insert("end", "Auspicious Activities:\n")
        for activity in day_energy.auspicious:
            self.energy_text.insert("end", f"- {activity}\n")

        # Challenging influences
        self.energy_text.insert("end", "\nChallenging Influences:\n")
        for challenge in day_energy.challenging:
            self.energy_text.insert("end", f"- {challenge}\n")

        self.energy_text.config(state="disabled")

    def update_bagua(self):
        """Update the bagua diagram."""
        # Get the selected arrangement
        arrangement = self.bagua_var.get()

        # Clear current bagua display
        for widget in self.bagua_display.winfo_children():
            widget.destroy()

        # Create the bagua diagram
        fig = self.visualizer.create_bagua_diagram(arrangement)
        canvas = FigureCanvasTkAgg(fig, master=self.bagua_display)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

# Launch the Xuán Dào application
if __name__ == "__main__":
    root = tk.Tk()
    app = XuanDaoApp(root)
    root.mainloop()