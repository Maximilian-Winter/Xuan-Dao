import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import math
from PIL import Image, ImageDraw, ImageTk


class XuanDaoSystem:
    """
    The Xuan Dao System - A digital representation of the mysterious mechanisms
    that unify Heaven, Earth, and Humanity through numerical patterns and energetic flows.
    """

    def __init__(self):
        # 1. 玄道體系 - Xuan Dao System
        self.xuan_dao_principles = {
            "玄之又玄": "Mystery within mystery",
            "眾妙之門": "Gate of all wonders",
            "天地人三才": "Three talents of Heaven, Earth, and Humanity",
            "顯微無間": "Manifest and subtle without gap",
            "通達玄機": "Penetrating mysterious mechanisms",
            "光明與玄秘之統一": "Unity of light and mystery",
        }

        # 2. 洛書體系 - Lo Shu System
        self.lo_shu_matrix = np.array([
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ])

        self.flying_stars = {
            1: {"name": "一白水星", "element": "water", "quality": "潛伏", "color": "white", "direction": "north"},
            2: {"name": "二黑土星", "element": "earth", "quality": "承載", "color": "black", "direction": "southwest"},
            3: {"name": "三碧木星", "element": "wood", "quality": "生發", "color": "blue", "direction": "east"},
            4: {"name": "四綠木星", "element": "wood", "quality": "漸進", "color": "green", "direction": "southeast"},
            5: {"name": "五黃土星", "element": "earth", "quality": "中正", "color": "yellow", "direction": "center"},
            6: {"name": "六白金星", "element": "metal", "quality": "收斂", "color": "white", "direction": "northwest"},
            7: {"name": "七赤金星", "element": "metal", "quality": "決斷", "color": "red", "direction": "west"},
            8: {"name": "八白土星", "element": "earth", "quality": "穩固", "color": "white", "direction": "northeast"},
            9: {"name": "九紫火星", "element": "fire", "quality": "光明", "color": "purple", "direction": "south"}
        }

        # 3. 八卦體系 - Eight Trigrams System
        self.trigrams = {
            "乾": {"lines": [1, 1, 1], "element": "metal", "quality": "天", "direction": "northwest"},
            "兌": {"lines": [1, 1, 0], "element": "metal", "quality": "澤", "direction": "west"},
            "離": {"lines": [1, 0, 1], "element": "fire", "quality": "火", "direction": "south"},
            "震": {"lines": [0, 1, 1], "element": "wood", "quality": "雷", "direction": "east"},
            "巽": {"lines": [1, 0, 0], "element": "wood", "quality": "風", "direction": "southeast"},
            "坎": {"lines": [0, 1, 0], "element": "water", "quality": "水", "direction": "north"},
            "艮": {"lines": [0, 0, 1], "element": "earth", "quality": "山", "direction": "northeast"},
            "坤": {"lines": [0, 0, 0], "element": "earth", "quality": "地", "direction": "southwest"}
        }

        # Pre-heaven arrangement
        self.pre_heaven_arrangement = ["乾", "兌", "離", "震", "巽", "坎", "艮", "坤"]

        # Post-heaven arrangement
        self.post_heaven_arrangement = ["離", "坤", "震", "巽", "乾", "坎", "艮", "兌"]

        # 4. 五行體系 - Five Phases System
        self.five_phases = {
            "metal": {
                "nature": "收斂、肅降",
                "dynamics": "沉降",
                "color": "white",
                "season": "autumn",
                "direction": "west",
                "generates": "water",
                "controlled_by": "fire"
            },
            "wood": {
                "nature": "生發、條達",
                "dynamics": "升浮",
                "color": "green",
                "season": "spring",
                "direction": "east",
                "generates": "fire",
                "controlled_by": "metal"
            },
            "water": {
                "nature": "寒冷、向下",
                "dynamics": "潛藏",
                "color": "black",
                "season": "winter",
                "direction": "north",
                "generates": "wood",
                "controlled_by": "earth"
            },
            "fire": {
                "nature": "炎熱、向上",
                "dynamics": "飛騰",
                "color": "red",
                "season": "summer",
                "direction": "south",
                "generates": "earth",
                "controlled_by": "water"
            },
            "earth": {
                "nature": "中正、包容",
                "dynamics": "安靜",
                "color": "yellow",
                "season": "late summer",
                "direction": "center",
                "generates": "metal",
                "controlled_by": "wood"
            }
        }

        # 5. 天文曆法體系 - Celestial Calendar System
        self.heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

        self.seasonal_divisions = [
            "立春", "雨水", "驚蟄", "春分", "清明", "穀雨",  # Spring
            "立夏", "小滿", "芒種", "夏至", "小暑", "大暑",  # Summer
            "立秋", "處暑", "白露", "秋分", "寒露", "霜降",  # Autumn
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"  # Winter
        ]

        # Core Themes
        self.core_themes = {
            "天人合一": "Unity of Heaven and Human",
            "陰陽變化": "Yin-Yang Transformations",
            "五行生克": "Five Phases Generation and Control",
            "八卦演易": "Eight Trigrams Evolution",
            "九宮飛星": "Nine Palaces Flying Stars",
            "時空能量": "Time-Space Energetics",
            "玄機妙用": "Mysterious Mechanism Applications",
            "修真證道": "Cultivation and Verification of the Way"
        }

        # 玄道印心 - Xuan Dao Heart Seal
        self.heart_seal = """
        玄之又玄 眾妙之門
        天地人合 五行八卦
        九宮洛書 時空無礙
        得此道者 明察秋毫
        """

        # Initialize the relationships matrix
        self.initialize_relationships()

    def initialize_relationships(self):
        """Initialize the relationships between different systems."""
        # Mapping between trigrams and flying stars
        self.trigram_star_mapping = {
            "乾": 6,  # Northwest - Six White Metal Star
            "兌": 7,  # West - Seven Red Metal Star
            "離": 9,  # South - Nine Purple Fire Star
            "震": 3,  # East - Three Azure Wood Star
            "巽": 4,  # Southeast - Four Green Wood Star
            "坎": 1,  # North - One White Water Star
            "艮": 8,  # Northeast - Eight White Earth Star
            "坤": 2,  # Southwest - Two Black Earth Star
        }

        # Mapping between stems and phases
        self.stem_phase_mapping = {
            "甲": "wood", "乙": "wood",
            "丙": "fire", "丁": "fire",
            "戊": "earth", "己": "earth",
            "庚": "metal", "辛": "metal",
            "壬": "water", "癸": "water"
        }

        # Mapping between branches and phases
        self.branch_phase_mapping = {
            "寅": "wood", "卯": "wood",
            "巳": "fire", "午": "fire",
            "辰": "earth", "未": "earth", "戌": "earth", "丑": "earth",
            "申": "metal", "酉": "metal",
            "亥": "water", "子": "water"
        }

    def get_flying_star_by_position(self, row, col):
        """Get the flying star number at a specific position in the Lo Shu square."""
        return self.lo_shu_matrix[row, col]

    def get_star_info(self, star_number):
        """Get information about a specific flying star."""
        return self.flying_stars[star_number]

    def get_trigram_lines(self, trigram_name):
        """Get the line configuration for a trigram."""
        return self.trigrams[trigram_name]["lines"]

    def get_phase_info(self, phase_name):
        """Get information about a specific phase."""
        return self.five_phases[phase_name]

    def get_generating_cycle(self):
        """Get the generating (mutual production) cycle of the five phases."""
        return ["wood", "fire", "earth", "metal", "water", "wood"]

    def get_controlling_cycle(self):
        """Get the controlling (mutual overcoming) cycle of the five phases."""
        return ["wood", "earth", "water", "fire", "metal", "wood"]

    def get_sixty_jiazi_cycle(self):
        """Get the sixty combinations of Heavenly Stems and Earthly Branches."""
        cycle = []
        for i in range(60):
            stem_idx = i % 10
            branch_idx = i % 12
            cycle.append(f"{self.heavenly_stems[stem_idx]}{self.earthly_branches[branch_idx]}")
        return cycle

    def calculate_flying_star_chart(self, facing_direction, period_number=8):
        """
        Calculate a flying star chart based on facing direction and period.

        This is a simplified version for demonstration purposes.
        In actual practice, this would involve more complex calculations.
        """
        # Base chart (center is always 5)
        base_chart = np.copy(self.lo_shu_matrix)

        # Adjust for period
        period_adjustment = period_number - 5
        adjusted_chart = (base_chart + period_adjustment) % 9
        adjusted_chart[adjusted_chart == 0] = 9

        # Simulate adjustment for facing direction (simplified)
        # In reality, this would involve complex calculations based on actual compass degrees
        direction_map = {
            "north": 0,
            "northeast": 1,
            "east": 2,
            "southeast": 3,
            "south": 4,
            "southwest": 5,
            "west": 6,
            "northwest": 7
        }

        if facing_direction in direction_map:
            direction_adjustment = direction_map[facing_direction]
            for _ in range(direction_adjustment):
                # Rotate the chart (simplified)
                adjusted_chart = np.rot90(adjusted_chart)

        return adjusted_chart

    def generate_hexagram(self):
        """Generate a random hexagram."""
        lines = []
        hexagram_number = 0

        for i in range(6):
            # 0: yin, 1: yang
            line = random.randint(0, 1)
            lines.append(line)
            hexagram_number += line * (2 ** i)

        # Return the lines and the corresponding hexagram number (0-63)
        return lines, hexagram_number

    def analyze_hexagram(self, lines):
        """Analyze a hexagram into its component trigrams."""
        lower_trigram = lines[0:3]
        upper_trigram = lines[3:6]

        # Find the trigram names
        lower_name = ""
        upper_name = ""

        for name, trigram in self.trigrams.items():
            if trigram["lines"] == lower_trigram:
                lower_name = name
            if trigram["lines"] == upper_trigram:
                upper_name = name

        return lower_name, upper_name

    def get_trigram_associations(self, trigram_name):
        """Get the associations for a specific trigram."""
        if trigram_name in self.trigrams:
            return self.trigrams[trigram_name]
        return None

    def calculate_element_balance(self, birth_year, birth_month, birth_day):
        """
        Calculate a person's element balance based on birth date.
        This is a simplified version for demonstration purposes.
        """
        # Calculate heavenly stem and earthly branch for the year
        stem_idx = (birth_year - 4) % 10
        branch_idx = (birth_year - 4) % 12

        year_stem = self.heavenly_stems[stem_idx]
        year_branch = self.earthly_branches[branch_idx]

        # Get the elements
        year_stem_element = self.stem_phase_mapping[year_stem]
        year_branch_element = self.branch_phase_mapping[year_branch]

        # Simple month element (simplified)
        month_elements = ["water", "water", "wood", "wood", "earth",
                          "fire", "fire", "earth", "metal", "metal", "earth", "water"]
        month_element = month_elements[birth_month - 1]

        # Simple day element (very simplified)
        day_element = self.five_phases[month_element]["generates"]

        # Count elements
        element_count = {
            "wood": 0,
            "fire": 0,
            "earth": 0,
            "metal": 0,
            "water": 0
        }

        element_count[year_stem_element] += 2
        element_count[year_branch_element] += 2
        element_count[month_element] += 1
        element_count[day_element] += 1

        return element_count

    def find_missing_elements(self, element_count):
        """Find missing or deficient elements based on element count."""
        missing = []

        for element, count in element_count.items():
            if count == 0:
                missing.append(element)
            elif count < 2:
                missing.append(element + " (weak)")

        return missing

    def suggest_balancing_strategies(self, missing_elements):
        """Suggest strategies to balance missing elements."""
        suggestions = []

        element_suggestions = {
            "wood": [
                "Incorporate more green colors",
                "Place plants in the east and southeast",
                "Use rectangular shapes and tall vertical objects",
                "Work with wood materials"
            ],
            "fire": [
                "Add more red colors",
                "Place lights and candles in the south",
                "Use triangular shapes",
                "Work with lively, vibrant designs"
            ],
            "earth": [
                "Incorporate more yellow and brown colors",
                "Place stable objects in the center, southwest and northeast",
                "Use square shapes",
                "Work with ceramic and clay materials"
            ],
            "metal": [
                "Add more white and metallic colors",
                "Place metal objects in the west and northwest",
                "Use circular and oval shapes",
                "Work with metal materials"
            ],
            "water": [
                "Incorporate more blue and black colors",
                "Place water features in the north",
                "Use wavy, flowing shapes",
                "Work with glass and reflective materials"
            ]
        }

        for element in missing_elements:
            element_clean = element.split(" ")[0]  # Remove "(weak)" if present
            if element_clean in element_suggestions:
                suggestions.extend(element_suggestions[element_clean])

        return suggestions

    def calculate_daily_energy(self, current_year, current_month, current_day):
        """
        Calculate the energetic quality of a specific day.
        This is a simplified demonstration version.
        """
        # Calculate the stem and branch for the day
        day_number = (current_year * 365 + current_month * 30 + current_day) % 60

        stem_idx = day_number % 10
        branch_idx = day_number % 12

        day_stem = self.heavenly_stems[stem_idx]
        day_branch = self.earthly_branches[branch_idx]

        # Get the elements
        day_stem_element = self.stem_phase_mapping[day_stem]
        day_branch_element = self.branch_phase_mapping[day_branch]

        # Determine the energy quality
        energy_quality = []

        # Element interaction (simplified)
        if day_stem_element == day_branch_element:
            energy_quality.append("Strong elemental harmony")
        elif day_stem_element == self.five_phases[day_branch_element]["generates"]:
            energy_quality.append("Productive, generative energy")
        elif day_stem_element == self.five_phases[day_branch_element]["controlled_by"]:
            energy_quality.append("Controlling, restrictive energy")
        else:
            energy_quality.append("Mixed, complex energy")

        # Season alignment (simplified)
        month_seasons = ["winter", "winter", "spring", "spring", "spring",
                         "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
        current_season = month_seasons[current_month - 1]

        stem_season = self.five_phases[day_stem_element]["season"]
        if current_season == stem_season:
            energy_quality.append("In season, naturally supported energy")
        elif current_season == self.five_phases[day_stem_element]["controlled_by"]:
            energy_quality.append("Against seasonal energy, requiring adaptation")

        return {
            "day_stem": day_stem,
            "day_branch": day_branch,
            "stem_element": day_stem_element,
            "branch_element": day_branch_element,
            "energy_quality": energy_quality
        }

    def suggest_auspicious_activities(self, day_energy):
        """Suggest auspicious activities based on day energy."""
        activities = []

        # Based on stem element
        element_activities = {
            "wood": ["Planning", "Starting projects", "Growth-oriented activities", "Planting", "Healing"],
            "fire": ["Celebration", "Promotion", "Marketing", "Social gatherings", "Inspiration"],
            "earth": ["Stabilizing", "Organizing", "Building foundations", "Nurturing", "Education"],
            "metal": ["Refining", "Cutting away excess", "Harvesting", "Seeking clarity", "Precision work"],
            "water": ["Reflection", "Exploration", "Risk-taking", "Research", "Flowing with change"]
        }

        stem_element = day_energy["stem_element"]
        activities.extend(element_activities[stem_element])

        # Based on energy quality
        if "Strong elemental harmony" in day_energy["energy_quality"]:
            activities.append("Activities requiring focused concentration")
        if "Productive, generative energy" in day_energy["energy_quality"]:
            activities.append("Creative endeavors")
        if "In season, naturally supported energy" in day_energy["energy_quality"]:
            activities.append("Working with natural cycles")

        return activities

    def generate_lo_shu_grid(self):
        """Generate a visual representation of the Lo Shu grid."""
        # Create a grid
        fig, ax = plt.subplots(figsize=(8, 8))

        # Hide axes
        ax.axis('off')

        # Draw grid
        for i in range(4):
            ax.axhline(i * 1 / 3, color='black', linewidth=2)
            ax.axvline(i * 1 / 3, color='black', linewidth=2)

        # Fill in the numbers
        for i in range(3):
            for j in range(3):
                number = self.lo_shu_matrix[i, j]
                star = self.flying_stars[number]
                element = star["element"]

                # Choose color based on element
                element_colors = {
                    "water": "blue",
                    "earth": "brown",
                    "wood": "green",
                    "metal": "gray",
                    "fire": "red"
                }

                color = element_colors[element]

                # Add number and element name
                ax.text(j / 3 + 1 / 6, 1 - (i / 3 + 1 / 6), f"{number}\n{star['name']}\n{element}",
                        ha='center', va='center', fontsize=12, color=color)

        return fig

    def generate_eight_trigrams_diagram(self, arrangement="pre-heaven"):
        """Generate a visual representation of the Eight Trigrams diagram."""
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide axes
        ax.axis('off')

        # Draw circle
        circle = plt.Circle((0.5, 0.5), 0.45, fill=False, color='black', linewidth=2)
        ax.add_patch(circle)

        # Draw inner circle
        inner_circle = plt.Circle((0.5, 0.5), 0.1, fill=True, color='black' if arrangement == "pre-heaven" else "white")
        ax.add_patch(inner_circle)

        if arrangement == "pre-heaven":
            # White for yang, black for yin in center
            yin_yang = plt.Circle((0.5, 0.5), 0.05, fill=True, color='white')
            ax.add_patch(yin_yang)
        else:
            # Black for yin, white for yang in center
            yin_yang = plt.Circle((0.5, 0.5), 0.05, fill=True, color='black')
            ax.add_patch(yin_yang)

        # Choose arrangement
        if arrangement == "pre-heaven":
            trigram_arrangement = self.pre_heaven_arrangement
            title = "先天八卦圖 - Pre-Heaven Arrangement"
        else:
            trigram_arrangement = self.post_heaven_arrangement
            title = "後天八卦圖 - Post-Heaven Arrangement"

        # Draw trigrams at positions around the circle
        for i, trigram_name in enumerate(trigram_arrangement):
            angle = i * 45 * (math.pi / 180)  # Convert degrees to radians

            # Calculate position on the circle
            x = 0.5 + 0.38 * math.sin(angle)
            y = 0.5 + 0.38 * math.cos(angle)

            # Get trigram lines
            lines = self.trigrams[trigram_name]["lines"]

            # Draw the trigram
            for j, line in enumerate(lines):
                # Calculate line start and end positions
                line_length = 0.06
                line_spacing = 0.02

                line_y = y + (j - 1) * (line_length + line_spacing)

                if line == 1:  # Yang line (solid)
                    ax.plot([x - line_length, x + line_length], [line_y, line_y], 'k-', linewidth=2)
                else:  # Yin line (broken)
                    ax.plot([x - line_length, x - line_length / 3], [line_y, line_y], 'k-', linewidth=2)
                    ax.plot([x + line_length / 3, x + line_length], [line_y, line_y], 'k-', linewidth=2)

            # Add trigram name
            name_distance = 0.35
            name_x = 0.5 + name_distance * math.sin(angle)
            name_y = 0.5 + name_distance * math.cos(angle)

            ax.text(name_x, name_y, trigram_name, ha='center', va='center', fontsize=14)

        # Add title
        ax.set_title(title, fontsize=16)

        # Set limits
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        return fig

    def generate_five_phases_diagram(self):
        """Generate a visual representation of the Five Phases and their relationships."""
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide axes
        ax.axis('off')

        # Define positions for the five phases (on a pentagon)
        positions = {
            "wood": (0.8, 0.65),
            "fire": (0.65, 0.9),
            "earth": (0.5, 0.5),
            "metal": (0.35, 0.9),
            "water": (0.2, 0.65)
        }

        # Define colors for the five phases
        colors = {
            "wood": "green",
            "fire": "red",
            "earth": "brown",
            "metal": "gray",
            "water": "blue"
        }

        # Draw circles for each phase
        for phase, pos in positions.items():
            circle = plt.Circle(pos, 0.1, fill=True, color=colors[phase], alpha=0.7)
            ax.add_patch(circle)

            # Add phase name
            ax.text(pos[0], pos[1], phase.capitalize(), ha='center', va='center', fontsize=12, color='white')

        # Draw generating cycle (outer pentagon)
        generating_cycle = self.get_generating_cycle()

        for i in range(len(generating_cycle) - 1):
            phase1 = generating_cycle[i]
            phase2 = generating_cycle[i + 1]

            # Draw arrow
            ax.annotate("", xy=positions[phase2], xytext=positions[phase1],
                        arrowprops=dict(facecolor='green', shrink=0.1, width=1.5, headwidth=7))

        # Draw controlling cycle (inner star)
        controlling_cycle = self.get_controlling_cycle()

        for i in range(len(controlling_cycle) - 1):
            phase1 = controlling_cycle[i]
            phase2 = controlling_cycle[i + 1]

            # Draw arrow
            ax.annotate("", xy=positions[phase2], xytext=positions[phase1],
                        arrowprops=dict(facecolor='red', shrink=0.1, width=1.5, headwidth=7,
                                        linestyle='dashed'))

        # Add title
        ax.set_title("五行相生相剋圖 - Five Phases Generation and Control Diagram", fontsize=16)

        return fig


class XuanDaoApp:
    """
    A GUI application for exploring the Xuan Dao System.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("玄道探索系統 - Xuan Dao Explorer")
        self.root.geometry("1100x800")

        # Create a Xuan Dao system instance
        self.xuan_dao_system = XuanDaoSystem()

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create tabs
        self.create_overview_tab()
        self.create_lo_shu_tab()
        self.create_trigrams_tab()
        self.create_five_phases_tab()
        self.create_divination_tab()
        self.create_calendar_tab()

    def create_overview_tab(self):
        """Create the overview tab."""
        overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(overview_frame, text="玄道總覽 (Overview)")

        # Create title
        title_label = ttk.Label(overview_frame, text="玄道體系探索 - Xuan Dao System Explorer",
                                font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        # Create heart seal frame
        heart_seal_frame = ttk.LabelFrame(overview_frame, text="玄道印心 - Xuan Dao Heart Seal")
        heart_seal_frame.pack(fill=tk.X, padx=20, pady=10)

        heart_seal_text = scrolledtext.ScrolledText(heart_seal_frame, wrap=tk.WORD, height=6)
        heart_seal_text.pack(fill=tk.X, padx=10, pady=10)
        heart_seal_text.insert(tk.END, self.xuan_dao_system.heart_seal)
        heart_seal_text.config(state=tk.DISABLED)

        # Create subsystems frame
        subsystems_frame = ttk.LabelFrame(overview_frame, text="五大體系 - Five Major Systems")
        subsystems_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        systems = [
            ("1. 玄道體系 - Xuan Dao System",
             "Mystery within mystery, gate of all wonders. The unified way of Heaven, Earth, and Humanity."),
            ("2. 洛書體系 - Lo Shu System",
             "Nine palace numerical structure with flying stars from One White to Nine Purple. The mathematical matrix of transformation."),
            ("3. 八卦體系 - Eight Trigrams System",
             "The eight trigrams of Qian, Dui, Li, Zhen, Xun, Kan, Gen, and Kun represent fundamental cosmic patterns."),
            ("4. 五行體系 - Five Phases System",
             "The five phases of Metal, Wood, Water, Fire, and Earth create cycles of generation and control."),
            ("5. 天文曆法體系 - Celestial Calendar System",
             "Movements of celestial bodies and the twenty-four seasonal divisions track cosmic time patterns.")
        ]

        for i, (title, description) in enumerate(systems):
            frame = ttk.Frame(subsystems_frame)
            frame.pack(fill=tk.X, padx=10, pady=5)

            title_label = ttk.Label(frame, text=title, font=("Arial", 12, "bold"))
            title_label.pack(anchor=tk.W)

            desc_label = ttk.Label(frame, text=description, wraplength=600)
            desc_label.pack(anchor=tk.W, padx=20)

        # Create core themes frame
        themes_frame = ttk.LabelFrame(overview_frame, text="核心主題 - Core Themes")
        themes_frame.pack(fill=tk.X, padx=20, pady=10)

        themes_text = ""
        for chinese, english in self.xuan_dao_system.core_themes.items():
            themes_text += f"{chinese} - {english}\n"

        themes_label = ttk.Label(themes_frame, text=themes_text, justify=tk.LEFT)
        themes_label.pack(anchor=tk.W, padx=10, pady=10)

    def create_lo_shu_tab(self):
        """Create the Lo Shu tab."""
        lo_shu_frame = ttk.Frame(self.notebook)
        self.notebook.add(lo_shu_frame, text="洛書九宮 (Lo Shu)")

        # Create title
        title_label = ttk.Label(lo_shu_frame, text="洛書九宮 - Lo Shu Nine Palaces",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create description
        desc_text = """
        The Lo Shu (洛書) or "Scroll of the River Luo" is a magical 3x3 grid of numbers that forms 
        a perfect magic square where each row, column, and diagonal sums to 15. It is said to have 
        emerged from the back of a divine turtle in the Luo River during ancient times.

        This mystical numerical configuration represents the perfect balance of cosmic forces and serves 
        as the foundation for the Flying Stars (飛星) system, which maps energetic patterns across 
        space and time.
        """

        desc_label = ttk.Label(lo_shu_frame, text=desc_text, wraplength=800, justify=tk.CENTER)
        desc_label.pack(pady=10)

        # Create main content frame with two columns
        content_frame = ttk.Frame(lo_shu_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left column - Lo Shu diagram
        left_frame = ttk.LabelFrame(content_frame, text="洛書圖 - Lo Shu Diagram")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Generate Lo Shu diagram
        fig = self.xuan_dao_system.generate_lo_shu_grid()

        # Convert matplotlib figure to tkinter canvas
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=left_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Right column - Flying Stars information
        right_frame = ttk.LabelFrame(content_frame, text="飛星九宮 - Flying Stars")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create scrolled text widget for flying stars info
        stars_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, height=20)
        stars_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add information about each flying star
        for i in range(1, 10):
            star = self.xuan_dao_system.flying_stars[i]
            stars_text.insert(tk.END, f"{i}. {star['name']} - {star['element'].capitalize()} Star\n")
            stars_text.insert(tk.END, f"   Element: {star['element'].capitalize()}\n")
            stars_text.insert(tk.END, f"   Quality: {star['quality']}\n")
            stars_text.insert(tk.END, f"   Color: {star['color'].capitalize()}\n")
            stars_text.insert(tk.END, f"   Direction: {star['direction'].capitalize()}\n\n")

        stars_text.config(state=tk.DISABLED)

        # Create flying star chart calculator
        calc_frame = ttk.LabelFrame(lo_shu_frame, text="飛星盤計算 - Flying Star Chart Calculator")
        calc_frame.pack(fill=tk.X, padx=20, pady=10)

        form_frame = ttk.Frame(calc_frame)
        form_frame.pack(padx=10, pady=10)

        # Facing direction
        ttk.Label(form_frame, text="Facing Direction:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        directions = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]
        self.direction_var = tk.StringVar(value=directions[0])
        direction_combo = ttk.Combobox(form_frame, textvariable=self.direction_var, values=directions)
        direction_combo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Period number
        ttk.Label(form_frame, text="Period Number (1-9):").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.period_var = tk.IntVar(value=8)
        period_combo = ttk.Combobox(form_frame, textvariable=self.period_var, values=list(range(1, 10)))
        period_combo.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        # Calculate button
        calc_button = ttk.Button(form_frame, text="Calculate Chart", command=self.calculate_flying_star_chart)
        calc_button.grid(row=0, column=4, padx=20, pady=5)

        # Frame for result
        self.chart_result_frame = ttk.LabelFrame(calc_frame, text="Chart Result")
        self.chart_result_frame.pack(fill=tk.X, padx=10, pady=10)

        # Initial empty label for result
        self.chart_result_label = ttk.Label(self.chart_result_frame, text="Chart will appear here after calculation")
        self.chart_result_label.pack(padx=10, pady=10)

    def calculate_flying_star_chart(self):
        """Calculate and display the flying star chart."""
        direction = self.direction_var.get()
        period = self.period_var.get()

        # Calculate the chart
        chart = self.xuan_dao_system.calculate_flying_star_chart(direction, period)

        # Clear previous result
        for widget in self.chart_result_frame.winfo_children():
            widget.destroy()

        # Create grid of labels to display the chart
        for i in range(3):
            for j in range(3):
                number = chart[i, j]
                star = self.xuan_dao_system.flying_stars[number]

                cell_frame = ttk.Frame(self.chart_result_frame, borderwidth=1, relief=tk.GROOVE)
                cell_frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

                # Configure the grid to expand cells evenly
                self.chart_result_frame.columnconfigure(j, weight=1)
                self.chart_result_frame.rowconfigure(i, weight=1)

                # Add star information to cell
                ttk.Label(cell_frame, text=str(number), font=("Arial", 14, "bold")).pack(pady=2)
                ttk.Label(cell_frame, text=star["name"]).pack(pady=1)
                ttk.Label(cell_frame, text=f"Element: {star['element'].capitalize()}").pack(pady=1)

        # Add explanation
        explanation = ttk.Label(self.chart_result_frame,
                                text=f"Flying Star Chart for {direction.capitalize()} facing building in Period {period}",
                                wraplength=600)
        explanation.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def create_trigrams_tab(self):
        """Create the Eight Trigrams tab."""
        trigrams_frame = ttk.Frame(self.notebook)
        self.notebook.add(trigrams_frame, text="八卦系統 (Bagua)")

        # Create title
        title_label = ttk.Label(trigrams_frame, text="八卦系統 - Eight Trigrams System",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create description
        desc_text = """
        The Eight Trigrams (八卦, Bagua) are fundamental symbols in Daoist cosmology representing 
        the building blocks of reality. Each trigram consists of three lines (爻, yao) that can be 
        either solid (Yang) or broken (Yin).

        There are two main arrangements of the trigrams:
        1. The Pre-Heaven Arrangement (先天八卦) - Representing the cosmic ideal order
        2. The Post-Heaven Arrangement (後天八卦) - Representing the manifest world
        """

        desc_label = ttk.Label(trigrams_frame, text=desc_text, wraplength=800, justify=tk.CENTER)
        desc_label.pack(pady=10)

        # Create tabs for different trigram arrangements
        trigram_notebook = ttk.Notebook(trigrams_frame)
        trigram_notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Pre-Heaven tab
        pre_heaven_frame = ttk.Frame(trigram_notebook)
        trigram_notebook.add(pre_heaven_frame, text="先天八卦 (Pre-Heaven)")

        # Generate Pre-Heaven diagram
        fig_pre = self.xuan_dao_system.generate_eight_trigrams_diagram("pre-heaven")

        # Convert matplotlib figure to tkinter canvas
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas_pre = FigureCanvasTkAgg(fig_pre, master=pre_heaven_frame)
        canvas_pre.draw()
        canvas_pre.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Post-Heaven tab
        post_heaven_frame = ttk.Frame(trigram_notebook)
        trigram_notebook.add(post_heaven_frame, text="後天八卦 (Post-Heaven)")

        # Generate Post-Heaven diagram
        fig_post = self.xuan_dao_system.generate_eight_trigrams_diagram("post-heaven")

        # Convert matplotlib figure to tkinter canvas
        canvas_post = FigureCanvasTkAgg(fig_post, master=post_heaven_frame)
        canvas_post.draw()
        canvas_post.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Trigram details tab
        details_frame = ttk.Frame(trigram_notebook)
        trigram_notebook.add(details_frame, text="卦象詳解 (Trigram Details)")

        # Create scrolled text widget for trigram details
        trigram_text = scrolledtext.ScrolledText(details_frame, wrap=tk.WORD, height=20)
        trigram_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add information about each trigram
        for trigram, info in self.xuan_dao_system.trigrams.items():
            # Convert binary lines to symbols
            line_symbols = []
            for line in info["lines"]:
                if line == 1:
                    line_symbols.append("— (Yang)")
                else:
                    line_symbols.append("- - (Yin)")

            line_text = "\n".join(line_symbols)

            trigram_text.insert(tk.END, f"{trigram} - {info['quality']}\n")
            trigram_text.insert(tk.END, f"Lines:\n{line_text}\n")
            trigram_text.insert(tk.END, f"Element: {info['element'].capitalize()}\n")
            trigram_text.insert(tk.END, f"Direction: {info['direction'].capitalize()}\n")
            trigram_text.insert(tk.END,
                                f"Associated Flying Star: {self.xuan_dao_system.trigram_star_mapping[trigram]}\n\n")

        trigram_text.config(state=tk.DISABLED)

        # I Ching divination teaser
        divination_frame = ttk.LabelFrame(trigrams_frame, text="易經占卜 - I Ching Divination")
        divination_frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(divination_frame,
                  text="The Eight Trigrams combine to form the 64 hexagrams used in I Ching divination.\nVisit the Divination tab to explore this further.",
                  justify=tk.CENTER).pack(pady=10)

    def create_five_phases_tab(self):
        """Create the Five Phases tab."""
        phases_frame = ttk.Frame(self.notebook)
        self.notebook.add(phases_frame, text="五行系統 (Wu Xing)")

        # Create title
        title_label = ttk.Label(phases_frame, text="五行系統 - Five Phases System",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create description
        desc_text = """
        The Five Phases (五行, Wu Xing) system describes the fundamental energetic states that compose 
        all phenomena in the universe: Wood (木), Fire (火), Earth (土), Metal (金), and Water (水).

        These phases are not static elements but dynamic processes that constantly transform into one another
        through cycles of generation (相生) and control (相剋).
        """

        desc_label = ttk.Label(phases_frame, text=desc_text, wraplength=800, justify=tk.CENTER)
        desc_label.pack(pady=10)

        # Create main content frame with diagram and details
        content_frame = ttk.Frame(phases_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left side - Five Phases diagram
        left_frame = ttk.LabelFrame(content_frame, text="五行圖 - Five Phases Diagram")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Generate Five Phases diagram
        fig = self.xuan_dao_system.generate_five_phases_diagram()

        # Convert matplotlib figure to tkinter canvas
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=left_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Right side - Five Phases details
        right_frame = ttk.LabelFrame(content_frame, text="五行詳解 - Five Phases Details")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create scrolled text widget for phase details
        phases_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, height=20)
        phases_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Add information about each phase
        for phase, info in self.xuan_dao_system.five_phases.items():
            phases_text.insert(tk.END, f"{phase.capitalize()}\n")
            phases_text.insert(tk.END, f"- Nature: {info['nature']}\n")
            phases_text.insert(tk.END, f"- Dynamics: {info['dynamics']}\n")
            phases_text.insert(tk.END, f"- Color: {info['color'].capitalize()}\n")
            phases_text.insert(tk.END, f"- Season: {info['season'].capitalize()}\n")
            phases_text.insert(tk.END, f"- Direction: {info['direction'].capitalize()}\n")
            phases_text.insert(tk.END, f"- Generates: {info['generates'].capitalize()}\n")
            phases_text.insert(tk.END, f"- Controlled by: {info['controlled_by'].capitalize()}\n\n")

        phases_text.config(state=tk.DISABLED)

        # Element balance analyzer
        analyzer_frame = ttk.LabelFrame(phases_frame, text="五行平衡分析 - Element Balance Analyzer")
        analyzer_frame.pack(fill=tk.X, padx=20, pady=10)

        form_frame = ttk.Frame(analyzer_frame)
        form_frame.pack(padx=10, pady=10)

        # Birth date inputs
        ttk.Label(form_frame, text="Enter Birth Date:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Year
        ttk.Label(form_frame, text="Year:").grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.year_var = tk.IntVar(value=1985)
        year_entry = ttk.Entry(form_frame, textvariable=self.year_var, width=6)
        year_entry.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        # Month
        ttk.Label(form_frame, text="Month:").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.month_var = tk.IntVar(value=1)
        month_combo = ttk.Combobox(form_frame, textvariable=self.month_var, values=list(range(1, 13)), width=3)
        month_combo.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)

        # Day
        ttk.Label(form_frame, text="Day:").grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
        self.day_var = tk.IntVar(value=1)
        day_combo = ttk.Combobox(form_frame, textvariable=self.day_var, values=list(range(1, 32)), width=3)
        day_combo.grid(row=0, column=6, padx=5, pady=5, sticky=tk.W)

        # Analyze button
        analyze_button = ttk.Button(form_frame, text="Analyze Elements", command=self.analyze_element_balance)
        analyze_button.grid(row=0, column=7, padx=20, pady=5)

        # Frame for results
        results_frame = ttk.Frame(analyzer_frame)
        results_frame.pack(fill=tk.X, padx=10, pady=10)

        # Element count display
        self.element_count_frame = ttk.LabelFrame(results_frame, text="Element Distribution")
        self.element_count_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Initial empty label
        self.element_count_label = ttk.Label(self.element_count_frame, text="Distribution will appear here")
        self.element_count_label.pack(padx=10, pady=10)

        # Recommendations display
        self.recommendations_frame = ttk.LabelFrame(results_frame, text="Balancing Recommendations")
        self.recommendations_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Initial empty label
        self.recommendations_label = ttk.Label(self.recommendations_frame, text="Recommendations will appear here")
        self.recommendations_label.pack(padx=10, pady=10)

    def analyze_element_balance(self):
        """Analyze and display the element balance based on birth date."""
        try:
            year = self.year_var.get()
            month = self.month_var.get()
            day = self.day_var.get()

            # Calculate element balance
            element_count = self.xuan_dao_system.calculate_element_balance(year, month, day)

            # Find missing or deficient elements
            missing_elements = self.xuan_dao_system.find_missing_elements(element_count)

            # Get balancing suggestions
            suggestions = self.xuan_dao_system.suggest_balancing_strategies(missing_elements)

            # Update element count display
            count_text = "Element Distribution:\n\n"
            for element, count in element_count.items():
                count_text += f"{element.capitalize()}: {count}\n"

            # Clear previous results
            for widget in self.element_count_frame.winfo_children():
                widget.destroy()

            count_label = ttk.Label(self.element_count_frame, text=count_text, justify=tk.LEFT)
            count_label.pack(padx=10, pady=10, anchor=tk.W)

            # Update recommendations display
            recommendations_text = "Missing or Deficient Elements:\n"
            if missing_elements:
                for element in missing_elements:
                    recommendations_text += f"- {element.capitalize()}\n"
            else:
                recommendations_text += "- None, your elements are well-balanced\n"

            recommendations_text += "\nBalancing Recommendations:\n"
            if suggestions:
                for suggestion in suggestions:
                    recommendations_text += f"- {suggestion}\n"
            else:
                recommendations_text += "- No specific recommendations needed\n"

            # Clear previous results
            for widget in self.recommendations_frame.winfo_children():
                widget.destroy()

            recommendations_label = ttk.Label(self.recommendations_frame, text=recommendations_text,
                                              justify=tk.LEFT, wraplength=400)
            recommendations_label.pack(padx=10, pady=10, anchor=tk.W)

        except Exception as e:
            # Show error message
            for widget in self.element_count_frame.winfo_children():
                widget.destroy()

            error_label = ttk.Label(self.element_count_frame,
                                    text=f"Error: {str(e)}\nPlease enter valid date values.",
                                    foreground="red")
            error_label.pack(padx=10, pady=10)

    def create_divination_tab(self):
        """Create the divination tab."""
        divination_frame = ttk.Frame(self.notebook)
        self.notebook.add(divination_frame, text="占卜系統 (Divination)")

        # Create title
        title_label = ttk.Label(divination_frame, text="易經占卜 - I Ching Divination",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create description
        desc_text = """
        The I Ching (易經), or Book of Changes, is one of the oldest divination systems in the world.
        It combines the Eight Trigrams into 64 hexagrams (六十四卦) that represent all possible 
        situations and their transformations.

        Consulting the I Ching traditionally involves ritual preparation, forming a question, and then 
        casting yarrow stalks or coins to generate a hexagram pattern, which is then interpreted.
        """

        desc_label = ttk.Label(divination_frame, text=desc_text, wraplength=800, justify=tk.CENTER)
        desc_label.pack(pady=10)

        # Create divination interface
        interface_frame = ttk.Frame(divination_frame)
        interface_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left side - Question and casting
        left_frame = ttk.LabelFrame(interface_frame, text="问卜 - Consultation")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Question entry
        question_frame = ttk.Frame(left_frame)
        question_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(question_frame, text="Enter your question:").pack(anchor=tk.W)

        self.question_var = tk.StringVar()
        question_entry = ttk.Entry(question_frame, textvariable=self.question_var, width=50)
        question_entry.pack(fill=tk.X, pady=5)

        # Cast button
        cast_button = ttk.Button(question_frame, text="Cast Hexagram", command=self.cast_hexagram)
        cast_button.pack(pady=10)

        # Hexagram display
        hexagram_frame = ttk.LabelFrame(left_frame, text="卦象 - Hexagram")
        hexagram_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.hexagram_canvas = tk.Canvas(hexagram_frame, width=200, height=300, bg="white")
        self.hexagram_canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Right side - Interpretation
        right_frame = ttk.LabelFrame(interface_frame, text="卦義 - Interpretation")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Interpretation text
        self.interpretation_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, height=20)
        self.interpretation_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Initial text
        self.interpretation_text.insert(tk.END, "Cast a hexagram to receive an interpretation...")
        self.interpretation_text.config(state=tk.DISABLED)

    def cast_hexagram(self):
        """Cast a hexagram and display the result."""
        # Get question
        question = self.question_var.get()

        # Generate hexagram
        lines, hexagram_number = self.xuan_dao_system.generate_hexagram()

        # Analyze trigrams
        lower_trigram, upper_trigram = self.xuan_dao_system.analyze_hexagram(lines)

        # Clear canvas
        self.hexagram_canvas.delete("all")

        # Draw hexagram
        line_length = 120
        line_spacing = 30
        start_x = 50
        start_y = 50

        for i, line in enumerate(reversed(lines)):  # Drawing from bottom to top
            y_pos = start_y + i * line_spacing

            if line == 1:  # Yang line (solid)
                self.hexagram_canvas.create_line(start_x, y_pos, start_x + line_length, y_pos, width=3)
            else:  # Yin line (broken)
                self.hexagram_canvas.create_line(start_x, y_pos, start_x + line_length / 2 - 5, y_pos, width=3)
                self.hexagram_canvas.create_line(start_x + line_length / 2 + 5, y_pos, start_x + line_length, y_pos,
                                                 width=3)

        # Label the trigrams
        upper_y = start_y + 3 * line_spacing + 20
        lower_y = start_y + 6 * line_spacing + 20

        self.hexagram_canvas.create_text(start_x + line_length / 2, upper_y,
                                         text=f"Upper Trigram: {upper_trigram}", font=("Arial", 10))
        self.hexagram_canvas.create_text(start_x + line_length / 2, lower_y,
                                         text=f"Lower Trigram: {lower_trigram}", font=("Arial", 10))

        # Update interpretation
        self.interpretation_text.config(state=tk.NORMAL)
        self.interpretation_text.delete(1.0, tk.END)

        # Create interpretation text
        interpretation = ""

        if question:
            interpretation += f"Question: {question}\n\n"

        interpretation += f"Hexagram Number: {hexagram_number}\n"
        interpretation += f"Composition: {upper_trigram} (upper) over {lower_trigram} (lower)\n\n"

        # Add trigram meanings
        upper_info = self.xuan_dao_system.get_trigram_associations(upper_trigram)
        lower_info = self.xuan_dao_system.get_trigram_associations(lower_trigram)

        interpretation += "Upper Trigram Qualities:\n"
        interpretation += f"- Element: {upper_info['element'].capitalize()}\n"
        interpretation += f"- Quality: {upper_info['quality']}\n"
        interpretation += f"- Direction: {upper_info['direction'].capitalize()}\n\n"

        interpretation += "Lower Trigram Qualities:\n"
        interpretation += f"- Element: {lower_info['element'].capitalize()}\n"
        interpretation += f"- Quality: {lower_info['quality']}\n"
        interpretation += f"- Direction: {lower_info['direction'].capitalize()}\n\n"

        # Add elemental interaction
        upper_element = upper_info['element']
        lower_element = lower_info['element']

        interpretation += "Elemental Interaction:\n"
        if upper_element == lower_element:
            interpretation += f"Both trigrams share the {upper_element} element, suggesting harmony and reinforcement.\n"
        elif upper_element == self.xuan_dao_system.five_phases[lower_element]["generates"]:
            interpretation += f"The upper {upper_element} element is generated by the lower {lower_element} element, suggesting growth and development.\n"
        elif lower_element == self.xuan_dao_system.five_phases[upper_element]["generates"]:
            interpretation += f"The lower {lower_element} element generates the upper {upper_element} element, suggesting foundation and support.\n"
        elif upper_element == self.xuan_dao_system.five_phases[lower_element]["controlled_by"]:
            interpretation += f"The upper {upper_element} element is controlled by the lower {lower_element} element, suggesting restraint and guidance.\n"
        elif lower_element == self.xuan_dao_system.five_phases[upper_element]["controlled_by"]:
            interpretation += f"The lower {lower_element} element is controlled by the upper {upper_element} element, suggesting discipline and direction.\n"

        # Add general interpretation
        interpretation += "\nGeneral Interpretation:\n"
        interpretation += f"The combination of {upper_trigram} over {lower_trigram} suggests a situation where "

        # Add some randomized interpretation (simplified for demonstration)
        qualities = []
        if "天" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("cosmic forces or higher principles are at work")
        if "地" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("material foundations need attention")
        if "水" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("flexibility and adaptability are important")
        if "火" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("illumination and clarity are emerging")
        if "山" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("stillness and contemplation are beneficial")
        if "澤" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("joy and openness bring opportunity")
        if "風" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("gentle persistence will yield results")
        if "雷" in [upper_info['quality'], lower_info['quality']]:
            qualities.append("decisive action may be necessary")

        # Add random qualities to interpretation
        if qualities:
            interpretation += ", ".join(qualities) + ".\n"
        else:
            interpretation += "balance between different forces is needed.\n"

        # Add guidance
        interpretation += "\nGuidance:\n"
        # Randomly select guidance based on hexagram components
        guidances = [
            "Consider how the qualities of both trigrams can work together harmoniously.",
            "Be mindful of the interaction between the upper and lower energies in your situation.",
            "The transition from lower to upper suggests a path of development to follow.",
            "The balance of elements indicates potential challenges and opportunities.",
            "Pay attention to the directional energies and how they influence your question."
        ]
        interpretation += random.choice(guidances) + "\n"

        # Add a reminder
        interpretation += "\nRemember, this is a simplified interpretation for demonstration purposes. "
        interpretation += "A full I Ching reading would include more detailed analysis of the specific hexagram, "
        interpretation += "its changing lines, and the wisdom contained in the traditional texts."

        self.interpretation_text.insert(tk.END, interpretation)
        self.interpretation_text.config(state=tk.DISABLED)

    def create_calendar_tab(self):
        """Create the celestial calendar tab."""
        calendar_frame = ttk.Frame(self.notebook)
        self.notebook.add(calendar_frame, text="天文曆法 (Calendar)")

        # Create title
        title_label = ttk.Label(calendar_frame, text="天文曆法體系 - Celestial Calendar System",
                                font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Create description
        desc_text = """
        The Chinese celestial calendar system integrates astronomical observations with cyclical time patterns.
        It combines the Ten Heavenly Stems (天干) and Twelve Earthly Branches (地支) to form the Sixty Jiazi 
        Cycle (六十甲子), along with the Twenty-Four Solar Terms (二十四節氣) that track seasonal changes.

        This system creates a harmonic relationship between cosmic cycles and human activities, allowing for 
        auspicious timing and alignment with natural rhythms.
        """

        desc_label = ttk.Label(calendar_frame, text=desc_text, wraplength=800, justify=tk.CENTER)
        desc_label.pack(pady=10)

        # Create main content frame
        content_frame = ttk.Frame(calendar_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left side - Calendar systems
        left_frame = ttk.Frame(content_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Heavenly Stems and Earthly Branches
        stems_branches_frame = ttk.LabelFrame(left_frame, text="天干地支 - Heavenly Stems & Earthly Branches")
        stems_branches_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create table for stems and branches
        table_frame = ttk.Frame(stems_branches_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Stems
        ttk.Label(table_frame, text="Heavenly Stems (天干):", font=("Arial", 10, "bold")).grid(row=0, column=0,
                                                                                               sticky=tk.W, pady=5)
        stems_text = " ".join(self.xuan_dao_system.heavenly_stems)
        ttk.Label(table_frame, text=stems_text).grid(row=0, column=1, sticky=tk.W, pady=5)

        # Branches
        ttk.Label(table_frame, text="Earthly Branches (地支):", font=("Arial", 10, "bold")).grid(row=1, column=0,
                                                                                                 sticky=tk.W, pady=5)
        branches_text = " ".join(self.xuan_dao_system.earthly_branches)
        ttk.Label(table_frame, text=branches_text).grid(row=1, column=1, sticky=tk.W, pady=5)

        # Elements
        ttk.Label(table_frame, text="Stem Elements:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W,
                                                                                       pady=5)
        stem_elements = ", ".join([f"{stem}: {self.xuan_dao_system.stem_phase_mapping[stem]}"
                                   for stem in self.xuan_dao_system.heavenly_stems[:5]])
        ttk.Label(table_frame, text=stem_elements + "...").grid(row=2, column=1, sticky=tk.W, pady=5)

        # Solar Terms
        terms_frame = ttk.LabelFrame(left_frame, text="二十四節氣 - Twenty-Four Solar Terms")
        terms_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create scrolled text for solar terms
        terms_text = scrolledtext.ScrolledText(terms_frame, wrap=tk.WORD, height=8)
        terms_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add solar terms
        terms_text.insert(tk.END, "Spring: ")
        terms_text.insert(tk.END, ", ".join(self.xuan_dao_system.seasonal_divisions[:6]) + "\n\n")

        terms_text.insert(tk.END, "Summer: ")
        terms_text.insert(tk.END, ", ".join(self.xuan_dao_system.seasonal_divisions[6:12]) + "\n\n")

        terms_text.insert(tk.END, "Autumn: ")
        terms_text.insert(tk.END, ", ".join(self.xuan_dao_system.seasonal_divisions[12:18]) + "\n\n")

        terms_text.insert(tk.END, "Winter: ")
        terms_text.insert(tk.END, ", ".join(self.xuan_dao_system.seasonal_divisions[18:24]))

        terms_text.config(state=tk.DISABLED)

        # Sixty Jiazi Cycle preview
        cycle_frame = ttk.LabelFrame(left_frame, text="六十甲子 - Sixty Jiazi Cycle")
        cycle_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        cycle_label = ttk.Label(cycle_frame,
                                text="The Sixty Jiazi Cycle combines the 10 Heavenly Stems with the 12 Earthly Branches\nto create a 60-year cycle used in traditional timekeeping and astrology.",
                                justify=tk.CENTER)
        cycle_label.pack(pady=5)

        # Preview of the cycle
        cycle = self.xuan_dao_system.get_sixty_jiazi_cycle()
        preview_text = " ".join(cycle[:10]) + "..."
        preview_label = ttk.Label(cycle_frame, text=preview_text)
        preview_label.pack(pady=5)

        # Right side - Daily Energy Calculator
        right_frame = ttk.LabelFrame(content_frame, text="日能量計算 - Daily Energy Calculator")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Form for date input
        form_frame = ttk.Frame(right_frame)
        form_frame.pack(padx=10, pady=10)

        # Date inputs
        ttk.Label(form_frame, text="Enter Date:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Year
        ttk.Label(form_frame, text="Year:").grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.cal_year_var = tk.IntVar(value=2024)
        cal_year_entry = ttk.Entry(form_frame, textvariable=self.cal_year_var, width=6)
        cal_year_entry.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        # Month
        ttk.Label(form_frame, text="Month:").grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
        self.cal_month_var = tk.IntVar(value=1)
        cal_month_combo = ttk.Combobox(form_frame, textvariable=self.cal_month_var, values=list(range(1, 13)), width=3)
        cal_month_combo.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)

        # Day
        ttk.Label(form_frame, text="Day:").grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)
        self.cal_day_var = tk.IntVar(value=1)
        cal_day_combo = ttk.Combobox(form_frame, textvariable=self.cal_day_var, values=list(range(1, 32)), width=3)
        cal_day_combo.grid(row=0, column=6, padx=5, pady=5, sticky=tk.W)

        # Calculate button
        calculate_button = ttk.Button(form_frame, text="Calculate Energy", command=self.calculate_daily_energy)
        calculate_button.grid(row=0, column=7, padx=20, pady=5)

        # Frame for energy display
        energy_display_frame = ttk.Frame(right_frame)
        energy_display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Day info display
        self.day_info_frame = ttk.LabelFrame(energy_display_frame, text="Day Information")
        self.day_info_frame.pack(fill=tk.X, padx=5, pady=5)

        # Initial empty label
        self.day_info_label = ttk.Label(self.day_info_frame, text="Day information will appear here")
        self.day_info_label.pack(padx=10, pady=10)

        # Energy quality display
        self.energy_frame = ttk.LabelFrame(energy_display_frame, text="Energy Quality")
        self.energy_frame.pack(fill=tk.X, padx=5, pady=5)

        # Initial empty label
        self.energy_label = ttk.Label(self.energy_frame, text="Energy quality will appear here")
        self.energy_label.pack(padx=10, pady=10)

        # Activities display
        self.activities_frame = ttk.LabelFrame(energy_display_frame, text="Auspicious Activities")
        self.activities_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Initial empty label
        self.activities_label = ttk.Label(self.activities_frame, text="Suggested activities will appear here")
        self.activities_label.pack(padx=10, pady=10)

    def calculate_daily_energy(self):
        """Calculate and display the energy quality of a specific day."""
        try:
            year = self.cal_year_var.get()
            month = self.cal_month_var.get()
            day = self.cal_day_var.get()

            # Calculate daily energy
            energy = self.xuan_dao_system.calculate_daily_energy(year, month, day)

            # Get auspicious activities
            activities = self.xuan_dao_system.suggest_auspicious_activities(energy)

            # Update day info display
            day_info_text = f"Date: {year}-{month}-{day}\n"
            day_info_text += f"Heavenly Stem: {energy['day_stem']} ({energy['stem_element'].capitalize()})\n"
            day_info_text += f"Earthly Branch: {energy['day_branch']} ({energy['branch_element'].capitalize()})"

            # Clear previous results
            for widget in self.day_info_frame.winfo_children():
                widget.destroy()

            day_info_label = ttk.Label(self.day_info_frame, text=day_info_text, justify=tk.LEFT)
            day_info_label.pack(padx=10, pady=10, anchor=tk.W)

            # Update energy quality display
            energy_text = "Energy Qualities:\n"
            for quality in energy['energy_quality']:
                energy_text += f"- {quality}\n"

            # Clear previous results
            for widget in self.energy_frame.winfo_children():
                widget.destroy()

            energy_label = ttk.Label(self.energy_frame, text=energy_text, justify=tk.LEFT, wraplength=400)
            energy_label.pack(padx=10, pady=10, anchor=tk.W)

            # Update activities display
            activities_text = "Auspicious Activities for This Day:\n"
            for activity in activities:
                activities_text += f"- {activity}\n"

            # Clear previous results
            for widget in self.activities_frame.winfo_children():
                widget.destroy()

            activities_label = ttk.Label(self.activities_frame, text=activities_text,
                                         justify=tk.LEFT, wraplength=400)
            activities_label.pack(padx=10, pady=10, anchor=tk.W)

        except Exception as e:
            # Show error message
            for widget in self.day_info_frame.winfo_children():
                widget.destroy()

            error_label = ttk.Label(self.day_info_frame,
                                    text=f"Error: {str(e)}\nPlease enter valid date values.",
                                    foreground="red")
            error_label.pack(padx=10, pady=10)


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = XuanDaoApp(root)
    root.mainloop()