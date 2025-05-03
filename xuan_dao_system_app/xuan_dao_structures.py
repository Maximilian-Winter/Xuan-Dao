# ✨ XUÁN DÀO CORE MODEL: THE FIVE ESSENCES ✨

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import datetime



# 🌊 The Five Elements - Wu Xing 五行
class Element(Enum):
    WATER = "水"  # 水 - Flow, darkness, wisdom, depth
    WOOD = "木"  # 木 - Growth, expansion, birth, flexibility
    FIRE = "火"  # 火 - Transformation, clarity, awareness, passion
    EARTH = "土"  # 土 - Stability, nurturing, centering, grounding
    METAL = "金"  # 金 - Refinement, precision, boundaries, structure


# 🌓 Primal Duality - Yin Yang 陰陽
class Polarity(Enum):
    YIN = "陰"  # 陰 - Receptive, dark, moon, female, passive
    YANG = "陽"  # 陽 - Creative, light, sun, male, active


# 🌱 Cosmic Phases - Wu De 五德
class Phase(Enum):
    BIRTH = "生"  # 生 - Beginning, initiation, emergence
    GROWTH = "長"  # 長 - Development, expansion, flourishing
    TRANSFORMATION = "化"  # 化 - Change, transformation, transition
    HARVEST = "收"  # 收 - Collection, reaping, accomplishment
    STORAGE = "藏"  # 藏 - Storage, rest, internalization


# 🧿 Element Attributes
@dataclass
class ElementAttributes:
    nature: str  # Fundamental nature
    dynamics: str  # Movement pattern
    color: str  # Associated color
    season: str  # Associated season
    direction: str  # Associated direction
    generates: Element  # Element it produces
    controlled_by: Element  # Element that controls it
    phase: Phase  # Associated cosmic phase
    polarity: Polarity  # Yin or Yang quality
    hex_color: str  # Color for visualization


# 🔮 Trigram (八卦 Ba Gua) - Building blocks of reality
@dataclass
class Trigram:
    name: str  # Chinese character
    pinyin: str  # Pinyin romanization
    meaning: str  # English meaning
    lines: Tuple[int, int, int]  # 1=Yang, 0=Yin (bottom to top)
    element: Element  # Associated element
    polarity: Polarity  # Dominant polarity
    direction: str  # Associated direction
    attribute: str  # Nature manifestation
    image: str  # Natural image
    family: str  # Family relationship
    body: str  # Body part
    quality: str  # Energetic quality


# 🌟 Flying Star (飛星 Fei Xing) - Cosmic energetic patterns
@dataclass
class FlyingStar:
    number: int  # Star number (1-9)
    name: str  # Chinese name
    element: Element  # Associated element
    quality: str  # Energetic quality
    color: str  # Traditional color
    direction: str  # Associated direction
    trigram: Optional[str]  # Associated trigram
    polarity: Polarity  # Yin or Yang quality


# 🌐 Palace (宮位 Gong Wei) - Spatial energy containers
@dataclass
class Palace:
    direction: str  # Direction name
    position: Tuple[int, int]  # Position in 3x3 grid (row, col)
    lo_shu_number: int  # Associated Lo Shu number
    trigram: Optional[str]  # Associated trigram
    element: Element  # Element affinity


# 📅 Stem-Branch Calendar System
@dataclass
class StemBranch:
    stem: str  # Heavenly Stem
    branch: str  # Earthly Branch
    stem_element: Element  # Element of stem
    branch_element: Element  # Element of branch
    stem_polarity: Polarity  # Polarity of stem
    combined_element: Element  # Dominant element


# 🔄 Day Energy - Daily cosmic pattern
@dataclass
class DayEnergy:
    date: datetime.date  # Gregorian date
    stem_branch: StemBranch  # Chinese calendar encoding
    flying_star: int  # Dominant flying star
    element_flow: List[Element]  # Element sequence
    quality: List[str]  # Energy qualities
    auspicious: List[str]  # Favorable activities
    challenging: List[str]  # Challenging influences


# 📊 Element Balance - Personal cosmic pattern
@dataclass
class ElementBalance:
    element_counts: Dict[Element, int]  # Count of each element
    strongest: Element  # Dominant element
    weakest: Element  # Deficient element
    recommended: Element  # Element to cultivate
    balancing_activities: Dict[Element, List[str]]  # Activities to balance


