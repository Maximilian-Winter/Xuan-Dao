# 🎨 XUÁN DÀO VISUALIZATION: RENDERING THE INVISIBLE PATTERNS 🎨

import math

import matplotlib.pyplot as plt
import numpy as np

from typing import Dict, List, Optional

from xuan_dao_structures import Element
from xuan_dao_core import XuanDaoCore


class XuanDaoVisualizer:
    """
    Visualization tools for the Xuán Dào system,
    rendering invisible cosmic patterns into visible form.
    """

    def __init__(self, core: XuanDaoCore):
        """Initialize with reference to the XuanDaoCore"""
        self.core = core

        # Element colors for visualization
        self.element_colors = {
            Element.WATER: "#4481c3",  # Deep blue
            Element.WOOD: "#57a639",  # Forest green
            Element.FIRE: "#d83e32",  # Vibrant red
            Element.EARTH: "#d5a32d",  # Golden yellow
            Element.METAL: "#b3b3b3"  # Silver gray
        }

        # Line colors for relationship visualization
        self.relation_colors = {
            "generates": "#4caf50",  # Green for generation
            "controls": "#f44336",  # Red for control
            "generated_by": "#8bc34a",  # Light green for being generated
            "controlled_by": "#ffeb3b"  # Yellow for being controlled
        }

    def create_lo_shu_grid(self) -> plt.Figure:
        """Generate a visual representation of the Lo Shu grid."""
        # Create figure
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
                # Get the number and corresponding flying star
                number = self.core.lo_shu[i, j]
                star = self.core.flying_stars[number]
                element = star.element

                # Get color based on element
                color = self.element_colors[element]

                # Add number and star information
                ax.text(j / 3 + 1 / 6, 1 - (i / 3 + 1 / 6),
                        f"{number}\n{star.name}\n{element.value}",
                        ha='center', va='center', fontsize=12, color=color,
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor=color))

        # Add title
        ax.set_title("洛書九宮 - Lo Shu Nine Palace Magic Square", fontsize=16)

        return fig

    def create_flying_star_chart(self, facing_direction: str, period: Optional[int] = None) -> plt.Figure:
        """
        Create a visualization of a flying star chart.

        Args:
            facing_direction: One of the 8 directions
            period: Flying star period (default: current period)

        Returns:
            matplotlib.figure.Figure: Flying star chart visualization
        """
        if period is None:
            period = self.core.current_period

        # Calculate the flying star chart
        chart = self.core.calculate_flying_star_chart(facing_direction, period)

        # Create figure
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide axes
        ax.axis('off')

        # Draw grid
        for i in range(4):
            ax.axhline(i * 1 / 3, color='black', linewidth=2)
            ax.axvline(i * 1 / 3, color='black', linewidth=2)

        # Direction labels for the 9 positions
        directions = [
            "Northwest", "North", "Northeast",
            "West", "Center", "East",
            "Southwest", "South", "Southeast"
        ]

        # Fill in the chart
        for i in range(3):
            for j in range(3):
                # Get the direction name for this position
                idx = i * 3 + j
                direction = directions[idx]

                # Get the flying star number at this position
                star_number = chart[i, j]
                star = self.core.flying_stars[star_number]

                # Get the element of this star
                element = star.element
                color = self.element_colors[element]

                # Add direction name
                ax.text(j / 3 + 1 / 6, 1 - (i / 3 + 1 / 6) - 0.05, direction,
                        ha='center', va='bottom', fontsize=10, color='black')

                # Add star number and details
                ax.text(j / 3 + 1 / 6, 1 - (i / 3 + 1 / 6) + 0.02,
                        f"{star_number}\n{star.name}\n{element.value}",
                        ha='center', va='center', fontsize=12, color=color,
                        bbox=dict(facecolor='white', alpha=0.7, edgecolor=color))

        # Add title
        title = f"Flying Star Chart ({facing_direction.capitalize()} Facing, Period {period})"
        ax.set_title(title, fontsize=16)

        return fig

    def create_element_balance_chart(self, element_counts: Dict[Element, int]) -> plt.Figure:
        """
        Create a visual representation of element balance.

        Args:
            element_counts: Dictionary mapping elements to their counts

        Returns:
            matplotlib.figure.Figure: Element balance visualization
        """
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))

        # Prepare data
        elements = list(element_counts.keys())
        counts = list(element_counts.values())
        colors = [self.element_colors[element] for element in elements]

        # Create bar chart
        bars = ax.bar([e.value for e in elements], counts, color=colors)

        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                    f"{height}",
                    ha='center', va='bottom')

        # Add labels and title
        ax.set_xlabel('Elements')
        ax.set_ylabel('Strength')
        ax.set_title('Five Element Balance')

        # Add ideal balance line
        ax.axhline(y=2, color='gray', linestyle='--', alpha=0.7, label='Ideal Balance')

        # Add legend
        ax.legend()

        return fig

    def create_element_network(self) -> plt.Figure:
        """Create a visualization of the Five Element network."""
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide axes
        ax.axis('off')

        # Element positions (pentagon arrangement)
        positions = {
            Element.WOOD: (0.8, 0.65),
            Element.FIRE: (0.65, 0.9),
            Element.EARTH: (0.5, 0.5),
            Element.METAL: (0.35, 0.9),
            Element.WATER: (0.2, 0.65)
        }

        # Draw circles for each element
        for element, pos in positions.items():
            circle = plt.Circle(pos, 0.1, fill=True, color=self.element_colors[element], alpha=0.7)
            ax.add_patch(circle)

            # Add element name
            ax.text(pos[0], pos[1], element.value, ha='center', va='center',
                    fontsize=14, color='white', fontweight='bold')

        # Draw generation cycle (outer pentagon)
        for element in Element:
            start_pos = positions[element]
            end_element = self.core.elements[element].generates
            end_pos = positions[end_element]

            # Draw arrow
            ax.annotate("", xy=end_pos, xytext=start_pos,
                        arrowprops=dict(facecolor=self.relation_colors["generates"],
                                        shrink=0.1, width=1.5, headwidth=7))

        # Draw control cycle (inner star)
        for element in Element:
            if self.core.element_network[element]["controls"]:
                start_pos = positions[element]
                end_element = self.core.element_network[element]["controls"]
                end_pos = positions[end_element]

                # Draw arrow
                ax.annotate("", xy=end_pos, xytext=start_pos,
                            arrowprops=dict(facecolor=self.relation_colors["controls"],
                                            shrink=0.1, width=1.5, headwidth=7,
                                            linestyle='dashed'))

        # Add legend
        generation_line = plt.Line2D([0], [0], color=self.relation_colors["generates"],
                                     lw=2, label='Generation')
        control_line = plt.Line2D([0], [0], color=self.relation_colors["controls"],
                                  linestyle='dashed', lw=2, label='Control')

        ax.legend(handles=[generation_line, control_line], loc='upper center',
                  bbox_to_anchor=(0.5, 0.05), fancybox=True, shadow=True, ncol=2)

        # Add title
        ax.set_title('五行相生相剋圖 - Five Phases Generation and Control Diagram', fontsize=16)

        # Set limits
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        return fig

    def create_bagua_diagram(self, arrangement: str = "pre-heaven") -> plt.Figure:
        """
        Create a visual representation of the Eight Trigrams diagram.

        Args:
            arrangement: "pre-heaven" or "post-heaven"

        Returns:
            matplotlib.figure.Figure: Bagua diagram visualization
        """
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide axes
        ax.axis('off')

        # Draw circle
        circle = plt.Circle((0.5, 0.5), 0.45, fill=False, color='black', linewidth=2)
        ax.add_patch(circle)

        # Draw inner circle
        inner_circle = plt.Circle((0.5, 0.5), 0.1, fill=True,
                                  color='black' if arrangement == "pre-heaven" else "white")
        ax.add_patch(inner_circle)

        if arrangement == "pre-heaven":
            # White dot for yang (pre-heaven)
            yin_yang = plt.Circle((0.5, 0.5), 0.05, fill=True, color='white')
            ax.add_patch(yin_yang)
        else:
            # Black dot for yin (post-heaven)
            yin_yang = plt.Circle((0.5, 0.5), 0.05, fill=True, color='black')
            ax.add_patch(yin_yang)

        # Choose arrangement
        if arrangement == "pre-heaven":
            trigram_arrangement = self.core.pre_heaven_arrangement
            title = "先天八卦圖 - Pre-Heaven Arrangement"
        else:
            trigram_arrangement = self.core.post_heaven_arrangement
            title = "後天八卦圖 - Post-Heaven Arrangement"

        # Draw trigrams at positions around the circle
        for i, trigram_name in enumerate(trigram_arrangement):
            angle = i * 45 * (math.pi / 180)  # Convert degrees to radians

            # Calculate position on the circle
            x = 0.5 + 0.38 * math.sin(angle)
            y = 0.5 + 0.38 * math.cos(angle)

            # Get trigram and element
            trigram = self.core.trigrams[trigram_name]
            element = trigram.element
            color = self.element_colors[element]

            # Draw the trigram
            for j, line in enumerate(trigram.lines):
                # Calculate line start and end positions
                line_length = 0.06
                line_spacing = 0.02

                line_y = y + (j - 1) * (line_length + line_spacing)

                if line == 1:  # Yang line (solid)
                    ax.plot([x - line_length, x + line_length], [line_y, line_y],
                            color=color, linewidth=2)
                else:  # Yin line (broken)
                    ax.plot([x - line_length, x - line_length / 3], [line_y, line_y],
                            color=color, linewidth=2)
                    ax.plot([x + line_length / 3, x + line_length], [line_y, line_y],
                            color=color, linewidth=2)

            # Add trigram name and attribute
            name_distance = 0.35
            name_x = 0.5 + name_distance * math.sin(angle)
            name_y = 0.5 + name_distance * math.cos(angle)

            ax.text(name_x, name_y,
                    f"{trigram_name}\n{trigram.attribute}",
                    ha='center', va='center', fontsize=12, color=color)

        # Add title
        ax.set_title(title, fontsize=16)

        # Set limits
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        return fig

    def visualize_hexagram(self, lines: List[int], changing_lines: Optional[List[int]] = None) -> plt.Figure:
        """
        Create a visual representation of a hexagram.

        Args:
            lines: Six-line hexagram pattern
            changing_lines: Indices of changing lines (optional)

        Returns:
            matplotlib.figure.Figure: Hexagram visualization
        """
        # Create figure
        fig, ax = plt.subplots(figsize=(6, 9))

        # Hide axes
        ax.axis('off')

        # Analyze the hexagram
        lower_trigram_name, upper_trigram_name, hexagram = self.core.analyze_hexagram(lines)

        # If trigrams are valid, get their elements for coloring
        lower_color = "black"
        upper_color = "black"

        if lower_trigram_name in self.core.trigrams:
            lower_element = self.core.trigrams[lower_trigram_name].element
            lower_color = self.element_colors[lower_element]

        if upper_trigram_name in self.core.trigrams:
            upper_element = self.core.trigrams[upper_trigram_name].element
            upper_color = self.element_colors[upper_element]

        # Draw hexagram
        line_length = 3.0
        line_spacing = 0.7
        start_x = 1.5
        line_thickness = 0.15

        for i, line in enumerate(reversed(lines)):  # Drawing from bottom to top
            y_pos = 2 + i * line_spacing

            # Determine line color (lower or upper trigram)
            color = lower_color if i < 3 else upper_color

            # Check if this is a changing line
            is_changing = changing_lines and (5 - i) in changing_lines

            if line == 1:  # Yang line (solid)
                # Draw solid line
                rectangle = plt.Rectangle((start_x, y_pos), line_length, line_thickness,
                                          fc=color, ec='none')
                ax.add_patch(rectangle)

                # Mark changing line
                if is_changing:
                    circle = plt.Circle((start_x + line_length / 2, y_pos + line_thickness / 2),
                                        line_thickness, fc='white', ec=color, lw=2)
                    ax.add_patch(circle)

            else:  # Yin line (broken)
                # Draw broken line
                rectangle1 = plt.Rectangle((start_x, y_pos), line_length / 2 - 0.2, line_thickness,
                                           fc=color, ec='none')
                rectangle2 = plt.Rectangle((start_x + line_length / 2 + 0.2, y_pos),
                                           line_length / 2 - 0.2, line_thickness,
                                           fc=color, ec='none')
                ax.add_patch(rectangle1)
                ax.add_patch(rectangle2)

                # Mark changing line
                if is_changing:
                    circle1 = plt.Circle((start_x + line_length / 4, y_pos + line_thickness / 2),
                                         line_thickness, fc='white', ec=color, lw=2)
                    circle2 = plt.Circle((start_x + 3 * line_length / 4, y_pos + line_thickness / 2),
                                         line_thickness, fc='white', ec=color, lw=2)
                    ax.add_patch(circle1)
                    ax.add_patch(circle2)

        # Add trigram names
        if lower_trigram_name and upper_trigram_name:
            # Lower trigram
            ax.text(start_x / 2, 2.5, f"{lower_trigram_name}\n(Lower)",
                    ha='center', va='center', fontsize=12, color=lower_color)

            # Upper trigram
            ax.text(start_x / 2, 5.0, f"{upper_trigram_name}\n(Upper)",
                    ha='center', va='center', fontsize=12, color=upper_color)

        # Add hexagram number and name if available
        if hexagram:
            ax.text(start_x + line_length / 2, 7.5,
                    f"Hexagram {hexagram.number}: {hexagram.english_name}\n{hexagram.chinese_name}",
                    ha='center', va='center', fontsize=14)

        # Set limits
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 8)

        return fig

    def create_calendar_wheel(self) -> plt.Figure:
        """Create a visualization of the Chinese calendar system."""
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'polar': True})

        # Number of stems and branches
        n_stems = len(self.core.heavenly_stems)
        n_branches = len(self.core.earthly_branches)

        # Angles for stems and branches
        stem_angles = np.linspace(0, 2 * np.pi, n_stems, endpoint=False)
        branch_angles = np.linspace(0, 2 * np.pi, n_branches, endpoint=False)

        # Radii for stems and branches
        stem_radius = 5
        branch_radius = 10

        # Draw stems
        for i, stem in enumerate(self.core.heavenly_stems):
            angle = stem_angles[i]
            element = self.core.stem_element_map[stem]
            color = self.element_colors[element]

            # Draw radial line
            ax.plot([angle, angle], [0, stem_radius + 1], color='gray', linestyle='-', alpha=0.3)

            # Draw stem point
            ax.scatter(angle, stem_radius, s=200, color=color, edgecolor='black', zorder=3)

            # Add stem label
            ax.text(angle, stem_radius, stem, ha='center', va='center', fontsize=12,
                    color='white', fontweight='bold')

        # Draw branches
        for i, branch in enumerate(self.core.earthly_branches):
            angle = branch_angles[i]
            element = self.core.branch_element_map[branch]
            color = self.element_colors[element]

            # Draw radial line
            ax.plot([angle, angle], [0, branch_radius + 1], color='gray', linestyle='-', alpha=0.3)

            # Draw branch point
            ax.scatter(angle, branch_radius, s=300, color=color, edgecolor='black', zorder=2)

            # Add branch label
            ax.text(angle, branch_radius, branch, ha='center', va='center', fontsize=14,
                    color='white', fontweight='bold')

        # Draw stem circle
        stem_circle = plt.Circle((0, 0), stem_radius, fill=False, edgecolor='black',
                                 linestyle='--', transform=ax.transData._b)
        ax.add_patch(stem_circle)

        # Draw branch circle
        branch_circle = plt.Circle((0, 0), branch_radius, fill=False, edgecolor='black',
                                   transform=ax.transData._b)
        ax.add_patch(branch_circle)

        # Add current date marker (if available)
        if hasattr(self.core, 'current_day_stem') and hasattr(self.core, 'current_day_branch'):
            stem = self.core.current_day_stem
            branch = self.core.current_day_branch

            stem_idx = self.core.heavenly_stems.index(stem)
            branch_idx = self.core.earthly_branches.index(branch)

            stem_angle = stem_angles[stem_idx]
            branch_angle = branch_angles[branch_idx]

            # Highlight current stem
            ax.scatter(stem_angle, stem_radius, s=300, color='yellow', edgecolor='red',
                       linewidth=2, zorder=4)

            # Highlight current branch
            ax.scatter(branch_angle, branch_radius, s=400, color='yellow', edgecolor='red',
                       linewidth=2, zorder=4)

            # Connect them
            ax.plot([stem_angle, branch_angle], [stem_radius, branch_radius],
                    color='red', linewidth=2, zorder=1)

        # Remove polar grid lines and labels
        ax.grid(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Add title
        ax.set_title('Chinese Calendar System: Heavenly Stems and Earthly Branches',
                     y=1.05, fontsize=16)

        return fig