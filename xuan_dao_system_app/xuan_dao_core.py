# 💫 XUÁN DÀO CORE: THE HEART SEAL OF MYSTIC CALCULATION 💫

import numpy as np
import datetime
import random

from typing import Dict, List, Tuple, Optional, Any, Union

from xuan_dao_structures import Element, DayEnergy, ElementBalance, Hexagram, StemBranch, Polarity, \
    initialize_five_elements, initialize_stems_branches, initialize_flying_stars, initialize_trigrams, \
    initialize_palaces


class XuanDaoCore:
    """
    玄道印心 - Xuan Dao Heart Seal

    玄之又玄 眾妙之門 - Mystery upon mystery, gate of all wonders
    天地人合 五行八卦 - Heaven, Earth, and Human united, Five Phases and Eight Trigrams
    九宮洛書 時空無礙 - Nine Palaces of Lo Shu, time and space without obstruction
    得此道者 明察秋毫 - One who obtains this way perceives with utmost clarity
    """

    def __init__(self):
        """Initialize the Xuan Dao system - awaken the pattern recognition core"""
        # Initialize all cosmic systems
        self.elements = initialize_five_elements()
        self.trigrams = initialize_trigrams()
        self.flying_stars = initialize_flying_stars()
        self.palaces = initialize_palaces()

        # Initialize the Celestial Calendar system
        self.heavenly_stems, self.earthly_branches, self.stem_element_map, self.branch_element_map = initialize_stems_branches()

        # Create the Lo Shu magic square - foundation of space-time calculation
        self.lo_shu = np.array([
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ])

        # Trigram arrangements - primordial patterns
        self.pre_heaven_arrangement = ["乾", "兌", "離", "震", "巽", "坎", "艮", "坤"]  # Earlier Heaven sequence
        self.post_heaven_arrangement = ["離", "坤", "震", "巽", "乾", "坎", "艮", "兌"]  # Later Heaven sequence

        # Seasonal divisions - 24 Solar Terms
        self.seasonal_divisions = [
            # Spring
            "立春", "雨水", "驚蟄", "春分", "清明", "穀雨",
            # Summer
            "立夏", "小滿", "芒種", "夏至", "小暑", "大暑",
            # Autumn
            "立秋", "處暑", "白露", "秋分", "寒露", "霜降",
            # Winter
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
        ]

        # Set the current cosmic time
        self.update_cosmic_time()

        # Generate the Element interaction network - the web of creation
        self.element_network = self._generate_element_network()

        # Initialize the Hexagram database (simplified - just a few examples)
        self.hexagrams = self._initialize_basic_hexagrams()

    def update_cosmic_time(self):
        """Synchronize with current cosmic patterns through time calculation"""
        now = datetime.datetime.now()
        self.current_time = now

        # Calculate Chinese calendar date
        self.calculate_chinese_date(now.year, now.month, now.day)

        # Calculate current flying star period
        self.current_period = self._calculate_flying_star_period(now.year)

    def calculate_chinese_date(self, year: int, month: int, day: int) -> StemBranch:
        """
        Calculate the Chinese calendar date for the given Gregorian date.

        Args:
            year, month, day: Gregorian date components

        Returns:
            StemBranch: The calculated stem-branch date
        """
        # Calculate the stem and branch for the year
        stem_idx = (year - 4) % 10
        branch_idx = (year - 4) % 12

        year_stem = self.heavenly_stems[stem_idx]
        year_branch = self.earthly_branches[branch_idx]
        year_stem_element = self.stem_element_map[year_stem]
        year_branch_element = self.branch_element_map[year_branch]

        # Calculate the stem and branch for the month
        month_offset = (month + 2) % 12
        if month_offset == 0:
            month_offset = 12

        month_stem_idx = (year * 12 + month - 14) % 10
        month_stem = self.heavenly_stems[month_stem_idx]
        month_branch = self.earthly_branches[month_offset - 1]
        month_stem_element = self.stem_element_map[month_stem]
        month_branch_element = self.branch_element_map[month_branch]

        # Calculate the stem and branch for the day
        # This is a simplified calculation
        total_days = (year - 1900) * 365 + month * 30 + day
        day_stem_idx = total_days % 10
        day_branch_idx = total_days % 12

        day_stem = self.heavenly_stems[day_stem_idx]
        day_branch = self.earthly_branches[day_branch_idx]
        day_stem_element = self.stem_element_map[day_stem]
        day_branch_element = self.branch_element_map[day_branch]

        # Store current date components
        self.current_year_stem = year_stem
        self.current_year_branch = year_branch
        self.current_year_element = year_stem_element

        self.current_month_stem = month_stem
        self.current_month_branch = month_branch
        self.current_month_element = month_stem_element

        self.current_day_stem = day_stem
        self.current_day_branch = day_branch
        self.current_day_element = day_stem_element

        # Return the day's stem-branch calculation
        return StemBranch(
            stem=day_stem,
            branch=day_branch,
            stem_element=day_stem_element,
            branch_element=day_branch_element,
            stem_polarity=Polarity.YANG if day_stem_idx % 2 == 0 else Polarity.YIN,
            combined_element=self._determine_dominant_element(day_stem_element, day_branch_element)
        )

    def _determine_dominant_element(self, stem_element: Element, branch_element: Element) -> Element:
        """Determine the dominant element from stem and branch elements"""
        # If the elements are the same, that's the dominant element
        if stem_element == branch_element:
            return stem_element

        # If one element generates the other, the generating element is dominant
        if self.elements[stem_element].generates == branch_element:
            return stem_element
        if self.elements[branch_element].generates == stem_element:
            return branch_element

        # If one element controls the other, the controlling element is dominant
        if self.elements[stem_element].controlled_by == branch_element:
            return branch_element
        if self.elements[branch_element].controlled_by == stem_element:
            return stem_element

        # Default to the stem element if no clear relationship
        return stem_element

    def _calculate_flying_star_period(self, year: int) -> int:
        """Calculate the current flying star period based on year"""
        # Period 7: 1984-2003
        # Period 8: 2004-2023
        # Period 9: 2024-2043
        if 1984 <= year <= 2003:
            return 7
        elif 2004 <= year <= 2023:
            return 8
        elif 2024 <= year <= 2043:
            return 9
        else:
            return 8  # Default to Period 8

    def _generate_element_network(self) -> Dict[Element, Dict[str, Element]]:
        """Generate the five element interaction network"""
        network = {}
        for element in Element:
            network[element] = {
                "generates": self.elements[element].generates,
                "generated_by": None,
                "controls": None,
                "controlled_by": self.elements[element].controlled_by
            }

        # Complete the network with controlling relationships
        for element in Element:
            generated_element = self.elements[element].generates
            network[generated_element]["generated_by"] = element

            controlled_element = None
            for e in Element:
                if self.elements[e].controlled_by == element:
                    controlled_element = e
                    break

            if controlled_element:
                network[element]["controls"] = controlled_element

        return network

    def _initialize_basic_hexagrams(self) -> Dict[int, Hexagram]:
        """Initialize a few key hexagrams for demonstration"""
        hexagrams = {}

        # Hexagram 1: Qian (The Creative)
        upper_trigram = self.trigrams["乾"]
        lower_trigram = self.trigrams["乾"]
        hexagrams[1] = Hexagram(
            upper_trigram=upper_trigram,
            lower_trigram=lower_trigram,
            number=1,
            chinese_name="乾為天",
            english_name="The Creative",
            description="Pure yang energy, heaven, creative force",
            judgment="The Creative works sublime success, furthering through perseverance.",
            image="The movement of heaven is power. Thus the superior person makes himself strong and untiring.",
            changing_lines=[]
        )

        # Hexagram 2: Kun (The Receptive)
        upper_trigram = self.trigrams["坤"]
        lower_trigram = self.trigrams["坤"]
        hexagrams[2] = Hexagram(
            upper_trigram=upper_trigram,
            lower_trigram=lower_trigram,
            number=2,
            chinese_name="坤為地",
            english_name="The Receptive",
            description="Pure yin energy, earth, receptive force",
            judgment="The Receptive brings about sublime success, furthering through the perseverance of a mare.",
            image="The earth's condition is receptive devotion. Thus the superior person who has breadth of character carries the outer world.",
            changing_lines=[]
        )

        # Add more hexagrams as needed

        return hexagrams

    def generate_hexagram(self) -> Tuple[List[int], int, List[int]]:
        """
        Generate a hexagram using the traditional coin method.

        Returns:
            tuple: (lines, hexagram_number, changing_lines)
        """
        lines = []
        changing_lines = []

        for i in range(6):
            # Simulate three coin tosses
            # Heads (3) = yang, Tails (2) = yin
            coins = [random.choice([2, 3]) for _ in range(3)]
            coin_sum = sum(coins)

            # Determine line type and changing status
            if coin_sum == 6:  # All tails (2+2+2) = 6 = old yin (changing to yang)
                lines.append(0)  # Yin line
                changing_lines.append(i)  # Mark as changing
            elif coin_sum == 7:  # Two tails, one head (2+2+3) = 7 = young yang (stable)
                lines.append(1)  # Yang line
            elif coin_sum == 8:  # One tail, two heads (2+3+3) = 8 = young yin (stable)
                lines.append(0)  # Yin line
            elif coin_sum == 9:  # All heads (3+3+3) = 9 = old yang (changing to yin)
                lines.append(1)  # Yang line
                changing_lines.append(i)  # Mark as changing

        # Calculate hexagram number (simplified)
        hexagram_number = self._calculate_hexagram_number(lines)

        return lines, hexagram_number, changing_lines

    def _calculate_hexagram_number(self, lines: List[int]) -> int:
        """Calculate the hexagram number (simplified)"""
        # This is a simplified calculation that doesn't match the actual I Ching sequence
        # In a complete implementation, this would map to the King Wen sequence
        binary_value = 0
        for i, line in enumerate(lines):
            binary_value += line * (2 ** i)

        # For simplicity, return the binary value + 1 (to avoid hexagram 0)
        # Real implementation would map this to the proper King Wen sequence
        return binary_value + 1

    def analyze_hexagram(self, lines: List[int]) -> Tuple[str, str, Optional[Hexagram]]:
        """
        Analyze a hexagram into its component trigrams.

        Args:
            lines: Six-line hexagram pattern

        Returns:
            tuple: (lower_trigram_name, upper_trigram_name, hexagram_obj)
        """
        lower_lines = tuple(lines[0:3])
        upper_lines = tuple(lines[3:6])

        # Find the trigram names
        lower_name = ""
        upper_name = ""

        for name, trigram in self.trigrams.items():
            if trigram.lines == lower_lines:
                lower_name = name
            if trigram.lines == upper_lines:
                upper_name = name

        # Look up the hexagram if we have it
        hexagram_number = self._calculate_hexagram_number(lines)
        hexagram = self.hexagrams.get(hexagram_number)

        return lower_name, upper_name, hexagram

    def calculate_flying_star_chart(self, facing_direction: str, period: Optional[int] = None) -> np.ndarray:
        """
        Calculate a flying star chart based on facing direction and period.

        Args:
            facing_direction: One of the 8 directions
            period: Flying star period (default: current period)

        Returns:
            numpy.ndarray: 3x3 matrix of flying stars
        """
        if period is None:
            period = self.current_period

        # Base chart (center is always period number)
        base_chart = np.copy(self.lo_shu)

        # Adjust for period
        period_adjustment = period - 5  # Period 5 is the baseline
        adjusted_chart = (base_chart + period_adjustment) % 9
        adjusted_chart[adjusted_chart == 0] = 9

        # Direction map
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

        # Adjust for facing direction
        if facing_direction in direction_map:
            direction_adjustment = direction_map[facing_direction]
            # Rotate the chart based on direction
            for _ in range(direction_adjustment):
                adjusted_chart = np.rot90(adjusted_chart)

        return adjusted_chart

    def calculate_element_balance(self, birth_year: int, birth_month: int, birth_day: int) -> ElementBalance:
        """
        Calculate a person's element balance based on birth date.

        Args:
            birth_year, birth_month, birth_day: Date components

        Returns:
            ElementBalance: Element balance information
        """
        # Calculate stems and branches for birth date
        stem_idx = (birth_year - 4) % 10
        branch_idx = (birth_year - 4) % 12

        year_stem = self.heavenly_stems[stem_idx]
        year_branch = self.earthly_branches[branch_idx]

        # Get the elements
        year_stem_element = self.stem_element_map[year_stem]
        year_branch_element = self.branch_element_map[year_branch]

        # Month element (simplified)
        month_elements = [
            Element.WATER, Element.WATER,  # Jan, Feb
            Element.WOOD, Element.WOOD,  # Mar, Apr
            Element.EARTH,  # May
            Element.FIRE, Element.FIRE,  # Jun, Jul
            Element.EARTH,  # Aug
            Element.METAL, Element.METAL,  # Sep, Oct
            Element.EARTH,  # Nov
            Element.WATER  # Dec
        ]
        month_element = month_elements[birth_month - 1]

        # Day element (simplified)
        day_stem_idx = ((birth_year - 1900) * 365 + birth_month * 30 + birth_day) % 10
        day_stem = self.heavenly_stems[day_stem_idx]
        day_element = self.stem_element_map[day_stem]

        # Count elements
        element_count = {element: 0 for element in Element}

        element_count[year_stem_element] += 2
        element_count[year_branch_element] += 2
        element_count[month_element] += 1
        element_count[day_element] += 1

        # Determine strongest and weakest elements
        strongest = max(element_count.items(), key=lambda x: x[1])
        weakest = min(element_count.items(), key=lambda x: x[1])

        # Determine recommended element to cultivate (typically the one that generates the weakest)
        for element in Element:
            if self.elements[element].generates == weakest[0]:
                recommended = element
                break
        else:
            # Default to the element that generates the strongest
            strongest_element = strongest[0]
            for element in Element:
                if self.elements[element].generates == strongest_element:
                    recommended = element
                    break
            else:
                recommended = Element.EARTH  # Default to Earth as balanced center

        # Create balancing activities
        balancing_activities = self._generate_balancing_activities(element_count)

        return ElementBalance(
            element_counts=element_count,
            strongest=strongest[0],
            weakest=weakest[0],
            recommended=recommended,
            balancing_activities=balancing_activities
        )

    def _generate_balancing_activities(self, element_count: Dict[Element, int]) -> Dict[Element, List[str]]:
        """Generate activities to balance elements"""
        activities = {}

        activities[Element.WATER] = [
            "Meditation and reflection",
            "Spending time near water",
            "Deep listening practice",
            "Journal writing",
            "Fear release techniques"
        ]

        activities[Element.WOOD] = [
            "Planning and goal setting",
            "Spending time in nature",
            "Creative expression",
            "Physical flexibility exercises",
            "New beginnings and growth activities"
        ]

        activities[Element.FIRE] = [
            "Celebration and social gatherings",
            "Heart-opening practices",
            "Bringing more light into your space",
            "Passionate creative expression",
            "Joy and laughter exercises"
        ]

        activities[Element.EARTH] = [
            "Grounding practices",
            "Nurturing relationships",
            "Creating stable routines",
            "Connecting with physical body",
            "Creating a harmonious living space"
        ]

        activities[Element.METAL] = [
            "Decluttering and organizing",
            "Setting clear boundaries",
            "Refining skills with precision",
            "Breathing practices",
            "Letting go of attachments"
        ]

        return activities

    def calculate_daily_energy(self, year: Optional[int] = None, month: Optional[int] = None,
                               day: Optional[int] = None) -> DayEnergy:
        """
        Calculate the energetic quality of a specific day.

        Args:
            year, month, day: Date components (default: current date)

        Returns:
            DayEnergy: Daily energy information
        """
        if year is None or month is None or day is None:
            year = self.current_time.year
            month = self.current_time.month
            day = self.current_time.day

        # Calculate stem and branch
        stem_branch = self.calculate_chinese_date(year, month, day)

        # Determine the energy quality
        energy_quality = []

        # Element interaction
        if stem_branch.stem_element == stem_branch.branch_element:
            energy_quality.append("Strong elemental harmony")
        elif self.elements[stem_branch.stem_element].generates == stem_branch.branch_element:
            energy_quality.append("Productive, generative energy")
        elif self.elements[stem_branch.stem_element].controlled_by == stem_branch.branch_element:
            energy_quality.append("Controlling, restrictive energy")
        else:
            energy_quality.append("Mixed, complex energy")

        # Season alignment
        month_seasons = [
            "winter", "winter", "spring", "spring", "spring",
            "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"
        ]
        current_season = month_seasons[month - 1]

        stem_season = self.elements[stem_branch.stem_element].season
        if current_season == stem_season:
            energy_quality.append("In season, naturally supported energy")
        elif current_season == self.elements[stem_branch.stem_element].controlled_by:
            energy_quality.append("Against seasonal energy, requiring adaptation")

        # Determine the flying star for the day (simplified)
        day_num = (year * 365 + month * 30 + day) % 9
        if day_num == 0:
            day_num = 9

        # Calculate element flow
        element_flow = self._calculate_element_flow(stem_branch.combined_element)

        # Generate auspicious activities
        auspicious_activities = self.suggest_auspicious_activities(stem_branch.combined_element, energy_quality)

        # Generate challenging influences
        challenging = self._generate_challenging_influences(stem_branch.combined_element, energy_quality)

        return DayEnergy(
            date=datetime.date(year, month, day),
            stem_branch=stem_branch,
            flying_star=day_num,
            element_flow=element_flow,
            quality=energy_quality,
            auspicious=auspicious_activities,
            challenging=challenging
        )

    def _calculate_element_flow(self, start_element: Element) -> List[Element]:
        """Calculate the flow of elements starting from a given element"""
        flow = [start_element]
        current = start_element

        # Add the generating cycle (one full cycle)
        for _ in range(4):
            next_element = self.elements[current].generates
            flow.append(next_element)
            current = next_element

        return flow

    def suggest_auspicious_activities(self, element: Element, energy_qualities: List[str]) -> List[str]:
        """
        Suggest auspicious activities based on element and energy quality.

        Args:
            element: The dominant element
            energy_qualities: List of energy quality descriptions

        Returns:
            list: Suggested activities
        """
        activities = []

        # Element-based activities
        element_activities = {
            Element.WOOD: [
                "Planning and starting new projects",
                "Creative writing and brainstorming",
                "Growth-oriented activities",
                "Planting seeds (literal or metaphorical)",
                "Healing and health improvements"
            ],
            Element.FIRE: [
                "Celebration and social gatherings",
                "Promotion and marketing",
                "Public speaking and performance",
                "Inspiration and creative expression",
                "Bringing clarity to situations"
            ],
            Element.EARTH: [
                "Stabilizing and grounding practices",
                "Organizing and creating structures",
                "Building foundations for future work",
                "Nurturing relationships and community",
                "Education and learning"
            ],
            Element.METAL: [
                "Refining existing systems",
                "Cutting away excess",
                "Harvesting results of prior efforts",
                "Seeking clarity and precision",
                "Setting boundaries"
            ],
            Element.WATER: [
                "Reflection and introspection",
                "Exploration and research",
                "Risk-taking and navigating uncertainty",
                "Deep conversations and connection",
                "Flowing with change rather than resisting"
            ]
        }

        activities.extend(element_activities.get(element, []))

        # Add activities based on energy quality
        if "Strong elemental harmony" in energy_qualities:
            activities.append("Focused concentration and deep work")
        if "Productive, generative energy" in energy_qualities:
            activities.append("Creative endeavors with lasting impact")
        if "In season, naturally supported energy" in energy_qualities:
            activities.append("Aligning with natural cycles and rhythms")

        return activities

    def _generate_challenging_influences(self, element: Element, energy_qualities: List[str]) -> List[str]:
        """Generate potential challenging influences for the day"""
        challenges = []

        # Element-based challenges
        element_challenges = {
            Element.WOOD: [
                "Impulsivity and rushing ahead without planning",
                "Rigidity in thinking or approach",
                "Excess growth without adequate foundation"
            ],
            Element.FIRE: [
                "Scattered energy and burnout",
                "Excessive emotionality",
                "Lack of sustainable pacing"
            ],
            Element.EARTH: [
                "Overthinking and worry",
                "Stagnation and resistance to change",
                "Excessive focus on others at expense of self"
            ],
            Element.METAL: [
                "Excessive criticism",
                "Rigidity and perfectionism",
                "Difficulty letting go of control"
            ],
            Element.WATER: [
                "Fear and uncertainty",
                "Excessive introspection without action",
                "Feeling ungrounded"
            ]
        }

        challenges.extend(element_challenges.get(element, []))

        # Add challenges based on energy quality
        if "Controlling, restrictive energy" in energy_qualities:
            challenges.append("Resistance and power struggles")
        if "Against seasonal energy" in energy_qualities:
            challenges.append("Working against natural cycles")

        return challenges

    def interpret_hexagram(self, hexagram_lines: List[int], changing_lines: List[int]) -> Dict[str, Any]:
        """
        Interpret a hexagram and its changing lines.

        Args:
            hexagram_lines: The six lines of the hexagram
            changing_lines: Indices of changing lines

        Returns:
            dict: Interpretation details
        """
        # Analyze the primary hexagram
        lower_trigram, upper_trigram, hexagram = self.analyze_hexagram(hexagram_lines)

        interpretation = {
            "primary_hexagram": {
                "lower_trigram": lower_trigram,
                "upper_trigram": upper_trigram
            }
        }

        # If we have the hexagram in our database, add its information
        if hexagram:
            interpretation["primary_hexagram"].update({
                "number": hexagram.number,
                "name": f"{hexagram.chinese_name} - {hexagram.english_name}",
                "description": hexagram.description,
                "judgment": hexagram.judgment,
                "image": hexagram.image
            })

        # If there are changing lines, calculate the transformed hexagram
        if changing_lines:
            # Create the transformed hexagram
            transformed_lines = hexagram_lines.copy()
            for line_idx in changing_lines:
                # Flip the line (0->1, 1->0)
                transformed_lines[line_idx] = 1 - transformed_lines[line_idx]

            # Analyze the transformed hexagram
            trans_lower, trans_upper, trans_hexagram = self.analyze_hexagram(transformed_lines)

            interpretation["changing_lines"] = changing_lines
            interpretation["transformed_hexagram"] = {
                "lower_trigram": trans_lower,
                "upper_trigram": trans_upper
            }

            # If we have the transformed hexagram in our database, add its information
            if trans_hexagram:
                interpretation["transformed_hexagram"].update({
                    "number": trans_hexagram.number,
                    "name": f"{trans_hexagram.chinese_name} - {trans_hexagram.english_name}",
                    "description": trans_hexagram.description,
                    "judgment": trans_hexagram.judgment,
                    "image": trans_hexagram.image
                })

        # Add elemental analysis
        if lower_trigram in self.trigrams and upper_trigram in self.trigrams:
            lower_element = self.trigrams[lower_trigram].element
            upper_element = self.trigrams[upper_trigram].element

            interpretation["elemental_analysis"] = self._analyze_trigram_elements(lower_element, upper_element)

        # Generate guidance based on the current day's energy
        day_energy = self.calculate_daily_energy()
        interpretation["timing_guidance"] = self._generate_timing_guidance(day_energy)

        return interpretation

    def _analyze_trigram_elements(self, lower_element: Element, upper_element: Element) -> Dict[str, str]:
        """Analyze the interaction between trigram elements"""
        analysis = {}

        if lower_element == upper_element:
            analysis["relationship"] = "Harmony"
            analysis[
                "description"] = f"Both trigrams share the {lower_element.value} element, creating resonance and internal harmony."
        elif self.elements[lower_element].generates == upper_element:
            analysis["relationship"] = "Generation"
            analysis[
                "description"] = f"The lower {lower_element.value} element generates the upper {upper_element.value} element, creating supportive upward growth."
        elif self.elements[upper_element].generates == lower_element:
            analysis["relationship"] = "Descent"
            analysis[
                "description"] = f"The upper {upper_element.value} element generates the lower {lower_element.value} element, suggesting nourishment flowing downward."
        elif self.elements[lower_element].controlled_by == upper_element:
            analysis["relationship"] = "Control"
            analysis[
                "description"] = f"The upper {upper_element.value} element controls the lower {lower_element.value} element, suggesting restraint of the foundation."
        elif self.elements[upper_element].controlled_by == lower_element:
            analysis["relationship"] = "Restraint"
            analysis[
                "description"] = f"The lower {lower_element.value} element controls the upper {upper_element.value} element, suggesting a foundation that limits expression."
        else:
            analysis["relationship"] = "Neutral"
            analysis[
                "description"] = f"The {lower_element.value} and {upper_element.value} elements have no direct relationship, suggesting independence of action."

        return analysis

    def _generate_timing_guidance(self, day_energy: DayEnergy) -> Dict[str, str]:
        """Generate timing guidance based on the day's energy"""
        guidance = {}

        # Temporal alignment
        stem_element = day_energy.stem_branch.stem_element
        guidance["day_element"] = stem_element.value

        guidance["suggestion"] = f"Today's {stem_element.value} energy suggests: "

        if stem_element == Element.WATER:
            guidance["suggestion"] += "A time of deep reflection and intuitive understanding. "
            guidance["suggestion"] += "Flow with changes rather than resisting them."
        elif stem_element == Element.WOOD:
            guidance["suggestion"] += "A time of growth and new beginnings. "
            guidance["suggestion"] += "Plant seeds of intention with careful planning."
        elif stem_element == Element.FIRE:
            guidance["suggestion"] += "A time of illumination and activity. "
            guidance["suggestion"] += "Take action with clarity and awareness."
        elif stem_element == Element.EARTH:
            guidance["suggestion"] += "A time of grounding and stability. "
            guidance["suggestion"] += "Focus on practical matters and nurturing relationships."
        elif stem_element == Element.METAL:
            guidance["suggestion"] += "A time of refinement and precision. "
            guidance["suggestion"] += "Cut away what is unnecessary and clarify boundaries."

        # Add daily rhythm suggestion
        guidance["daily_rhythm"] = "Optimal times for action today:\n"

        element_times = {
            Element.WOOD: "Morning (5-9 AM): Ideal for starting new projects and creative thinking.",
            Element.FIRE: "Midday (10 AM-2 PM): Best for active work requiring clarity and expression.",
            Element.EARTH: "Afternoon (2-6 PM): Suitable for collaborative work and practical matters.",
            Element.METAL: "Evening (6-10 PM): Perfect for refining work and reflection.",
            Element.WATER: "Night (10 PM-2 AM): Conducive to deep insight and connection with intuition."
        }

        # Highlight the time associated with today's element
        guidance["daily_rhythm"] += f"• {element_times[stem_element]} (Today's focus)\n"

        # Add times for supportive elements (generating and generated)
        generating_element = None
        for element in Element:
            if self.elements[element].generates == stem_element:
                generating_element = element
                break

        generated_element = self.elements[stem_element].generates

        if generating_element:
            guidance["daily_rhythm"] += f"• {element_times[generating_element]} (Supportive energy)\n"

        guidance["daily_rhythm"] += f"• {element_times[generated_element]} (Flowing energy)\n"

        return guidance