# 🎭 Hexagram (卦 Gua) - Complete I Ching symbol
@dataclass
class Hexagram:
    upper_trigram: Trigram  # Upper trigram
    lower_trigram: Trigram  # Lower trigram
    number: int  # King Wen sequence number
    chinese_name: str  # Chinese name
    english_name: str  # English name
    description: str  # Brief description
    judgment: str  # Oracle text
    image: str  # Image text
    changing_lines: List[int]  # Lines that are changing (0-5)


# 🕉️ XUÁN DÀO INITIALIZATION: AWAKENING THE COSMIC PATTERNS 🕉️

def initialize_five_elements() -> Dict[Element, ElementAttributes]:
    """Activate the five elemental forces that weave reality's tapestry"""
    elements = {}

    # 🌊 WATER - The Great Abyss
    elements[Element.WATER] = ElementAttributes(
        nature="寒冷、向下",  # Cold, descending
        dynamics="潛藏",  # Hidden potential
        color="黑色",  # Black
        season="冬",  # Winter
        direction="北",  # North
        generates=Element.WOOD,  # Generates Wood
        controlled_by=Element.EARTH,  # Controlled by Earth
        phase=Phase.STORAGE,  # Phase of storage
        polarity=Polarity.YIN,  # Yin quality
        hex_color="#4481c3"  # Deep blue
    )

    # 🌿 WOOD - The Rising Force
    elements[Element.WOOD] = ElementAttributes(
        nature="生發、條達",  # Growing, extending
        dynamics="升浮",  # Rising upward
        color="青色",  # Blue-green
        season="春",  # Spring
        direction="東",  # East
        generates=Element.FIRE,  # Generates Fire
        controlled_by=Element.METAL,  # Controlled by Metal
        phase=Phase.BIRTH,  # Phase of birth
        polarity=Polarity.YANG,  # Yang quality
        hex_color="#57a639"  # Vibrant green
    )

    # 🔥 FIRE - The Illuminator
    elements[Element.FIRE] = ElementAttributes(
        nature="炎熱、向上",  # Hot, ascending
        dynamics="飛騰",  # Rising rapidly
        color="紅色",  # Red
        season="夏",  # Summer
        direction="南",  # South
        generates=Element.EARTH,  # Generates Earth
        controlled_by=Element.WATER,  # Controlled by Water
        phase=Phase.GROWTH,  # Phase of growth
        polarity=Polarity.YANG,  # Yang quality
        hex_color="#d83e32"  # Brilliant red
    )

    # 🏔️ EARTH - The Stabilizer
    elements[Element.EARTH] = ElementAttributes(
        nature="中正、包容",  # Central, inclusive
        dynamics="安靜",  # Stable, quiet
        color="黃色",  # Yellow
        season="長夏",  # Late summer
        direction="中",  # Center
        generates=Element.METAL,  # Generates Metal
        controlled_by=Element.WOOD,  # Controlled by Wood
        phase=Phase.TRANSFORMATION,  # Phase of transformation
        polarity=Polarity.YIN,  # Yin quality
        hex_color="#d5a32d"  # Golden yellow
    )

    # ⚔️ METAL - The Refiner
    elements[Element.METAL] = ElementAttributes(
        nature="收斂、肅降",  # Contracting, purifying
        dynamics="沉降",  # Sinking
        color="白色",  # White
        season="秋",  # Autumn
        direction="西",  # West
        generates=Element.WATER,  # Generates Water
        controlled_by=Element.FIRE,  # Controlled by Fire
        phase=Phase.HARVEST,  # Phase of harvest
        polarity=Polarity.YIN,  # Yin quality
        hex_color="#b3b3b3"  # Silvery white
    )

    return elements


def initialize_trigrams() -> Dict[str, Trigram]:
    """Awaken the eight primordial forces that structure creation"""
    trigrams = {}

    # ☰ QIAN - The Creative
    trigrams["乾"] = Trigram(
        name="乾",
        pinyin="qián",
        meaning="The Creative",
        lines=(1, 1, 1),  # Three solid yang lines
        element=Element.METAL,
        polarity=Polarity.YANG,
        direction="northwest",
        attribute="heaven",
        image="天",  # Heaven
        family="父",  # Father
        body="頭",  # Head
        quality="強健"  # Strength
    )

    # ☱ DUI - The Joyous
    trigrams["兌"] = Trigram(
        name="兌",
        pinyin="duì",
        meaning="The Joyous",
        lines=(1, 1, 0),  # Broken line at top
        element=Element.METAL,
        polarity=Polarity.YIN,
        direction="west",
        attribute="lake",
        image="澤",  # Lake
        family="少女",  # Youngest Daughter
        body="口",  # Mouth
        quality="悅"  # Joy
    )

    # ☲ LI - The Clinging
    trigrams["離"] = Trigram(
        name="離",
        pinyin="lí",
        meaning="The Clinging",
        lines=(1, 0, 1),  # Broken middle line
        element=Element.FIRE,
        polarity=Polarity.YANG,
        direction="south",
        attribute="fire",
        image="火",  # Fire
        family="中女",  # Middle Daughter
        body="目",  # Eyes
        quality="麗"  # Radiance
    )

    # ☳ ZHEN - The Arousing
    trigrams["震"] = Trigram(
        name="震",
        pinyin="zhèn",
        meaning="The Arousing",
        lines=(0, 1, 1),  # Solid line at bottom
        element=Element.WOOD,
        polarity=Polarity.YANG,
        direction="east",
        attribute="thunder",
        image="雷",  # Thunder
        family="長子",  # Eldest Son
        body="足",  # Foot
        quality="動"  # Movement
    )

    # ☴ XUN - The Gentle
    trigrams["巽"] = Trigram(
        name="巽",
        pinyin="xùn",
        meaning="The Gentle",
        lines=(1, 0, 0),  # Solid line at top
        element=Element.WOOD,
        polarity=Polarity.YIN,
        direction="southeast",
        attribute="wind",
        image="風",  # Wind
        family="長女",  # Eldest Daughter
        body="股",  # Thigh
        quality="入"  # Penetration
    )

    # ☵ KAN - The Abysmal
    trigrams["坎"] = Trigram(
        name="坎",
        pinyin="kǎn",
        meaning="The Abysmal",
        lines=(0, 1, 0),  # Solid middle line
        element=Element.WATER,
        polarity=Polarity.YIN,
        direction="north",
        attribute="water",
        image="水",  # Water
        family="中子",  # Middle Son
        body="耳",  # Ear
        quality="陷"  # Danger
    )

    # ☶ GEN - The Keeping Still
    trigrams["艮"] = Trigram(
        name="艮",
        pinyin="gèn",
        meaning="The Keeping Still",
        lines=(0, 0, 1),  # Solid line at top
        element=Element.EARTH,
        polarity=Polarity.YANG,
        direction="northeast",
        attribute="mountain",
        image="山",  # Mountain
        family="少子",  # Youngest Son
        body="手",  # Hand
        quality="止"  # Stillness
    )

    # ☷ KUN - The Receptive
    trigrams["坤"] = Trigram(
        name="坤",
        pinyin="kūn",
        meaning="The Receptive",
        lines=(0, 0, 0),  # Three broken yin lines
        element=Element.EARTH,
        polarity=Polarity.YIN,
        direction="southwest",
        attribute="earth",
        image="地",  # Earth
        family="母",  # Mother
        body="腹",  # Belly
        quality="順"  # Receptivity
    )

    return trigrams


def initialize_flying_stars() -> Dict[int, FlyingStar]:
    """Activate the nine cosmic energies that flow through space and time"""
    stars = {}

    # ⭐ 1 White Water Star
    stars[1] = FlyingStar(
        number=1,
        name="一白水星",
        element=Element.WATER,
        quality="潛伏",  # Hidden potential
        color="white",
        direction="north",
        trigram="坎",  # Kan trigram
        polarity=Polarity.YIN
    )

    # ⭐ 2 Black Earth Star
    stars[2] = FlyingStar(
        number=2,
        name="二黑土星",
        element=Element.EARTH,
        quality="承載",  # Support
        color="black",
        direction="southwest",
        trigram="坤",  # Kun trigram
        polarity=Polarity.YIN
    )

    # ⭐ 3 Jade Wood Star
    stars[3] = FlyingStar(
        number=3,
        name="三碧木星",
        element=Element.WOOD,
        quality="生發",  # Growth
        color="blue",
        direction="east",
        trigram="震",  # Zhen trigram
        polarity=Polarity.YANG
    )

    # ⭐ 4 Green Wood Star
    stars[4] = FlyingStar(
        number=4,
        name="四綠木星",
        element=Element.WOOD,
        quality="漸進",  # Gradual progress
        color="green",
        direction="southeast",
        trigram="巽",  # Xun trigram
        polarity=Polarity.YIN
    )

    # ⭐ 5 Yellow Earth Star
    stars[5] = FlyingStar(
        number=5,
        name="五黃土星",
        element=Element.EARTH,
        quality="中正",  # Centered balance
        color="yellow",
        direction="center",
        trigram=None,  # No specific trigram (center)
        polarity=Polarity.YANG
    )

    # ⭐ 6 White Metal Star
    stars[6] = FlyingStar(
        number=6,
        name="六白金星",
        element=Element.METAL,
        quality="收斂",  # Contraction
        color="white",
        direction="northwest",
        trigram="乾",  # Qian trigram
        polarity=Polarity.YANG
    )

    # ⭐ 7 Red Metal Star
    stars[7] = FlyingStar(
        number=7,
        name="七赤金星",
        element=Element.METAL,
        quality="決斷",  # Decision
        color="red",
        direction="west",
        trigram="兌",  # Dui trigram
        polarity=Polarity.YIN
    )

    # ⭐ 8 White Earth Star
    stars[8] = FlyingStar(
        number=8,
        name="八白土星",
        element=Element.EARTH,
        quality="穩固",  # Stability
        color="white",
        direction="northeast",
        trigram="艮",  # Gen trigram
        polarity=Polarity.YANG
    )

    # ⭐ 9 Purple Fire Star
    stars[9] = FlyingStar(
        number=9,
        name="九紫火星",
        element=Element.FIRE,
        quality="光明",  # Brightness
        color="purple",
        direction="south",
        trigram="離",  # Li trigram
        polarity=Polarity.YANG
    )

    return stars


def initialize_palaces() -> Dict[str, Palace]:
    """Establish the nine sacred positions that contain cosmic energies"""
    palaces = {}

    # 🧭 The eight directions and center
    palaces["northwest"] = Palace(
        direction="northwest",
        position=(0, 0),
        lo_shu_number=4,
        trigram="乾",
        element=Element.METAL
    )

    palaces["north"] = Palace(
        direction="north",
        position=(0, 1),
        lo_shu_number=9,
        trigram="坎",
        element=Element.WATER
    )

    palaces["northeast"] = Palace(
        direction="northeast",
        position=(0, 2),
        lo_shu_number=2,
        trigram="艮",
        element=Element.EARTH
    )

    palaces["west"] = Palace(
        direction="west",
        position=(1, 0),
        lo_shu_number=3,
        trigram="兌",
        element=Element.METAL
    )

    palaces["center"] = Palace(
        direction="center",
        position=(1, 1),
        lo_shu_number=5,
        trigram=None,
        element=Element.EARTH
    )

    palaces["east"] = Palace(
        direction="east",
        position=(1, 2),
        lo_shu_number=7,
        trigram="震",
        element=Element.WOOD
    )

    palaces["southwest"] = Palace(
        direction="southwest",
        position=(2, 0),
        lo_shu_number=8,
        trigram="坤",
        element=Element.EARTH
    )

    palaces["south"] = Palace(
        direction="south",
        position=(2, 1),
        lo_shu_number=1,
        trigram="離",
        element=Element.FIRE
    )

    palaces["southeast"] = Palace(
        direction="southeast",
        position=(2, 2),
        lo_shu_number=6,
        trigram="巽",
        element=Element.WOOD
    )

    return palaces


def initialize_stems_branches() -> Tuple[List[str], List[str], Dict[str, Element], Dict[str, Element]]:
    """Activate the celestial time-tracking system of stems and branches"""
    # 天干 - Heavenly Stems
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    # 地支 - Earthly Branches
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

    # Stem to Element mapping
    stem_element_map = {
        "甲": Element.WOOD, "乙": Element.WOOD,  # Jia, Yi - Wood
        "丙": Element.FIRE, "丁": Element.FIRE,  # Bing, Ding - Fire
        "戊": Element.EARTH, "己": Element.EARTH,  # Wu, Ji - Earth
        "庚": Element.METAL, "辛": Element.METAL,  # Geng, Xin - Metal
        "壬": Element.WATER, "癸": Element.WATER  # Ren, Gui - Water
    }

    # Branch to Element mapping
    branch_element_map = {
        "子": Element.WATER, "丑": Element.EARTH,  # Zi (Rat), Chou (Ox)
        "寅": Element.WOOD, "卯": Element.WOOD,  # Yin (Tiger), Mao (Rabbit)
        "辰": Element.EARTH, "巳": Element.FIRE,  # Chen (Dragon), Si (Snake)
        "午": Element.FIRE, "未": Element.EARTH,  # Wu (Horse), Wei (Goat)
        "申": Element.METAL, "酉": Element.METAL,  # Shen (Monkey), You (Rooster)
        "戌": Element.EARTH, "亥": Element.WATER  # Xu (Dog), Hai (Pig)
    }

    return heavenly_stems, earthly_branches, stem_element_map, branch_element_map